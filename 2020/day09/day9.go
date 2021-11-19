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

func main() {
	input := getInput("input.txt")

	preamble := 25
	for i := preamble; i < len(input); i++ {
		if !isComposable(input, i, preamble) {
			fmt.Println(input[i])
		}
	}
}
