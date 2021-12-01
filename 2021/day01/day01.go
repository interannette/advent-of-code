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
		i, _ := strconv.Atoi(scanner.Text())
		input = append(input, i)
	}

	return input
}

func countIncreases(depths []int) int {
	increases := 0
	previous := depths[0]
	for i := 1; i < len(depths); i++ {
		if depths[i] > previous {
			increases++
		}
		previous = depths[i]
	}
	return increases
}

func countWindowIncreases(depths []int) int {
	increases := 0

	previous := depths[0] + depths[1] + depths[2]
	for i := 1; i < len(depths)-2; i++ {
		current := depths[i] + depths[i+1] + depths[i+2]
		if current > previous {
			increases++
		}
		previous = current
	}

	return increases
}

func main() {
	input := "input"
	part := 2

	depths := getInput(input + ".txt")

	if part == 1 {
		fmt.Println(countIncreases(depths))
	} else {
		fmt.Println(countWindowIncreases(depths))
	}

}
