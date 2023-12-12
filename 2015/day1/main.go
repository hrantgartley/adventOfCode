package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	part1()
	part2()
}

func part1() {
	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	openParen := 0
	closeParen := 0

	for scanner.Scan() {
		line := scanner.Text()
		for _, char := range line {
			switch char {
			case '(':
				openParen++
			case ')':
				closeParen++
			}
		}
	}

	currentFloor := openParen - closeParen
	fmt.Println("Santa is on floor", currentFloor)
}

func part2() {
	baseFloor := 0
	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	position := 0 // Initialize position tracker
	for scanner.Scan() {
		line := scanner.Text()
		for _, char := range line {
			position++
			switch char {
			case '(':
				baseFloor++
			case ')':
				baseFloor--
			}
			if baseFloor == -1 {
				fmt.Println("Santa entered the basement at position", position)
				return
			}
		}
	}
	fmt.Println("Santa never enters the basement.")
}
