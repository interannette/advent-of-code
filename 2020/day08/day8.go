package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

type instruction struct {
	operation string
	argument  int
	visited   bool
}

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

var instructionRegex = regexp.MustCompile(`^(?P<op>[a-z]{3}) (?P<arg>[+\-]{1}\d+)$`)

func parseInstruction(line string) instruction {
	match := instructionRegex.FindStringSubmatch(line)
	if len(match) > 0 {
		op := match[1]
		arg, _ := strconv.Atoi(match[2])

		return instruction{
			operation: op,
			argument:  arg,
			visited:   false,
		}

	} else {
		panic("Unable to parse line " + line)
	}
}

func runInstructions(program []instruction) int {
	val := 0
	i := 0

	for {
		cur := program[i]
		fmt.Printf("Executing %+v\n", cur)

		if cur.visited == true {
			return val
		}

		program[i].visited = true

		if cur.operation == "nop" {
			i++
		} else if cur.operation == "acc" {
			val += cur.argument
			i++
		} else {
			i = i + cur.argument
		}
	}
}

func main() {
	instructions := getInput("input.txt")
	val := runInstructions(instructions)
	fmt.Println(val)
}
