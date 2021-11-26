package main

type action int

const (
	north action = iota
	south
	east
	west
	left
	right
	forward
)

func parseAction(s string) action {
	switch s {
	case "N":
		return north
	case "S":
		return south
	case "E":
		return east
	case "W":
		return west
	case "L":
		return left
	case "R":
		return right
	case "F":
		return forward
	default:
		panic("Could not parse action")
	}
}

func (a action) String() string {
	switch a {
	case north:
		return "N"
	case south:
		return "S"
	case east:
		return "E"
	case west:
		return "W"
	case left:
		return "L"
	case right:
		return "R"
	case forward:
		return "F"
	default:
		return "unknown"
	}
}
