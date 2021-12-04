package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func getInput(fileName string) []string {
	input := make([]string, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	return input
}

func buildPosCount(input []string) []int {

	posCount := make([]int, len(input[0]))

	for _, line := range input {
		chars := strings.Split(line, "")
		for i, c := range chars {
			if c == "1" {
				posCount[i] = posCount[i] + 1
			}
		}
	}

	return posCount
}

// Just wrote my own. I don't want to deal with converting floats to use math.Pow
func powerOf2(p int) int64 {
	v := int64(1)
	for i := 0; i < p; i++ {
		v = v * 2
	}
	return v
}

func computeDeltaGamma(posCounts []int, numLines int) (delta int64, gamma int64) {
	h := numLines / 2       // "most common" = more than half
	p := len(posCounts) - 1 // how many digits do our numbers have

	for i, c := range posCounts {
		if c > h { // most common is 1, least common is 0
			gamma += powerOf2(p - i)
		} else { // most common is 0, least common is 1
			delta += powerOf2(p - i)
		}
	}

	return delta, gamma
}

func convertLines(lines []string) []int64 {
	nums := make([]int64, 0)
	for _, l := range lines {
		i, _ := strconv.ParseInt(l, 2, 0)
		nums = append(nums, i)
	}
	return nums
}

//Doing it with bit math so I learn bit math.
func computeLifeSupportRating(nums []int64, maxPower int, fn compareCounts) int64 {

	for power := maxPower; power >= 0; power-- {

		currentPowerOf2 := powerOf2(power)

		zeros := make([]int64, 0)
		ones := make([]int64, 0)

		for _, n := range nums {
			// will be either currentPowerOf2 or 0
			a := n & currentPowerOf2
			if a == 0 {
				zeros = append(zeros, n)
			} else {
				ones = append(ones, n)
			}
		}

		winner := fn(len(ones), len(zeros))
		if winner == 1 {
			nums = ones
		} else {
			nums = zeros
		}

		if len(nums) <= 1 {
			break
		}

	}

	if len(nums) > 1 {
		panic("could not find single number for rating")
	} else if len(nums) == 0 {
		panic("removed all numbers for rating")
	}

	return nums[0]
}

type compareCounts func(int, int) int

/*
To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
and keep only numbers with that bit in that position.
If 0 and 1 are equally common, keep values with a 1 in the position being considered.
*/
func oxygenCompare(onesCount int, zerosCount int) int {
	if onesCount >= zerosCount {
		return 1
	} else {
		return 0
	}
}

/*
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
and keep only numbers with that bit in that position.
If 0 and 1 are equally common, keep values with a 0 in the position being considered.
*/
func co2Compare(onesCount int, zerosCount int) int {
	if zerosCount <= onesCount {
		return 0
	} else {
		return 1
	}
}

func main() {
	input := "input"
	part := 2

	lines := getInput(input + ".txt")

	if part == 1 {
		posCounts := buildPosCount(lines)
		delta, gamma := computeDeltaGamma(posCounts, len(lines))
		fmt.Printf("Delta %d. Gamma %d. Product %d.\n", delta, gamma, delta*gamma)
	} else {
		nums := convertLines(lines)
		maxPowerOf2 := len(lines[0]) - 1
		oxygen := computeLifeSupportRating(nums, maxPowerOf2, oxygenCompare)
		co2 := computeLifeSupportRating(nums, maxPowerOf2, co2Compare)
		fmt.Printf("Oxygen rating %d. CO2 rating %d. Product %d\n", oxygen, co2, oxygen*co2)
	}
}
