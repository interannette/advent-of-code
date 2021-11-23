package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

const (
	empty = iota
	taken
	floor
)

func getInput(fileName string) [][]int {
	input := make([][]int, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		chars := strings.Split(line, "")
		row := make([]int, 0)
		for _, c := range chars {
			if c == "L" {
				row = append(row, empty)
			} else if c == "." {
				row = append(row, floor)
			} else {
				panic("unknown char in input")
			}
		}
		input = append(input, row)
	}

	return input
}

func print(input [][]int) {
	for _, r := range input {
		for _, c := range r {
			if c == empty {
				fmt.Print("L")
			} else if c == floor {
				fmt.Print(".")
			} else {
				fmt.Print("#")
			}
		}
		fmt.Print("\n")
	}
}

func iterate(grid [][]int) ([][]int, bool) {
	new_grid := make([][]int, len(grid))
	changed := false
	for i := range grid {
		new_row := make([]int, len(grid[i]))
		for j := range grid[i] {
			if grid[i][j] == floor {
				new_row[j] = floor
			} else {
				count := countOccupied(grid, i, j)
				if grid[i][j] == empty && count == 0 {
					new_row[j] = taken
					changed = true
				} else if grid[i][j] == taken && count >= 4 {
					new_row[j] = empty
					changed = true
				} else {
					new_row[j] = grid[i][j]
				}
			}
		}
		new_grid[i] = new_row
	}

	return new_grid, changed
}

func countOccupied(grid [][]int, i int, j int) int {
	count := 0

	startX := i - 1
	if i == 0 {
		startX = 0
	}

	endX := i + 1
	if i == len(grid)-1 {
		endX = i
	}

	startY := j - 1
	if j == 0 {
		startY = 0
	}

	endY := j + 1
	if j == len(grid[i])-1 {
		endY = j
	}

	for x := startX; x <= endX; x++ {
		for y := startY; y <= endY; y++ {
			if x == i && y == j {
				// skip counting the spot in question
			} else {
				if grid[x][y] == taken {
					count++
				}
			}
		}
	}

	return count
}

func countAll(grid [][]int) int {
	count := 0
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == taken {
				count++
			}
		}
	}

	return count
}

func main() {

	input := getInput("input.txt")

	changed := true
	for changed {
		input, changed = iterate(input)
	}

	count := countAll(input)
	fmt.Println(count)
}
