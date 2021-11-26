package main

import (
	"fmt"
)

type position struct {
	x int
	y int
	d int
}

func (p position) String() string {
	return fmt.Sprintf("(%d,%d)%d", p.x, p.y, p.d)
}
