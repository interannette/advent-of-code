package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

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

func (p pos) neighbors() []pos {
	neighbors := make([]pos, 0)

	xMinusValid := p.x > 0
	xPlusValid := p.x < 9
	yMinusValid := p.y > 0
	yPlusValid := p.y < 9

	if xMinusValid {
		if yPlusValid {	
			neighbors = append(neighbors, NewPos(p.x-1, p.y+1))
		}
		neighbors = append(neighbors, NewPos(p.x-1, p.y))
		if yMinusValid {
			neighbors = append(neighbors, NewPos(p.x-1, p.y-1))
		}
	}

	if yMinusValid {
		neighbors = append(neighbors, NewPos(p.x, p.y-1))
	}

	if yPlusValid {
		neighbors = append(neighbors, NewPos(p.x, p.y+1))
	}

	if xPlusValid {
		if yPlusValid {
			neighbors = append(neighbors, NewPos(p.x+1, p.y+1))
		}
		if yMinusValid {
			neighbors = append(neighbors, NewPos(p.x+1, p.y-1))
		}
		neighbors = append(neighbors, NewPos(p.x+1, p.y))
	}		
	return neighbors
}

type posQueue struct {
	positions []pos
	current int
}

func NewPosQueue() posQueue{
	return posQueue {
		positions: make([]pos, 0),
		current :0,
	}
}

func (q posQueue) String() string {
	var output strings.Builder
	output.WriteString("Queue len: ")
	output.WriteString(strconv.Itoa(len(q.positions)))
	output.WriteString(". Current ")
	output.WriteString(strconv.Itoa(q.current))
	return output.String()
}

func (q *posQueue) push(p pos) {
	q.positions = append(q.positions, p)
}

func (q *posQueue) pushSlice(p []pos) {
	q.positions = append(q.positions, p...)
}

// not resizing, see how bad it goes...
func (q *posQueue) pop() pos {
	p := q.positions[q.current]
	q.current++
	return p
}

func (q posQueue) hasMore() bool {
	return q.current < len(q.positions)
}

type octopus struct {
	energy int
	flashed bool
}

func NewOctopus(e int) octopus {
	return octopus {
		energy: e,
		flashed: false,
	}
}

func (o octopus) String() string {
	s := strconv.Itoa(o.energy)
	if o.flashed {
		s = s+"*"
	} else {
		s = s+"_"
	}
	return s
}

func (o *octopus) addOneAndCheckFlash() bool {
	o.energy += 1
	if o.flashed {
		return false
	} else if o.energy > 9 {
		o.flashed = true
		return true
	} else {
		return false
	}
}

type grid struct {
	octopi map[pos]octopus
}

func NewGrid(lines []string) grid {
	g := make(map[pos]octopus)
	for i, l := range lines {
		chars := strings.Split(l, "")
		for j, c := range chars {
			num, _ := strconv.Atoi(c)
			g[NewPos(i,j)] = NewOctopus(num)
		}
	}

	return grid {
		octopi: g,
	}
}

func (g *grid) advanceStep(debug bool) int {
	flashes := 0

	posToAddTo := NewPosQueue()
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			posToAddTo.push(NewPos(i,j))
		}
	}

	if debug {
		fmt.Printf("Starting advance with queue %v\n", posToAddTo)
	}

	for posToAddTo.hasMore() {
		p := posToAddTo.pop()
		o := g.octopi[p]

		flashed := o.addOneAndCheckFlash()
		if flashed {
			flashes++
			n := p.neighbors()
			posToAddTo.pushSlice(n)
			if debug {
				fmt.Printf("%v flashed. Adding neighbors %v\n", p, n)
			}
		}
		g.octopi[p] = o
	}

	g.reset()
	return flashes
}

func (g *grid) reset() {
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			p := NewPos(i,j)
			o := g.octopi[p]
			if o.flashed {
				o.energy = 0
				o.flashed = false
			}
			g.octopi[p] = o
		}
	}	
}

func (g grid) String() string {
	var output strings.Builder
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			p := NewPos(i,j)
			if j != 0 {
				output.WriteString(" ")
			}
			output.WriteString(g.octopi[p].String())
		}
		output.WriteString("\n")
	}
	return output.String()
}

func getInput(fileName string) grid {

	input := make([]string, 0)

	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	return NewGrid(input)
}

func doPart1(g grid) {
	flashes := 0
	for i:=1; i<=100;i++ {
		flashes += g.advanceStep(false)
	}
	fmt.Printf("Total flashes %d\n", flashes)
}

func doPart2(g grid) {
	flashes :=0
	rounds := 0
	for flashes < 100 {
		rounds++
		flashes = g.advanceStep(false)
	}

	fmt.Printf("All flash at round %d\n", rounds)
}

func main() {
	file := "input"
	part := 2

	grid := getInput(file + ".txt")

	if part == 1 {
		doPart1(grid)
	} else {
		doPart2(grid)
	}
}