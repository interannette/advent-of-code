package main

import "fmt"

func doPart2(input []instruction) {
	ship := position{
		x: 0,
		y: 0,
	}

	waypoint := position{
		x: 10,
		y: 1,
	}

	for _, i := range input {
		waypoint, ship = applyInstruction2(i, waypoint, ship)
	}

	printFinal(ship)

}

func rotateWaypoint(angle int, waypoint position) position {
	switch angle {
	case 0:
		return waypoint
	case 90:
		// x = y
		// y = -x
		return position{
			x: waypoint.y,
			y: -waypoint.x,
		}
	case 180:
		// x = -x
		// y = -y
		return position{
			x: -waypoint.x,
			y: -waypoint.y,
		}
	case 270:
		// x = -y
		// y = x
		return position{
			x: -waypoint.y,
			y: waypoint.x,
		}
	default:
		panic("unsupported angle")
	}
}

func advance(waypoint position, ship position) position {
	new_ship := position{
		x: ship.x + waypoint.x,
		y: ship.y + waypoint.y,
	}
	return new_ship
}

func applyInstruction2(ins instruction, waypoint position, ship position) (position, position) {
	fmt.Printf("Applying instruction %s\n", ins)
	new_waypoint := waypoint
	new_ship := ship
	switch ins.a {
	case north:
		new_waypoint.y = waypoint.y + ins.v
	case south:
		new_waypoint.y = waypoint.y - ins.v
	case east:
		new_waypoint.x = waypoint.x + ins.v
	case west:
		new_waypoint.x = waypoint.x - ins.v
	case left:
		angle := consolidateAngle(-ins.v)
		new_waypoint = rotateWaypoint(angle, new_waypoint)
	case right:
		angle := consolidateAngle(ins.v)
		new_waypoint = rotateWaypoint(angle, new_waypoint)
	case forward:
		for i := 0; i < ins.v; i++ {
			new_ship = advance(new_waypoint, new_ship)
		}
	default:
		panic("unknown action")
	}

	fmt.Printf("Ship %s. Waypoint %s\n", new_ship, new_waypoint)
	return new_waypoint, new_ship
}
