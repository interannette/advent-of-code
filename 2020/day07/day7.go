package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type condition struct {
	n     int
	color string
}

type rule struct {
	color      string
	conditions []condition
}

func getInput(sample bool) []string {

	input := make([]string, 0)
	if sample {
		input = append(input, "light red bags contain 1 bright white bag, 2 muted yellow bags.")
		input = append(input, "dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
		input = append(input, "bright white bags contain 1 shiny gold bag.")
		input = append(input, "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
		input = append(input, "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
		input = append(input, "dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
		input = append(input, "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
		input = append(input, "faded blue bags contain no other bags.")
		input = append(input, "dotted black bags contain no other bags.")
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

func parseRules(input []string) []rule {
	rules := make([]rule, 0)

	for _, s := range input {
		rules = append(rules, parseRule(s))
	}

	return rules
}

var ruleRegex = regexp.MustCompile(`^(?P<color>[a-z0-9 ]+) bags contain (?P<condition>[a-z0-9 ]+).*`)

//input = append(input, "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
//input = append(input, "faded blue bags contain no other bags.")
//input = append(input, "bright white bags contain 1 shiny gold bag.")
func parseRule(s string) rule {
	match := ruleRegex.FindStringSubmatch(s)

	if len(match) == 0 {
		fmt.Printf("Could not parse rule from %s\n", s)
	}

	color := match[1]
	conidtionString := match[2]
	conditions := make([]condition, 0)
	if conidtionString != "no other bags" {
		conditionSubstrings := strings.Split(conidtionString, ",")
		for _, c := range conditionSubstrings {
			condition := parseCondition(c)
			conditions = append(conditions, condition)
		}
	}

	r := rule{
		color:      color,
		conditions: conditions,
	}

	return r
}

var conditionRegex = regexp.MustCompile(`(?P<num>\d+) (?P<color>[a-z0-9 ]+) bag`)

func parseCondition(s string) condition {

	match := conditionRegex.FindStringSubmatch(s)

	if len(match) == 0 {
		fmt.Printf("Could not parse condition from %s\n", s)
	}

	num, _ := strconv.Atoi(match[1])
	color := match[2]

	c := condition{
		n:     num,
		color: color,
	}
	return c
}

func main() {
	input := getInput(true)
	rules := parseRules(input)
	fmt.Println(rules)
}
