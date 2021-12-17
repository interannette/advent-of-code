package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

type pair struct {
	first string
	second string
}

func NewPair(f string, s string) pair {
	return pair {
		first: f,
		second:s,
	}
}

type rule struct {
	start pair
	insert string
}

// CH -> B
var ruleRegex = regexp.MustCompile("^(\\w{1})(\\w{1}) -> (\\w{1})$")
func ParseRule(s string) rule {
	match := ruleRegex.FindStringSubmatch(s)
	
	if len(match) < 4 {
		panic("could not parse rule")
	} 

	return rule {
		start: NewPair(match[1],match[2]),
		insert:match[3],
	}
}

type input struct {
	template []string
	rules map[pair]string
	polymerCounts map[pair]int
}

func NewInput(s string) input {
	t := strings.Split(s, "")
	counts := make(map[pair]int)
	for i:=0; i < len(t) - 1; i++ {
		p := NewPair(t[i], t[i+1])
		counts[p] = counts[p] + 1
	}
	return input {
		template: t,
		rules: make(map[pair]string),
		polymerCounts:counts,
	}
}

func (i *input) addRule(r rule) {
	i.rules[r.start] = r.insert
}

func (i *input) advance() {
	
	newCounts := make(map[pair]int)

	for k, v := range i.polymerCounts {
		
		insert, exists := i.rules[k]

		if exists {

			p1 := NewPair(k.first, insert)
			p2 := NewPair(insert, k.second)
		
			newCounts[p1] = newCounts[p1] + v
			newCounts[p2] = newCounts[p2] + v

		} else {
			fmt.Printf("No matching rule for %v", k)
		}
	}

	i.polymerCounts = newCounts
}

func (i input) lengthOfPolymer() int {
	length := 1 // we don't have the last char in the map
	for _, v := range i.polymerCounts {
		length += v
	}
	return length
}

func getInput(fileName string) input {


	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	input := NewInput(scanner.Text())
	scanner.Scan()

	for scanner.Scan() {
		input.addRule(ParseRule(scanner.Text()))
	}

	return input
}

func main() {
	file := "input"
	steps := 40

	input := getInput(file + ".txt")

	for i := 1; i <= steps; i++ {
		input.advance()
	}

	countMap := make(map[string]int)
	for p, c := range input.polymerCounts {
		countMap[p.first] = countMap[p.first] + c
	}
	lastChar := input.template[len(input.template) - 1]
	countMap[lastChar] = countMap[lastChar] + 1

	maxCount := 0
	minCount := input.lengthOfPolymer() + 1
	for _, v := range countMap {
		if v < minCount {
			minCount = v
		}
		if v > maxCount {
			maxCount = v
		}
	}

	fmt.Println(maxCount-minCount)

}