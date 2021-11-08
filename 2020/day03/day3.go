package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type trees struct {
	grid [][]bool
	r    int
	c    int
}

func (t trees) get(i int, j int) bool {
	return t.grid[i][j%t.c]
}

func getInput(sample bool) trees {
	input := make([]string, 0)
	if sample {
		input = append(input, "..##.......")
		input = append(input, "#...#...#..")
		input = append(input, ".#....#..#.")
		input = append(input, "..#.#...#.#")
		input = append(input, ".#...##..#.")
		input = append(input, "..#.##.....")
		input = append(input, ".#.#.#....#")
		input = append(input, ".#........#")
		input = append(input, "#.##...#...")
		input = append(input, "#...##....#")
		input = append(input, ".#..#...#.#")
	} else {
		file, err := os.Open("input.txt")
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			input = append(input, scanner.Text())
		}
	}

	r := len(input)
	c := len(input[0]) // this only works because we know the chars are . and #
	g := make([][]bool, 0, 0)
	for _, s := range input {
		row := make([]bool, 0)
		chars := strings.Split(s, "")
		for _, c := range chars {
			v := (c == "#")
			row = append(row, v)
		}
		g = append(g, row)
	}

	t := trees{
		r:    r,
		c:    c,
		grid: g,
	}
	return t

}

func countTrees(t trees, right int, down int) int {
	row := 0
	col := 0
	count := 0

	for row < t.r {
		if t.get(row, col) {
			count++
		}
		row += down
		col += right
	}

	return count
}

func main() {
	a := getInput(false)
	c := countTrees(a, 3, 1)
	fmt.Println(c)

	slopes := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}

	counts := make([]int, 0)
	for _, s := range slopes {
		count := countTrees(a, s[0], s[1])
		counts = append(counts, count)
	}

	product := 1
	for _, s := range counts {
		product = product * s
	}
	fmt.Println(product)
}
