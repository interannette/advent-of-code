package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type command struct {
	instruction string
	amount      int
}

type position struct {
	horiztonal int
	depth      int
	aim        int
}

func parseCommand(line string) command {
	parts := strings.Split(line, " ")

	a, _ := strconv.Atoi(parts[1])

	return command{
		instruction: parts[0],
		amount:      a,
	}
}

func getInput(fileName string) []command {
	input := make([]command, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, parseCommand(scanner.Text()))
	}

	return input
}

func runPart1Command(pos position, c command) position {
	if c.instruction == "forward" {
		pos.horiztonal += c.amount
	} else if c.instruction == "up" {
		pos.depth -= c.amount
	} else if c.instruction == "down" {
		pos.depth += c.amount
	} else {
		panic("unknown command")
	}
	return pos
}

func runPart2Command(pos position, c command) position {
	if c.instruction == "forward" {
		pos.horiztonal += c.amount
		pos.depth += pos.aim * c.amount
	} else if c.instruction == "up" {
		pos.aim -= c.amount
	} else if c.instruction == "down" {
		pos.aim += c.amount
	} else {
		panic("unknown command")
	}
	return pos
}

func main() {
	input := "input"
	part := 2

	commands := getInput(input + ".txt")

	pos := position{}

	for _, c := range commands {
		if part == 1 {
			pos = runPart1Command(pos, c)
		} else {
			pos = runPart2Command(pos, c)
		}
	}

	fmt.Printf("Final position %d, %d. Product %d\n", pos.horiztonal, pos.depth, pos.depth*pos.horiztonal)
}
