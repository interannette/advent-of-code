package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func getInput(fileName string) []int {

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := scanner.Text()
	input := ConvertCSVLineToInts(line)
	return input
}

func ConvertToInts(numbersAsStrings []string) []int {
	numbers := make([]int, 0)
	for _, s := range numbersAsStrings {
		n, _ := strconv.Atoi(s)
		numbers = append(numbers, n)
	}
	return numbers
}
func ConvertCSVLineToInts(line string) []int {
	return ConvertToInts(strings.Split(line, ","))
}

func buildPosCount(crabs []int) (map[int]int, int) {
	posCounts := make(map[int]int)
	max := 0

	for _, c := range crabs {
		posCounts[c] = posCounts[c] + 1
		if c > max {
			max = c
		}
	}

	return posCounts, max
}

func computeCost1(i int, j int) int {
	if i < j {
		return j - i
	} else {
		return i - j
	}
}

func computeCost2(start int, goal int) int {
	distance := computeCost1(start, goal)
	return distance * (distance + 1) / 2
}

func main() {
	input := "input"
	part := 2

	crabs := getInput(input + ".txt")
	posCounts, max := buildPosCount(crabs)

	fuelByAlignmentPos := make(map[int]int)
	minFuel := max * computeCost2(0, len(crabs))
	for i := 0; i <= max; i++ {
		fuelCost := 0
		for pos, num := range posCounts {
			var cost int
			if part == 1 {
				cost = computeCost1(i, pos)
			} else {
				cost = computeCost2(i, pos)
			}
			fuelCost += cost * num
		}
		fuelByAlignmentPos[i] = fuelCost
		if fuelCost < minFuel {
			minFuel = fuelCost
		}
	}

	fmt.Println(minFuel)
}
