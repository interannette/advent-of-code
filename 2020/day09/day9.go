package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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

func isComposable(list []int, current int, lookback int) bool {
	v := list[current]
	for i := current - lookback; i < current; i++ {
		needed := v - list[i]
		for j := i + 1; j < current; j++ {
			if list[j] == needed {
				return true
			}
		}
	}
	return false
}

func findContiguousSum(input []int, invalid int) (int, int) {
	for i := 0; i < len(input); i++ {
		sum := input[i]
		for j := i + 1; j < len(input); j++ {
			sum += input[j]
			if sum == invalid {
				return i, j
			} else if sum > invalid {
				break
			}
		}
	}
	return -1, -1
}

func findMinMax(input []int, start int, end int) (int, int) {
	min := input[start]
	max := input[start]
	for i := start; i <= end; i++ {
		if input[i] < min {
			min = input[i]
		}

		if input[i] > max {
			max = input[i]
		}
	}

	return min, max
}

func main() {
	input := getInput("input.txt")

	preamble := 25
	invalid := 0
	for i := preamble; i < len(input); i++ {
		if !isComposable(input, i, preamble) {
			invalid = input[i]
			break
		}
	}
	fmt.Printf("Invalid number %d\n", invalid)

	start, end := findContiguousSum(input, invalid)
	fmt.Printf("Start %d (%d), end %d (%d).\n", start, input[start], end, input[end])

	min, max := findMinMax(input, start, end)
	fmt.Printf("Min %d, max %d. Sum %d\n", min, max, min+max)

}
