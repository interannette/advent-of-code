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
	threes := 0

	for i := 1; i < len(input); i++ {
		diff := input[i] - input[i-1]
		if diff == 1 {
			ones++
		} else if diff == 3 {
			threes++
		} else {
			panic("Unexpected diff")
		}
	}

	return ones, threes
}

// number of ways to get to the end from step a (with options x, y, z)
// 		sum of ways to get to the end from x +
//				ways to get to the end from y +
//				ways to get to the end from z
func countOptions(input []int, i int, computed map[int]int) int {

	if i == len(input)-1 {
		return 1
	}

	options := 0
	for j := 1; j <= 3 && i+j < len(input); j++ {
		diff := input[i+j] - input[i]
		if diff >= 1 && diff <= 3 {

			val, exists := computed[input[i+j]]
			if exists {
				options += val
			} else {
				options += countOptions(input, i+j, computed)
			}
		}
	}
	computed[input[i]] = options
	return options
}

func main() {

	data := "input.txt"
	part := 2

	input := getInput(data)
	input = append(input, 0)
	sort.Slice(input, func(i, j int) bool {
		return input[i] < input[j]
	})
	input = append(input, input[len(input)-1]+3)

	if part == 1 {
		ones, threes := countDifferences(input)
		fmt.Printf("Number of ones %d. Number of threes %d. Product %d\n", ones, threes, ones*threes)
	}

	if part == 2 {
		arangments := countOptions(input, 0, make(map[int]int))
		fmt.Printf("Possible arangments %d\n", arangments)
	}
}
