package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type pos struct {
	x int
	y int
}

func NewPos(i int, j int) pos {
	return pos{
		x: i,
		y: j,
	}
}

func (p pos) String() string {
	return "(" + strconv.Itoa(p.x) + "," + strconv.Itoa(p.y) + ")"
}

func (c cave) neighbors(p pos) []pos {
	neighbors := make([]pos, 0)

	// up x-1, y
	// if p.x > 0 {
	// 	neighbors = append(neighbors, NewPos(p.x-1, p.y))
	// }

	// down x+1, y
	if p.x < c.size-1 {
		neighbors = append(neighbors, NewPos(p.x+1, p.y))
	}

	// left x, y-1
	// if p.y > 0 {
	// 	neighbors = append(neighbors, NewPos(p.x, p.y-1))
	// }
	// right x, y+1
	if p.y < c.size-1 {
		neighbors = append(neighbors, NewPos(p.x, p.y+1))
	}

	return neighbors
}

func (c cave) riskOfPos(p pos) uint64 {
	return c.scores[p]
}

type cave struct {
	scores map[pos]uint64
	size   int
}

func (c cave) String() string {
	var output strings.Builder
	for i := 0; i < c.size; i++ {
		for j := 0; j < c.size; j++ {
			p := NewPos(j, i)
			if j != 0 {
				output.WriteString(" ")
			}
			output.WriteString(strconv.Itoa(int(c.riskOfPos(p))))
		}
		output.WriteString("\n")
	}

	return output.String()
}

func NewCave(lines []string, part2 bool) cave {
	grid := make(map[pos]uint64)
	for i, l := range lines {
		chars := strings.Split(l, "")
		for j, c := range chars {
			num, _ := strconv.Atoi(c)
			grid[NewPos(j, i)] = uint64(num)
		}
	}
	size := len(lines)

	if part2 {
		newGrid := make(map[pos]uint64)
		originalSize := size
		size = size * 5
		for i := 0; i < size; i++ {
			for j := 0; j < size; j++ {
				p := NewPos(i, j)
				risk := exntendedRisk(p, grid, originalSize)
				newGrid[p] = risk
			}
		}
		grid = newGrid
	}

	return cave{
		scores: grid,
		size:   size,
	}
}

func exntendedRisk(p pos, originalGrid map[pos]uint64, originalSize int) uint64 {
	//each time the tile repeats to the right or downward,
	// all of its risk levels are 1 higher than the tile immediately up or left of it.
	// However, risk levels above 9 wrap back around to 1.
	xRemainder := p.x % originalSize
	xMultiple := p.x / originalSize

	yRemainder := p.y % originalSize
	yMultiple := p.y / originalSize

	originalRisk := originalGrid[NewPos(xRemainder, yRemainder)]
	risk := int(originalRisk) + xMultiple + yMultiple
	riskRemainder := risk % 10
	riskMultiple := risk / 10

	totalRisk := riskRemainder + riskMultiple

	return uint64(totalRisk)
}

func (c cave) allPos() ([]pos, pos) {
	all := make([]pos, 0)

	for i := 0; i < c.size; i++ {
		for j := 0; j < c.size; j++ {
			all = append(all, NewPos(i, j))
		}
	}
	return all, NewPos(c.size-1, c.size-1)
}

func (c cave) doDijkstra() uint64 {
	/*
	   1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
	   2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.
	   The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the
	   starting node. Since initially no path is known to any other vertex than the source itself (which is a path of length zero),
	   all other tentative distances are initially set to infinity. Set the initial node as current.[15]
	*/
	all, end := c.allPos()
	start := NewPos(0, 0)
	visited := make(map[pos]bool)
	distances := make(map[pos]uint64)
	for _, p := range all {
		visited[p] = false
		distances[p] = math.MaxUint64
	}
	visited[start] = true
	distances[start] = 0
	current := start

	done := false

	for !done {
		/*
		   3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
		   Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
		   For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2,
		   then the distance to B through A will be 6 + 2 = 8.
		   If B was previously marked with a distance greater than 8 then change it to 8.
		   Otherwise, the current value will be kept.
		*/
		distOfCurrent := distances[current]
		neighbors := c.neighbors(current)
		for _, n := range neighbors {
			if !visited[n] {
				risk := c.riskOfPos(n)
				newDist := distOfCurrent + risk
				existingDist := distances[n]
				if newDist < existingDist {
					distances[n] = newDist
				}
			}
		}

		/*
		   4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and
		   remove it from the unvisited set. A visited node will never be checked again.
		*/
		visited[current] = true
		/*
			   5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest
			   tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when
				there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
		*/
		done = visited[end]
		/*
		   6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current
		   node, and go back to step 3.
		*/
		current = c.findNextPos(visited, distances)
	}

	return distances[end]
}

func (c cave) findNextPos(visited map[pos]bool, distances map[pos]uint64) pos {

	var next pos
	minDist := uint64(math.MaxUint64)
	for p, v := range visited {
		if !v {
			dist := distances[p]
			if dist < minDist {
				minDist = dist
				next = p
			}
		}
	}

	return next
}

func getInput(fileName string, part2 bool) cave {

	input := make([]string, 0)

	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	return NewCave(input, part2)
}

func main() {
	file := "input"
	part2 := true
	c := getInput(file+".txt", part2)

	risk := c.doDijkstra()
	fmt.Println(risk)
}
