package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"sort"
)

type line struct {
	chars []string
}

func NewLine(s string) line {
	return line {
		chars : strings.Split(s, ""),
	}
}

func (l line) corrupted() (bool, string) {
	openChunks := make([]string, 0)

	for _, c := range l.chars {
		if len(openChunks) == 0 {
			if isOpener(c) {
				openChunks = append(openChunks, c)
			} else {
				return true, c
			}
		} else if match(openChunks[len(openChunks) - 1], c) {
			// remove last open chunk
			openChunks = openChunks[:len(openChunks)-1]
		} else if isOpener(c) {
			// add c to open chunks list
			openChunks = append(openChunks, c)
		} else {
			return true, c
		}
	}

	return false, ""
}

func (l line) calculateCompletion() (bool, string) {
	openChunks := make([]string, 0)

	for _, c := range l.chars {
		if len(openChunks) == 0 {
			if isOpener(c) {
				openChunks = append(openChunks, c)
			} else {
				return false, ""
			}
		} else if match(openChunks[len(openChunks) - 1], c) {
			// remove last open chunk
			openChunks = openChunks[:len(openChunks)-1]
		} else if isOpener(c) {
			// add c to open chunks list
			openChunks = append(openChunks, c)
		} else {
			return false, ""
		}
	}

	completion := ""
	for i := len(openChunks)-1; i >= 0; i-- {
		match := getMatch(openChunks[i])
		completion = completion + match
	}

	return true, completion
}

func match(left string, right string) bool {
	if left == "(" && right == ")" {
		return true
	} else if left == "[" && right == "]" {
		return true
	} else if left == "{" && right == "}" {
		return true
	} else if left == "<" && right == ">" {
		return true
	} else {
		return false
	}
}

func isOpener(s string) bool {
	return s == "(" || s == "[" || s == "{" || s == "<"
}

func getMatch(open string) string {
	if open == "(" {
		return ")"
	} else if open == "[" {
		return "]"
	} else if open == "{" {
		return "}"
	} else if open == "<" {
		return ">"
	} else {
		return ""
	}
}

var charPoints = map[string]int {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

func getInput(fileName string) []line {

	input := make([]line, 0)

	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, NewLine(scanner.Text()))
	}

	return input
}

func doPart1(lines []line) {
	corruptedCounts := make(map[string]int)
	for _, l := range lines {
		corrupted, char := l.corrupted()
		if corrupted {
			corruptedCounts[char] = corruptedCounts[char] + 1
 		}
	}

	score := 0
	for k, v := range corruptedCounts {
		score += charPoints[k] * v
	}

	fmt.Println(score)
}

var completionPointValues = map[string]int {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

func scoreCompletionString(s string) int {
	//multiple by 5, add char score
	score := 0
	chars := strings.Split(s, "")
	for _, c := range chars {
		score = score * 5 + completionPointValues[c]
	}
	return score
}

func doPart2(lines []line) {
	corrections := make([]string, 0)
	for _, l := range lines {
		incomplete, completionString := l.calculateCompletion()
		if incomplete {
			corrections = append(corrections, completionString)
		}
	}
	
	scores := make([]int, 0)
	for _, completion := range corrections {
		scores =append(scores, scoreCompletionString(completion))
	}

	sort.Ints(scores)

	fmt.Println(scores[len(scores)/2])
}

func main() {
	file := "input"
	part := 2
	lines := getInput(file + ".txt")
	
	if part == 1 {
		doPart1(lines)
	} else {
		doPart2(lines)
	}
}