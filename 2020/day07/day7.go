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

var ruleRegex = regexp.MustCompile(`^(?P<color>[a-z0-9 ]+) bags contain (?P<condition>[a-z0-9 ,]+).$`)

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
		if len(conditions) > 1 {
			fmt.Println("Found rule with multiple conditions")
		}
		for _, c := range conditionSubstrings {
			condition := parseCondition(c)
			conditions = append(conditions, condition)
		}
	}

	if len(conditions) > 1 {
		fmt.Println("Found rule with multiple conditions")
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

func buildMap(rules []rule) map[string][]string {

	colorMap := make(map[string][]string)

	for _, r := range rules {
		//fmt.Println("Rule: ")
		//fmt.Println(r)
		for _, c := range r.conditions {
			cur := colorMap[c.color]
			cur = append(cur, r.color)
			colorMap[c.color] = cur
			//fmt.Println(colorMap[c.color])
		}
	}

	return colorMap
}

func findContainingColors(colorMap map[string][]string, color string, containingColors map[string]bool) map[string]bool {

	nextColors := colorMap[color]

	if len(nextColors) == 0 {
		return containingColors
	}

	for _, c := range nextColors {
		containingColors[c] = true
		containingColors = findContainingColors(colorMap, c, containingColors)
	}

	return containingColors
}

func main() {
	input := getInput(false)
	rules := parseRules(input)
	colorsMap := buildMap(rules)
	containerColors := findContainingColors(colorsMap, "shiny gold", make(map[string]bool))
	fmt.Println(len(containerColors))
}
