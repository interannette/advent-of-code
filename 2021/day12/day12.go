package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type graph struct {
	edges map[string][]string
}

func (g *graph) addEdge(n1 string, n2 string) {
	destinations, exits := g.edges[n1]
	if exits {
		destinations = append(destinations, n2)
	} else {
		destinations = []string{n2}
	}
	g.edges[n1] = destinations

	destinations, exits = g.edges[n2]
	if exits {
		destinations = append(destinations, n1)
	} else {
		destinations = []string{n1}
	}
	g.edges[n2] = destinations
}

func NewGraph() graph {
	return graph {
		edges: make(map[string][]string),
	}
}

func (g graph) findAllPaths(v validation) []path {
	done := make([]path, 0)
	p := NewPath("start", v)
	
	partialPaths := NewQueue(p)
	for partialPaths.hasMore() {
		p = partialPaths.pop()
		morePaths, finished := g.extendPath(p)
		if finished {
			done = append(done, p)
		} else if len(morePaths) > 0 {
			partialPaths.pushSlice(morePaths)
		}
	}

	return done
}

func (g graph) extendPath(p path) ([]path, bool) {
	if p.lastNode() == "end" {
		return nil, true
	}
	
	extended := make([]path, 0)
	children := g.edges[p.lastNode()]
	for _, child := range children {
		newPath, valid := p.addStep(child)
		if valid {
			extended = append(extended, newPath)
		} else {
		}
	}
	return extended, false

}

type queue struct {
	paths []path
	current int
}

func NewQueue(p path) queue {
	return queue {
		paths : []path{p},
		current: 0,
	}
}

func (q *queue) push(p path) {
	q.paths = append(q.paths, p)
}

func (q *queue) pushSlice(p []path) {
	q.paths = append(q.paths, p...)
}

func (q *queue) pop() path {
	q.current++
	return q.paths[q.current-1]
}

func (q queue) hasMore() bool {
	return q.current < len(q.paths)
}

type path struct {
	steps []string
	validator validation
}

func NewPath(n string, v validation) path {
	s := []string{n}
	return path {
		steps : s,
		validator: v,
	}
}

func (p path) lastNode() string {
	return p.steps[len(p.steps)-1]
}

func (p path) addStep(node string) (path, bool) {

	valid := p.validator(p, node)
	if !valid {
		return p, false
	}

	newSteps := make([]string, 0)
	newSteps = append(newSteps, p.steps...)
	newSteps = append(newSteps, node)

	newCounts := make(map[string]int)
	for _, s := range newSteps {
		newCounts[s] = newCounts[s] + 1
	}

	newPath := path {
		steps: newSteps,
		validator: p.validator,
	}
	return newPath, true
}

type validation func(path, string) bool 

var part1Validation validation = func(p path, node string) bool {
	if node == strings.ToLower(node) {
		for _, n := range p.steps {
			if node == n {
				return false
			}
		}
	}

	return true
}

var part2Validation validation = func(p path, node string) bool {

	if node == "start" || node == "end" {
		for _, n := range p.steps {
			if n == node {
				return false
			}
		}
	} else if node == strings.ToLower(node) {
		count := make(map[string]int)
		for _, n := range p.steps {
			if n == strings.ToLower(n) {
				count[n] = count[n] + 1
			}
		}
		// if this new node isn't present, we are in the clear
		if count[node] == 0 {
			return true
		} else {
			// we already have visited this node, make sure we have not already used up our "double"
			for _, c := range count {
				if c > 1 {
					return false
				}
			}
		}
	}

	return true
}

func getInput(fileName string) graph {

	input := NewGraph()

	file, _ := os.Open(fileName)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		nodes := strings.Split(line, "-")
		input.addEdge(nodes[0], nodes[1])
	}

	return input
}

func main() {
	file := "input"
	part := 2

	g := getInput(file + ".txt")
	var validator validation
	if part == 1 {
		validator = part1Validation
	} else {
		validator = part2Validation
	}

	
	paths := g.findAllPaths(validator)

	fmt.Println(len(paths))
}