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

type policy struct {
	min, max int
	c        string
}

type entry struct {
	p        policy
	password string
}

var lineRegex = regexp.MustCompile(`(?P<min>\d+)-(?P<max>\d+) (?P<c>\w): (?P<p>\w+)`)

func parse(s string) entry {

	match := lineRegex.FindStringSubmatch(s)
	result := make(map[string]string)

	for i, name := range lineRegex.SubexpNames() {
		if i != 0 && name != "" {
			result[name] = match[i]
		}
	}

	min, _ := strconv.Atoi(result["min"])
	max, _ := strconv.Atoi(result["max"])

	p := policy{
		min: min,
		max: max,
		c:   result["c"],
	}
	e := entry{
		p:        p,
		password: result["p"],
	}
	return e
}

func getInput(sample bool) []entry {
	strings := make([]string, 0)
	if sample {
		strings = append(strings, "1-3 a: abcde")
		strings = append(strings, "1-3 b: cdefg")
		strings = append(strings, "2-9 c: ccccccccc")
	} else {
		file, err := os.Open("input.txt")
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			strings = append(strings, scanner.Text())
		}
	}

	entries := make([]entry, 0)
	for _, s := range strings {
		e := parse(s)
		entries = append(entries, e)
	}

	return entries

}

func isValid(e entry) bool {
	c := strings.Count(e.password, e.p.c)
	if e.p.min <= c && e.p.max >= c {
		return true
	} else {
		return false
	}
}

func countValid(entries []entry) int {
	i := 0
	for _, e := range entries {
		if isValid(e) {
			i++
		}
	}
	return i
}

func main() {
	a := getInput(false)

	c := countValid(a)

	fmt.Printf("Found %d valid entries\n", c)

}
