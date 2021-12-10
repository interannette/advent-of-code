package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"sort"
)

type heightmap struct {
	heights [][]int
	rows int
	cols int
}

type pos struct {
	x int
	y int
}

func NewPos(i int, j int) pos {
	return pos {
		x: i,
		y: j,
	}
}

func (p pos) String() string {
	return "("+ strconv.Itoa(p.x)+","+strconv.Itoa(p.y)+")"
}

func (h heightmap) value(p pos) int {
	return h.heights[p.x][p.y]
}

func (h heightmap) String() string {
	var output strings.Builder
	for i := 0; i < h.rows; i++ {
		for j := 0; j < h.cols; j++ {
			if j != 0 {
				output.WriteString(" ")
			}
			s := strconv.Itoa(h.heights[i][j])
			output.WriteString(s)
		}
		output.WriteString("\n")
	}
	output.WriteString("\n")
	return output.String()
}

func (h heightmap) adjacent(i int, j int) ([]int, []pos) {
	values := make([]int, 0)
	neighbors := make([]pos, 0)
				// down: i-1, j
				if i-1 >= 0 {
					values = append(values, h.heights[i-1][j])
					neighbors = append(neighbors, NewPos(i-1, j))
				}
				// up: i+1, j
				if i+1 < h.rows {
					values = append(values, h.heights[i+1][j])
					neighbors = append(neighbors, NewPos(i+1, j))
				}
				// left: i, j-1
				if j-1 >= 0 {
					values = append(values, h.heights[i][j-1])
					neighbors = append(neighbors, NewPos(i, j-1))

				}
				// right: i , j+1
				if j+1 < h.cols {
					values = append(values, h.heights[i][j+1])
					neighbors = append(neighbors, NewPos(i, j+1))
				}

	return values, neighbors
}

func (h heightmap) neighbors(p pos) []pos {
	_, n := h.adjacent(p.x, p.y)
	return n
}

func getInput(fileName string) heightmap {

	input := make([][]int, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		digits := strings.Split(line, "")
		row := make([]int, 0)
		for _, d := range digits {
			n, _ := strconv.Atoi(d)
			row = append(row, n)
		}
		input = append(input, row)
		
	}

	return heightmap {
		heights: input,
		rows: len(input),
		cols: len(input[0]),
	}
}

func findMinimums(h heightmap) []pos {
	minimums := make([]pos, 0)
	for i, row := range h.heights {
		for j, n := range row {
			isLocalMin := true
			neighbors, _ := h.adjacent(i,j)
			for _, v := range neighbors {
				if v <= n {
					isLocalMin = false
				}
			}
			if isLocalMin {
				fmt.Printf("At %d, %d. Value %d, neighbors %v\n", i, j, n, neighbors)
				minimums = append(minimums, NewPos(i,j))
			}
		}
	}
	return minimums
}

func findBasins(h heightmap) [][]pos {
	minimums := findMinimums(h)
	basins := make([][]pos, 0)

	for _, minimum := range minimums {
		
		basinAsMap := findBasinForMin(h, minimum)
		basin := make([]pos, 0)
		for k, v := range basinAsMap {
			if v {
				basin = append(basin, k)
			}
		}
		basins = append(basins, basin)
	}

	// remove duplicates?
	return basins
}

func findBasinForMin(h heightmap, minimum pos) map[pos]bool {
	fmt.Printf("Finding basin for %v\n", minimum)
	basin := make(map[pos]bool)
	basin[minimum] = true

	expandBasin(h, minimum, basin)
	return basin
}

func expandBasin(h heightmap, p pos, basin map[pos]bool) map[pos]bool {
	fmt.Printf("Expanding basin for %v\n", p)
	neighbors := h.neighbors(p)
	for _, n := range neighbors {
		fmt.Printf("checking neighbor %v\n", p)
		_, exists := basin[n]
		fmt.Printf("checked neighbor %v\n", p)
		if !exists {
			fmt.Printf("neighbor needs consideration\n")
			if h.value(n) == 9 {
				fmt.Printf("neighbor is 9. done\n")
				basin[n] = false
			} else {
				fmt.Printf("neighbor is not 9. recurse\n")
				basin[n] = true
				expandBasin(h, n, basin)
			}
		} else {
			fmt.Printf("already handled %v\n",n)
		}
	}

	return basin
}

func computeRisk(h heightmap, minimums []pos) int {
	risk := 0
	for _, p := range minimums {
		risk += (h.value(p) + 1)
	}
	return risk
}

func main() {
	file := "input"
	part := 2

	input := getInput(file + ".txt")
	
	if part == 1 {
		minimums := findMinimums(input)
		risk := computeRisk(input, minimums)
		fmt.Println(risk)
	} else {
		basins := findBasins(input)
		fmt.Printf("Found %d basins %v\n", len(basins), basins)
		sizes := make([]int, 0)
		for _, basin := range basins {
			sizes = append(sizes, len(basin))
		}
		sort.Ints(sizes)
		fmt.Printf("Three largest basins: %d, %d, %d. Product %d\n", sizes[len(sizes)-1],
						sizes[len(sizes)-2], sizes[len(sizes)-3],
						sizes[len(sizes)-1]*sizes[len(sizes)-2]*sizes[len(sizes)-3])
	}
}