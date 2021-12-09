package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strings"
)

type entry struct {
	allDigits    []string
	outputDigits []string
	// char in this entry -> "real" char
	segmentMap map[string]string
}

func NewEntry(line string) entry {
	parts := strings.Split(line, " | ")
	all := strings.Split(parts[0], " ")
	output := strings.Split(parts[1], " ")
	return entry{
		allDigits:    all,
		outputDigits: output,
	}
}

/*
If we count all segments in the digits 0-9,
e, b, and f can be uniquely identified by counts (4, 6, and 9).
d and g both appear 7 times. And a and c appear 8 times.

We can distinquish d from g because we can distinquich the number 4
(because it is the only digit with 4 segments), and d is in 4 but g is not.

We can distinquish a from c because both a and c are in 7
(unqiuely identified as the digit with 3 segments), but a is not in
1 (uniquely identified as the digit with 2 segments)
*/
func (e *entry) computeSegmentMap() {
	charCounts := make(map[string]int)
	one := ""
	seven := ""
	four := ""
	for _, d := range e.allDigits {

		chars := strings.Split(d, "")
		for _, c := range chars {
			charCounts[c] = charCounts[c] + 1
		}

		if len(chars) == 2 {
			one = d
		} else if len(chars) == 3 {
			seven = d
		} else if len(chars) == 4 {
			four = d
		}
	}

	e.segmentMap = make(map[string]string)
	for c, num := range charCounts {
		if num == 4 {
			e.segmentMap[c] = "e"
		} else if num == 6 {
			e.segmentMap[c] = "b"
		} else if num == 9 {
			e.segmentMap[c] = "f"
		} else if num == 7 {
			/* We can distinquish d from g because we can distinquich the number 4
			(because it is the only digit with 4 segments), and d is in 4 but g is not.*/
			isD := strings.Contains(four, c)
			if isD {
				e.segmentMap[c] = "d"
			} else {
				e.segmentMap[c] = "g"
			}
		} else if num == 8 {
			/* We can distinquish a from c because both a and c are in 7 (unqiuely
			identified as the digit with 3 segments), but a is not in 1 (uniquely
			identified as the digit with 2 segments)*/

			isInSeven := strings.Contains(seven, c)
			isInOne := strings.Contains(one, c)

			if isInSeven && !isInOne {
				e.segmentMap[c] = "a"
			} else {
				e.segmentMap[c] = "c"
			}
		}
	}

}

var digitMap = map[int][]string{
	0: {"a", "b", "c", "e", "f", "g"},
	1: {"c", "f"},
	2: {"a", "c", "d", "e", "g"},
	3: {"a", "c", "d", "f", "g"},
	4: {"b", "c", "d", "f"},
	5: {"a", "b", "d", "f", "g"},
	6: {"a", "b", "d", "e", "f", "g"},
	7: {"a", "c", "f"},
	8: {"a", "b", "c", "d", "e", "f", "g"},
	9: {"a", "b", "c", "d", "f", "g"},
}

func (e entry) computeOutputDigit(s string) int {

	// segmentMap : this entry -> real
	realSegements := make([]string, 0)
	for _, c := range s {
		realSegements = append(realSegements, e.segmentMap[string(c)])
	}
	sort.Strings(realSegements)

	for val, segments := range digitMap {
		if slicesAreEqual(segments, realSegements) {
			return val
		}
	}

	panic("could not id output")
}

// ASSUMES SLICES ARE SORTED
func slicesAreEqual(s1 []string, s2 []string) bool {

	if len(s1) != len(s2) {
		return false
	}

	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			return false
		}
	}

	return true
}

func (e entry) computeOutputNumber() int {

	e.computeSegmentMap()

	sum := 0
	for i, o := range e.outputDigits {
		sum += int(math.Pow10(3-i)) * e.computeOutputDigit(o)
	}

	return sum
}

func getInput(fileName string) []entry {
	input := make([]entry, 0)

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		input = append(input, NewEntry(scanner.Text()))
	}

	return input
}

func main() {
	input := "input"
	part := 2

	entries := getInput(input + ".txt")

	if part == 1 {
		count := 0
		for _, o := range entries {
			for _, v := range o.outputDigits {
				l := len(v)
				if l == 2 || l == 4 || l == 3 || l == 7 {
					count++
				}
			}
		}
		fmt.Println(count)
	} else {
		outputSum := 0
		for _, e := range entries {
			outputSum += e.computeOutputNumber()
		}
		fmt.Println(outputSum)
	}
}
