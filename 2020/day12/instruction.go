package main

import (
	"fmt"
	"regexp"
	"strconv"
)

type instruction struct {
	v int
	a action
}

func (i instruction) String() string {
	return fmt.Sprintf("%s%d", i.a, i.v)
}

var instructionRegex = regexp.MustCompile(`^(?P<action>\w{1})(?P<value>\d+)$`)

func parseInstruction(s string) instruction {
	match := instructionRegex.FindStringSubmatch(s)

	if len(match) == 0 {
		fmt.Printf("Could not parse instruction from %s\n", s)
	}

	a := parseAction(match[1])
	v, _ := strconv.Atoi(match[2])

	i := instruction{
		a: a,
		v: v,
	}

	return i
}
