package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func getInput(fileName string) []line {
	input := make([]line, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, NewLine(scanner.Text()))
	}

	return input
}

func main() {
	input := "input"
	part := 2

	lines := getInput(input + ".txt")

	maxX := 0
	maxY := 0

	nonDiagonalLines := make([]line, 0)
	for _, l := range lines {
		if l.IsNotDiagonal() {
			nonDiagonalLines = append(nonDiagonalLines, l)
		}

		if l.MaxX() > maxX {
			maxX = l.MaxX()
		}
		if l.MaxY() > maxY {
			maxY = l.MaxY()
		}
	}
	if part == 1 {
		lines = nonDiagonalLines
	}
	

	m := NewMap(maxX, maxY)
	for _, l := range lines {
		for _, p := range l.AllPos() {
			m = m.MarkPos(p.x, p.y)
		}	
	}

	fmt.Println(m.SumMultiples())

}