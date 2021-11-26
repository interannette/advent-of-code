package main

import (
	"fmt"
	"math"
)

func applyInstruction(i instruction, p position) position {
	new_pos := p

	switch i.a {
	case north:
		new_pos.y = new_pos.y + i.v
	case south:
		new_pos.y = new_pos.y - i.v
	case east:
		new_pos.x = new_pos.x + i.v
	case west:
		new_pos.x = new_pos.x - i.v
	case left:
		new_pos.d = consolidateAngle(new_pos.d - i.v)
	case right:
		new_pos.d = consolidateAngle(new_pos.d + i.v)
	case forward:
		switch p.d {
		case 0:
			new_pos.y = new_pos.y + i.v
		case 90:
			new_pos.x = new_pos.x + i.v
		case 180:
			new_pos.y = new_pos.y - i.v
		case 270:
			new_pos.x = new_pos.x - i.v
		default:
			panic("only handling 90 degree angles")
		}
	default:
		panic("unknown action")
	}

	return new_pos
}

// 0 - 360 degrees. 0 = N
func consolidateAngle(i int) int {
	// assuming i is postitive
	if i >= 0 {
		return i % 360
	} else {
		return 360 + i
	}
}

func doPart1(input []instruction) {
	pos := position{
		x: 0,
		y: 0,
		d: 90,
	}

	for _, ins := range input {
		pos = applyInstruction(ins, pos)
	}

	printFinal(pos)
}

func printFinal(pos position) {
	fmt.Printf("Final position %s. Distance %.0f\n", pos, math.Abs(float64(pos.x))+math.Abs(float64(pos.y)))

}
