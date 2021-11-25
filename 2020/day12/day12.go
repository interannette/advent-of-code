package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"regexp"
	"strconv"
)

type action int

const (
	north action = iota
	south
	east
	west
	left
	right
	forward
)

func parseAction(s string) action {
	switch s {
	case "N":
		return north
	case "S":
		return south
	case "E":
		return east
	case "W":
		return west
	case "L":
		return left
	case "R":
		return right
	case "F":
		return forward
	default:
		panic("Could not parse action")
	}
}

func (a action) String() string {
	switch a {
	case north:
		return "N"
	case south:
		return "S"
	case east:
		return "E"
	case west:
		return "W"
	case left:
		return "L"
	case right:
		return "R"
	case forward:
		return "F"
	default:
		return "unknown"
	}
}

type instruction struct {
	v int
	a action
}

func (i instruction) String() string {
	return fmt.Sprintf("%s%d", i.a, i.v)
}

var instructionRegex = regexp.MustCompile(`^(?P<action>\w{1})(?P<value>\d+)$`)

func parseInstruction(s string) instruction {
	match := instructionRegex.FindStringSubmatch(s)

	if len(match) == 0 {
		fmt.Printf("Could not parse instruction from %s\n", s)
	}

	a := parseAction(match[1])
	v, _ := strconv.Atoi(match[2])

	i := instruction{
		a: a,
		v: v,
	}

	return i
}

type postion struct {
	x int
	y int
	d int
}

func (p postion) String() string {
	return fmt.Sprintf("(%d,%d)%d", p.x, p.y, p.d)
}

func getInput(fileName string) []instruction {
	input := make([]instruction, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, parseInstruction(scanner.Text()))
	}

	return input
}

func applyInstruction(i instruction, p postion) postion {
	new_pos := p

	switch i.a {
	case north:
		new_pos.y = new_pos.y + i.v
	case south:
		new_pos.y = new_pos.y - i.v
	case east:
		new_pos.x = new_pos.x + i.v
	case west:
		new_pos.x = new_pos.x - i.v
	case left:
		new_pos.d = consolidateAngle(new_pos.d - i.v)
	case right:
		new_pos.d = consolidateAngle(new_pos.d + i.v)
	case forward:
		switch p.d {
		case 0:
			new_pos.y = new_pos.y + i.v
		case 90:
			new_pos.x = new_pos.x + i.v
		case 180:
			new_pos.y = new_pos.y - i.v
		case 270:
			new_pos.x = new_pos.x - i.v
		default:
			panic("only handling 90 degree angles")
		}
	default:
		panic("unknown action")
	}

	return new_pos
}

// 0 - 360 degrees. 0 = N
func consolidateAngle(i int) int {
	// assuming i is postitive
	if i >= 0 {
		return i % 360
	} else {
		return 360 + i
	}
}

func main() {
	input := getInput("input.txt")

	pos := postion{
		x: 0,
		y: 0,
		d: 90,
	}

	for _, ins := range input {
		pos = applyInstruction(ins, pos)
	}

	fmt.Printf("Final position %s. Distance %.0f\n", pos, math.Abs(float64(pos.x))+math.Abs(float64(pos.y)))
}
