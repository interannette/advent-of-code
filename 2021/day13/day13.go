package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"regexp"
)
type fold struct {
	direction string
	line int
}

// fold along y=7
var foldRegex = regexp.MustCompile("^fold along (\\w+)=(\\d+)$")
func ParseFold(s string) fold {
	match := foldRegex.FindStringSubmatch(s)
	
	if len(match) < 1 {
		panic("could not parse fold")
	} 

	direction := match[1]
	line, _ := strconv.Atoi(match[2])

	return fold {
		direction: direction,
		line : line,
	}
}

type pos struct {
	x int
	y int
}

//x,y
func ParsePos(s string) pos {
	tokens := strings.Split(s, ",")
	xVal, _ := strconv.Atoi(tokens[0])
	yVal, _ := strconv.Atoi(tokens[1])
	return pos {
		x : xVal,
		y:yVal,
	}
}

func NewPos(x int, y int) pos {
	return pos {
		x:x,
		y:y,
	}
}

type paper struct {
	points map[pos]bool
	folds []fold
	maxX int
	maxY int
}

func NewPaper() paper {
	return paper {
		points : make(map[pos]bool),
		folds : make([]fold,0),
	}
}

func (p paper) String() string {

	var output strings.Builder	
	for i := 0; i <= p.maxY; i++ {
		for j:=0; j <= p.maxX; j++ {
			if p.points[NewPos(j,i)] {
				output.WriteString("#")
			} else {
				output.WriteString(".")
			}
		}
		output.WriteString("\n")
	}

	output.WriteString("Max x: " + strconv.Itoa(p.maxX) + "\n")
	output.WriteString("Max y: " + strconv.Itoa(p.maxY) + "\n")

	return output.String()
}

func (p paper) PrintPoints() {
	for point, exists := range p.points {
		fmt.Printf("%v, %v\n", point, exists)
	}
}

func (p *paper) addPos(newPos pos) {
	p.points[newPos] = true

	if newPos.x > p.maxX {
		p.maxX = newPos.x
	}

	if newPos.y > p.maxY {
		p.maxY = newPos.y
	}
}

func (p *paper) addFold(newFold fold) {
	p.folds = append(p.folds, newFold)
}

func (p *paper) executeFold() bool {

	if len(p.folds) <= 0 {
		return false
	}

	f := p.folds[0]
	p.folds = p.folds[1:]

	if f.direction == "y" {
		p.doHorizontalFold(f.line)
	} else {
		p.doVerticalFold(f.line)
	}

	return true
}

func (p *paper) doHorizontalFold(value int) {
	//x,value+diff -> x,value-diff
	for point, exists := range p.points {
		if exists {
			// if y > value,
			diff := point.y - value
			if diff > 0 {
				p.points[point] = false
				if diff <= value {
					p.points[NewPos(point.x,value-diff)] = true
				} // else will fold "off" the paper -- assume we ignore
			}
		}
	}

	//update max y
	p.maxY = value-1
}

func (p *paper) doVerticalFold(value int) {
	//value+diff,y -> value-diff,y
	for point, exists := range p.points {
		if exists {
			// if x > value,
			diff := point.x - value
			if diff > 0 {
				p.points[point] = false
				if diff <= value {
					p.points[NewPos(value-diff, point.y)] = true
				} // else will fold "off" the paper -- assume we ignore
			}
		}
	}

	//update max x
	p.maxX = value-1
}

func (p paper) countPoints() int {
	count := 0

	for _, exists := range p.points {
		if exists {
			count++
		}
	}
	return count
}

func getInput(fileName string) paper {

	input := NewPaper()

	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	foldsStarted := false
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			foldsStarted = true
		} else if foldsStarted {
			input.addFold(ParseFold(line))
		} else {
			input.addPos(ParsePos(line))
		}
	}

	return input
}

func main() {
	file := "input"

	p := getInput(file + ".txt")

	rounds := 0
	for p.executeFold() {
		rounds++
		fmt.Printf("Round %d complete\n", rounds)
	}
	fmt.Println(p)
}