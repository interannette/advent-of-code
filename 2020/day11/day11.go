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

func iterate(grid [][]int, part int) ([][]int, bool) {
	threshold := 3 + part // 4 for part 1, 5 for part 2

	new_grid := make([][]int, len(grid))
	changed := false
	for i := range grid {
		new_row := make([]int, len(grid[i]))
		for j := range grid[i] {
			if grid[i][j] == floor {
				new_row[j] = floor
			} else {
				count := countOccupied(grid, i, j, part)
				if grid[i][j] == empty && count == 0 {
					new_row[j] = taken
					changed = true
				} else if grid[i][j] == taken && count >= threshold {
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

func countOccupied(grid [][]int, i int, j int, part int) int {
	if part == 1 {
		return countAdjacentOccupied(grid, i, j)
	} else {
		return countLineOfSight(grid, i, j)
	}
}

func countAdjacentOccupied(grid [][]int, i int, j int) int {
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

func countLineOfSight(grid [][]int, i int, j int) int {
	count := 0

	// (1, 0)
	for x := i + 1; x < len(grid); x++ {
		s := grid[x][j]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}
	// (-1, 0)
	for x := i - 1; x >= 0; x-- {
		s := grid[x][j]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}
	// (0, -1)
	for y := j - 1; y >= 0; y-- {
		s := grid[i][y]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}
	// (0, 1)
	for y := j + 1; y < len(grid[i]); y++ {
		s := grid[i][y]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}
	// (1, 1)
	for z := 1; i+z < len(grid) && j+z < len(grid[i]); z++ {
		s := grid[i+z][j+z]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}
	// (1, -1)
	for z := 1; i+z < len(grid) && j-z >= 0; z++ {
		s := grid[i+z][j-z]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}

	// (-1, -1)
	for z := 1; i-z >= 0 && j-z >= 0; z++ {
		s := grid[i-z][j-z]
		if s == taken {
			count++
			break
		} else if s == empty {
			break
		}
	}

	// (-1, 1)
	for z := 1; i-z >= 0 && j+z < len(grid[i]); z++ {
		s := grid[i-z][j+z]
		if grid[i-z][j+z] == taken {
			count++
			break
		} else if s == empty {
			break
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
	part := 2
	input := getInput("input.txt")

	changed := true
	for changed {
		input, changed = iterate(input, part)
	}

	count := countAll(input)
	fmt.Println(count)
}
