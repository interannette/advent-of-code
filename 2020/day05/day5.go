package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
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

func computeSeatIds(seats [][]int64) []int64 {
	seatIds := make([]int64, 0)
	for _, s := range seats {
		seatIds = append(seatIds, s[0]*8+s[1])
	}
	return seatIds
}

func computeSeatList(input []string) [][]int64 {
	seats := make([][]int64, 0)
	for _, s := range input {
		r, c := computeSeat(s)
		seats = append(seats, []int64{r, c})
	}
	return seats
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

func findMissingSeat(seatMap [][]bool) (row int, col int) {

	for i := 1; i < 127; i++ {
		row := seatMap[i]
		for j := 0; j < 8; j++ {
			if !row[j] {
				front := seatMap[i-1][j]
				back := seatMap[i+1][j]
				if front && back {
					return i, j
				}
			}
		}
	}

	return -1, -1
}

func buildSeatMap(seats [][]int64) [][]bool {
	seatMap := make([][]bool, 128)
	for i := 0; i <= 127; i++ {
		seatMap[i] = make([]bool, 8)
	}

	for _, seat := range seats {
		seatMap[seat[0]][seat[1]] = true
	}

	return seatMap
}

func printSeatMap(seatMap [][]bool) {
	for i, row := range seatMap {
		fmt.Printf("Row %d:\t", i)
		fmt.Println(row)
	}
}

func main() {
	input := getInput(false)

	seats := computeSeatList(input)
	ids := computeSeatIds(seats)
	max := findMax(ids)
	fmt.Println(max)

	seatMap := buildSeatMap(seats)
	r, c := findMissingSeat(seatMap)
	fmt.Printf("Row %d, col %d. Id %d\n", r, c, r*8+c)
}
