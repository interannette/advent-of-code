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

func getInput(sample int) []string {

	input := make([]string, 0)
	if sample == 1 {
		input = append(input, "light red bags contain 1 bright white bag, 2 muted yellow bags.")
		input = append(input, "dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
		input = append(input, "bright white bags contain 1 shiny gold bag.")
		input = append(input, "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
		input = append(input, "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
		input = append(input, "dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
		input = append(input, "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
		input = append(input, "faded blue bags contain no other bags.")
		input = append(input, "dotted black bags contain no other bags.")
	} else if sample == 2 {
		input = append(input, "shiny gold bags contain 2 dark red bags.")
		input = append(input, "dark red bags contain 2 dark orange bags.")
		input = append(input, "dark orange bags contain 2 dark yellow bags.")
		input = append(input, "dark yellow bags contain 2 dark green bags.")
		input = append(input, "dark green bags contain 2 dark blue bags.")
		input = append(input, "dark blue bags contain 2 dark violet bags.")
		input = append(input, "dark violet bags contain no other bags.")
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

func buildConditionMap(rules []rule) map[string][]string {

	colorMap := make(map[string][]string)

	for _, r := range rules {
		for _, c := range r.conditions {
			cur := colorMap[c.color]
			cur = append(cur, r.color)
			colorMap[c.color] = cur
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

func buildRulesMap(rules []rule) map[string]rule {
	rulesMap := make(map[string]rule)

	for _, r := range rules {
		rulesMap[r.color] = r
	}

	return rulesMap
}

func findNumContained(rulesMap map[string]rule, color string) int {
	r := rulesMap[color]

	if len(r.conditions) == 0 {
		return 0
	}

	count := 0
	for _, c := range r.conditions {
		count += c.n * (1 + findNumContained(rulesMap, c.color))
	}
	return count
}

func main() {

	sample := 0
	part := 2

	input := getInput(sample)
	rules := parseRules(input)

	if part == 1 {
		colorsMap := buildConditionMap(rules)
		containerColors := findContainingColors(colorsMap, "shiny gold", make(map[string]bool))
		fmt.Println(len(containerColors))
	} else {
		rulesMap := buildRulesMap(rules)
		numberContained := findNumContained(rulesMap, "shiny gold")
		fmt.Println(numberContained)
	}
}
