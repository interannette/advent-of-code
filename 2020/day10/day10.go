package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func getInput(fileName string) []int {
	input := make([]int, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		i, _ := strconv.Atoi(line)
		input = append(input, i)
	}

	return input
}

func countDifferences(input []int) (int, int) {
	ones := 0
	threes := 1 // always count last one as 3

	previous := 0 // wall counts as 0
	for _, c := range input {
		diff := c - previous
		if diff == 1 {
			ones++
		} else if diff == 3 {
			threes++
		} else {
			panic("Unexpected diff")
		}
		previous = c
	}

	return ones, threes
}

func main() {
	input := getInput("input.txt")

	sort.Slice(input, func(i, j int) bool {
		return input[i] < input[j]
	})

	ones, threes := countDifferences(input)

	fmt.Printf("Number of ones %d. Number of threes %d. Product %d\n", ones, threes, ones*threes)

}
