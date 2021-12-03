package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func getInput(fileName string) (map[int]int, int) {
	posCount := make(map[int]int)
	lines := 0

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		lines++
		chars := strings.Split(scanner.Text(), "")
		for i, c := range chars {
			if c == "1" {
				posCount[i] = posCount[i] + 1
			}
		}
	}

	return posCount, lines
}

// Just wrote my own. I don't want to deal with converting floats to use math.Pow
func powerOf2(p int) int {
	v := 1
	for i := 0; i < p; i++ {
		v = v * 2
	}
	return v
}

func computeDeltaGamma(posCounts map[int]int, numLines int) (delta int, gamma int) {
	h := numLines / 2       // "most common" = more than half
	p := len(posCounts) - 1 // how many digits do our numbers have

	for i, c := range posCounts {
		if c > h { // most common is 1, least common is 0
			gamma += powerOf2(p - i)
		} else { // most common is 0, least common is 1
			delta += powerOf2(p - i)
		}
	}

	return delta, gamma
}

func main() {
	input := "input"

	posCounts, numLines := getInput(input + ".txt")

	delta, gamma := computeDeltaGamma(posCounts, numLines)
	fmt.Printf("Delta %d. Gamma %d. Product %d.\n", delta, gamma, delta*gamma)

}
