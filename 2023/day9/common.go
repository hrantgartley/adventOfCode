package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func parse() [][]int {
	scanner := bufio.NewScanner(os.Stdin)
	listOfSeq := [][]int{}
	for scanner.Scan() {
		sequence := []int{}
		for _, field := range strings.Fields(scanner.Text()) {
			n, _ := strconv.Atoi(field)
			sequence = append(sequence, n)
		}
		listOfSeq = append(listOfSeq, sequence)
	}
	return listOfSeq
}

func buildPascal(firstSeq []int) [][]int {
	pascalTriangle := [][]int{firstSeq}
	for {
		prevRow := len(pascalTriangle) - 1

		finished := true
		newRow := make([]int, len(pascalTriangle[prevRow])-1)
		for i := 0; i < len(pascalTriangle[prevRow])-1; i++ {
			newRow[i] = pascalTriangle[prevRow][i+1] - pascalTriangle[prevRow][i]
			if newRow[i] != 0 {
				finished = false
			}
		}
		pascalTriangle = append(pascalTriangle, newRow)

		if finished {
			return pascalTriangle
		}
	}
}
