package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func getInput(sample bool) [][]string {

	input := make([]string, 0)
	if sample {
		input = append(input, "abc")
		input = append(input, "")
		input = append(input, "a")
		input = append(input, "b")
		input = append(input, "c")
		input = append(input, "")
		input = append(input, "ab")
		input = append(input, "ac")
		input = append(input, "")
		input = append(input, "a")
		input = append(input, "a")
		input = append(input, "a")
		input = append(input, "a")
		input = append(input, "")
		input = append(input, "b")
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

	groups := make([][]string, 0)
	currentGroup := make([]string, 0)
	for _, s := range input {
		if s == "" {
			groups = append(groups, currentGroup)
			currentGroup = make([]string, 0)
		} else {
			currentGroup = append(currentGroup, s)
		}
	}
	groups = append(groups, currentGroup)

	return groups
}

//a-z = 97, 122
func computeCount(group []string) int {
	questions := make([]bool, 26)

	for _, s := range group {
		runes := []rune(s)
		for _, c := range runes {
			questions[int(c)-97] = true
		}
	}

	count := 0
	for _, q := range questions {
		if q {
			count++
		}
	}

	return count
}

func main() {
	input := getInput(false)
	sum := 0
	for _, group := range input {
		count := computeCount(group)
		sum += count
	}
	fmt.Println(sum)
}
