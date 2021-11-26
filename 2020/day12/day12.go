package main

import (
	"bufio"
	"log"
	"os"
)

func getInput(fileName string) []instruction {
	input := make([]instruction, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, parseInstruction(scanner.Text()))
	}

	return input
}

func main() {
	input := "input"
	part := 2

	instructions := getInput(input + ".txt")

	if part == 1 {
		doPart1(instructions)
	} else {
		doPart2(instructions)
	}

}
