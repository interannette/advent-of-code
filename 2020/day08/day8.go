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

func runInstructions(program []instruction) (int, bool) {
	val := 0
	i := 0

	for i < len(program) {
		cur := program[i]
		fmt.Printf("Executing %+v\n", cur)

		if cur.visited == true {
			return val, true
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

	return val, false
}

func reset(program []instruction) {
	for i := 0; i < len(program); i++ {
		program[i].visited = false
	}
}

func fixProgram(program []instruction) int {

	for i := 0; i < len(program); i++ {
		cur := program[i]
		fmt.Printf("Testing line %d: %+v\n", i, cur)
		if cur.operation != "acc" {

			var newOp string
			if cur.operation == "jmp" {
				newOp = "nop"
			} else {
				newOp = "jmp"
			}

			update := instruction{
				operation: newOp,
				argument:  cur.argument,
				visited:   false,
			}
			program[i] = update

			val, loop := runInstructions(program)
			if !loop {
				return val
			} else {
				fmt.Println("Still loops")
			}

			program[i] = cur
			reset(program)
		}
	}

	return -1
}

func main() {
	instructions := getInput("input.txt")
	val, loop := runInstructions(instructions)
	fmt.Printf("Result: %d. Infinite loop: %v\n", val, loop)

	val = fixProgram(instructions)
	fmt.Printf("Fixed program returns %d", val)
}
