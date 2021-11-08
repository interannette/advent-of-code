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

	a := make([]int, 0)
	for scanner.Scan() {
		l := scanner.Text()
		if i, err := strconv.Atoi(l); err == nil {
			a = append(a, i)
		}

	}

	return a
}

func find_2(a []int, t int) (int, int) {
	for i := 0; i < len(a); i++ {
		c := t - a[i]
		for j := (i + 1); j < len(a); j++ {
			if a[j] == c {
				return a[i], a[j]
			}
		}
	}

	return -1, -1
}

func find_3(a []int, t int) (int, int, int) {
	for i := 0; i < len(a); i++ {
		c := t - a[i]
		x, y := find_2(a[1:], c)
		if x > 0 {
			return a[i], x, y
		}
	}
	return -1, -1, -1
}

func main() {
	a := getInput(false)

	i, j := find_2(a, 2020)
	fmt.Printf("%d product. Components %d, %d\n", i*j, i, j)

	i, j, k := find_3(a, 2020)
	fmt.Printf("%d product. Components %d, %d, %d\n", i*j*k, i, j, k)

}
