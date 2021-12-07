package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
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

func advanceFish(f int) (int, bool) {
	
	spawn := false

	if f == 0 {
		f = 6
		spawn = true
	} else {
		f = f-1
	}

	return f, spawn
}

func doSlowWay(fish []int, rounds int) {
	for i := 0; i < rounds; i++ {
		newFish := make([]int, len(fish))
		for j := 0; j < len(fish); j++ {
			value, spawn := advanceFish(fish[j])
			newFish[j] = value
			if spawn {
				newFish = append(newFish, 8)
			}
		}
		fish = newFish
	}

	fmt.Printf("Number of fish after %d rounds: %d\n", rounds, len(fish))
}

func doFastWay(fish []int, rounds int) {
	fishCounts := make(map[int]uint64)

	for _, f := range fish {
		fishCounts[f] = fishCounts[f] + 1
	}

	for r := 0; r < rounds; r++ {
		newCounts := make(map[int]uint64)
		for i:=0; i <= 8; i++ {
			numberAtDay := fishCounts[i]
			newDay, spawn := advanceFish(i)
			newCounts[newDay] = newCounts[newDay] + numberAtDay
			if spawn {
				newCounts[8] = newCounts[8] + numberAtDay
			}
		}
		fishCounts = newCounts
	}

	sum := uint64(0)
	for _, f := range fishCounts {
		sum += f
	}
	fmt.Printf("Number of fish after %d rounds %d\n", rounds, sum)
	
}

func main() {
	input := "input"
	part := 2

	fish := getInput(input + ".txt")

	if part == 1 {
		doSlowWay(fish, 80)
	} else {
		doFastWay(fish, 256)
	}

}