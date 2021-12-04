package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func getInput(fileName string) ([]int, []board) {

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	draws := convertToInts(strings.Split(scanner.Text(), ","))

	// skip blank line between number and boards
	scanner.Scan()
	scanner.Text()

	boards := make([]board, 0)
	linesForBoard := make([]string, 0)
	for scanner.Scan() {
		if len(linesForBoard) == 5 {
			boards = append(boards, NewBoard(linesForBoard))
			linesForBoard = make([]string, 0)
			scanner.Text()
		} else {
			linesForBoard = append(linesForBoard, scanner.Text())
		}
	}
	boards = append(boards, NewBoard(linesForBoard))

	return draws, boards
}

func convertToInts(numbersAsStrings []string) []int {
	numbers := make([]int, 0)
	for _, s := range numbersAsStrings {
		n, _ := strconv.Atoi(s)
		numbers = append(numbers, n)
	}
	return numbers
}

func main() {
	input := "input"
	part := 2

	draws, boards := getInput(input + ".txt")
	
	if part == 1 {
		done := false
		for _, d := range draws {
			for i, b := range boards {
				newB, win := b.MarkNumber(d)
				if win {
					s := newB.SumUnmarked()
					fmt.Printf("Winner at draw %d. Sum unmarked %d. Product %d.\n", d, s, d*s)
					done = true
					break
				} else {
					boards[i] = newB
				}
			}
			if done {
				break
			}
		}
	} else {
		for _, d := range draws {
			losers := make([]board, 0)
			for _, b := range boards {
				newB, win := b.MarkNumber(d)
				if !win {
					losers = append(losers, newB)
				}
			}

			// every board has won, we found the last one.
			if len(losers) == 0 {
				last := boards[len(boards)-1]
				s := last.SumUnmarked()
				fmt.Printf("Last winner at draw %d. Sum unmarked %d. Product %d.\n", d, s, d*s)
				break
			} else { // only contiue the next draw the boards that have not won
				boards = losers
			}
		}
	}
}
