package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getInput(sample bool) []int {
	if sample {
		return []int{1721, 979, 366, 299, 675, 1456}
	}

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	a := make([]int, 100)
	for scanner.Scan() {
		l := scanner.Text()
		if i, err := strconv.Atoi(l); err == nil {
			a = append(a, i)
		}

	}

	return a
}

func find(a []int) (int, int) {
	for i := 0; i < len(a); i++ {
		c := 2020 - a[i]
		for j := 1; j < len(a); j++ {
			if a[j] == c {
				return a[i], a[j]
			}
		}
	}
	return 0, 0
}

func main() {
	a := getInput(false)
	i, j := find(a)
	fmt.Printf("%d product. Components %d, %d", i*j, i, j)
}
