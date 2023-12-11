package main

import "fmt"

func main() {
	triangeData := parse()

	runningTotal := 0
	for _, row := range triangeData {
		currentRow := buildPascal(row)

		currentRow[len(currentRow)-1] = append(currentRow[len(currentRow)-1], 0)

		for i := len(currentRow) - 2; i >= 0; i-- {
			currentRow[i] = append(currentRow[i], currentRow[i][len(currentRow[i])-1]+currentRow[i+1][len(currentRow[i+1])-1])
		}

		runningTotal += currentRow[0][len(currentRow[0])-1]
	}

	fmt.Println(runningTotal)
}
