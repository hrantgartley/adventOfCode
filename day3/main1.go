package main

import "fmt"

func main() {
	grid := parse()

	sum := 0
	for row := 0; row < Size; row++ {
		for col := 0; col < Size; col++ {

			currentCoordinate := Coordinate{row, col}
			currentCharacter := grid[currentCoordinate]

			if isDigit(currentCharacter) {
				valid := false
				num := 0
				for isDigit(currentCharacter) {
					num = 10*num + int(currentCharacter-'0')
					valid = valid || isValid(grid, currentCoordinate)
					col++
					currentCoordinate = Coordinate{row, col}
					currentCharacter = grid[currentCoordinate]
				}

				if valid {
					sum += num
				}
			}
		}
	}
	fmt.Println(sum)
}

func isValid(m map[Coordinate]byte, c Coordinate) bool {
	delta := []int{-1, 0, 1}
	for _, di := range delta {
		for _, dj := range delta {
			if di|dj != 0 {
				ch, exists := m[Coordinate{c.i + di, c.j + dj}]
				if exists && !isDigit(ch) {
					return true
				}
			}
		}
	}
	return false
}
