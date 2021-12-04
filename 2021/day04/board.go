package main

import (
	"strings"
)

type board struct {
	marks [][]bool
	numbers map[int][]int
}

func NewBoard(lines []string) board {
	marks := make([][]bool, 5)
	numbers := make(map[int][]int)

	for r, l := range lines {

		tokens := strings.Fields(l)
		curRow := convertToInts(tokens)
		for c, n := range curRow {
			numbers[n] = []int {r, c}
		}

		marks[r] = make([]bool, 5)
	}

	return board {
		marks : marks,
		numbers : numbers,
	}
}

func (b board) String() string {
	var output strings.Builder
	for i := 0; i < len(b.marks); i++ {
		for j := 0; j < len(b.marks[i]); j++ {
			if j != 0 {
				output.WriteString(" ")
			}
			if b.marks[i][j] {
				output.WriteString("*")
			} else {
				output.WriteString("_")
			}
		}
		output.WriteString("\n")
	}
	output.WriteString("\n")
	return output.String()
}

func (b board) MarkNumber(n int) (board, bool) {
	pos, exists := b.numbers[n]

	if exists {
		row := pos[0]
		col := pos[1]
		b.marks[row][col] = true

		win := b.checkRow(row) || b.checkCol(col)
		return b, win
	}
	return b, false
}

func (b board) checkRow(row int) bool {
	for i := 0; i < 5; i++ {
		if !b.marks[row][i] {
			return false
		}
	}
	return true
}

func (b board) checkCol(col int) bool {
	for i := 0; i < 5; i++ {
		if !b.marks[i][col] {
			return false
		}
	}
	return true
}

func (b board) SumUnmarked() int {
	sum := 0
	for n, pos := range b.numbers {
		if !b.marks[pos[0]][pos[1]] {
			sum += n
		}
	}
	return sum
}
