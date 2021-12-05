package main

import (
	"strings"
	"strconv"
)

type Map struct {
	grid [][]int
}

func NewMap(maxX int, maxY int) Map {
	g := make([][]int, 0)
	for i := 0; i <= maxY; i++ {
		r := make([]int, maxX+1)
		g = append(g, r)
	}

	return Map {
		grid : g,
	}
}

func (m Map) String() string {
	var output strings.Builder
	for i := 0; i < len(m.grid); i++ {
		for j := 0; j < len(m.grid[i]); j++ {
			if j != 0 {
				output.WriteString(" ")
			}
			output.WriteString(strconv.Itoa(m.grid[i][j]))
		}
		output.WriteString("\n")
	}
	output.WriteString("\n")
	return output.String()
}

func (m Map) MarkPos(x int, y int) Map {
	m.grid[y][x] += 1
	return m
}


func (m Map) SumMultiples() int {
	count := 0
	for _, r := range m.grid {
		for _, v := range r {
			if v > 1 {
				count++
			}
		}
	}
	return count
}