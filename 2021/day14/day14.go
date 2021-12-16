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
}

func NewInput(s string) input {
	t := strings.Split(s, "")
	return input {
		template: t,
		rules: make(map[pair]string),
	}
}

func (i *input) addRule(r rule) {
	i.rules[r.start] = r.insert
}

func (i *input) advance() {
	newTemplate := make([]string,0)
	for j := 0; j < len(i.template)-1; j++ {
		
		first := i.template[j]
		second := i.template[j+1]
		
		newTemplate = append(newTemplate, first)

		r, exists := i.rules[NewPair(first, second)]
		if exists {
			newTemplate = append(newTemplate, r)
		}
		
	}
	newTemplate = append(newTemplate, i.template[len(i.template)-1])

	i.template = newTemplate
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
	file := "sample"
	steps := 10

	p := getInput(file + ".txt")

	for i := 1; i <= steps; i++ {
		p.advance()
		fmt.Printf("Step %d. Template length %d\n", i, len(p.template))
	}

	countMap := make(map[string]int)
	for _, s := range p.template {
		countMap[s] = countMap[s] + 1
	}

	maxCount := 0
	minCount := len(p.template) + 1
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