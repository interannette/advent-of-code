package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	// "regexp"
)

func getInput(sample bool) []string {

	input := make([]string, 0)
	if sample {
		input = append(input, "FBFBBFFRLR")
		input = append(input, "BFFFBBFRRR")
		input = append(input, "FFFBBBFRRR")
		input = append(input, "BBFFBBFRLL")
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

	return input
}

func computeSeatIds(input []string) []int64 {
	seats := make([]int64, 0)
	for _, s := range input {
		seats = append(seats, computeSeatId(s))
	}
	return seats
}

func computeSeatId(s string) int64 {
	r, c := computeSeat(s)
	return r*8 + c
}

func computeSeat(s string) (row int64, col int64) {
	return computeRow(s[:7]), computeCol(s[7:])
}

// F = 0
// B = 1
func computeRow(s string) int64 {
	s = strings.ReplaceAll(s, "F", "0")
	s = strings.ReplaceAll(s, "B", "1")
	i, _ := strconv.ParseInt(s, 2, 0)
	return i
}

// L = 0
// R = 1
func computeCol(s string) int64 {
	s = strings.ReplaceAll(s, "L", "0")
	s = strings.ReplaceAll(s, "R", "1")
	i, _ := strconv.ParseInt(s, 2, 0)
	return i
}

func findMax(l []int64) int64 {
	max := int64(0)
	for _, v := range l {
		if v > max {
			max = v
		}
	}
	return max
}

func main() {
	s := getInput(false)
	ids := computeSeatIds(s)
	max := findMax(ids)

	fmt.Println(max)
}
