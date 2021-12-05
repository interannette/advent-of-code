package main

import (
	"regexp"
	"strconv"
	"fmt"
)

type pos struct {
	x int
	y int
}
type line struct {
	start pos
	end pos
}

// 0,9 -> 5,9
var inputRegex = regexp.MustCompile("^(\\d+),(\\d+) -> (\\d+),(\\d+)$")
func NewLine(input string) line {
	match := inputRegex.FindStringSubmatch(input)

	if len(match) <= 0 {
		panic("could not parse line")
	}

	x,_ := strconv.Atoi(match[1])
	y,_ := strconv.Atoi(match[2])
	s := pos {
		x: x,
		y: y,
	}

	x,_ = strconv.Atoi(match[3])
	y,_ = strconv.Atoi(match[4])
	e := pos {
		x:x,
		y:y,
	}

	l := line {
		start : s,
		end : e,
	}
	return l

}

func (l line) String() string {
	return fmt.Sprintf("(%d,%d) > (%d,%d)", l.start.x, l.start.y, l.end.x, l.end.y)
}

func (l line) IsNotDiagonal() bool {
	return l.start.x == l.end.x || l.start.y == l.end.y
}

func (l line) MaxX() int {
	if l.start.x >= l.end.x {
		return l.start.x
	} else {
		return l.end.x
	}
}

func (l line) MaxY() int {
	if l.start.y >= l.end.y {
		return l.start.y
	} else {
		return l.end.y
	}}

func (l line) AllPos() []pos {

	posList := make([]pos, 0)
	if l.start.x == l.end.x {

		min := l.start.y
		max := l.end.y
		if l.end.y < min {
			min = l.end.y
			max = l.start.y
		}

		for i := min; i <= max; i++ {
			posList = append(posList, pos {
				x: l.start.x, 
				y: i,
			})
		}

	} else if l.start.y == l.end.y {

		min := l.start.x
		max := l.end.x
		if l.end.x < min {
			min = l.end.x
			max = l.start.x
		}

		for i := min; i <= max; i++ {
			posList = append(posList, pos {
				x: i, 
				y: l.start.y,
			})
		}

	} else {

		slope := (l.end.x - l.start.x) / (l.end.y - l.start.y)

		minX := l.start.x
		maxX := l.end.x
		startY := l.start.y
		if l.end.x < minX {
			minX = l.end.x
			maxX = l.start.x
			startY = l.end.y
		}

		for i := 0; i <= (maxX-minX); i++ {
			posList = append(posList, pos {
				x: minX + i,
				y: startY + slope*i,
			})
		}

	}

	return posList
}