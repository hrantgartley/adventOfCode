package main

import (
	"bufio"
	"os"
)

type Coordinate struct{ i, j int }

const Size = 140

func parse() map[Coordinate]byte {
	scanner := bufio.NewScanner(os.Stdin)

	m := map[Coordinate]byte{}

	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()

		for j := 0; j < len(line); j++ {
			c := line[j]
			if c == '.' {
				continue
			}
			m[Coordinate{i, j}] = c
		}
	}
	return m
}

func isDigit(b byte) bool {
	return b >= '0' && b <= '9'
}
