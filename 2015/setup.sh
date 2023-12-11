SESSION_COOKIE=$(<session.txt)
DAY=$1
YEAR=$2

# Check if the year is within the specified range
if [ "$YEAR" -ge 2015 ] && [ "$YEAR" -le 2023 ]; then
	DIR="${YEAR}/day${DAY}"
else
	echo "Invalid year. Please provide a year between 2015 and 2023."
	exit 1
fi

mkdir -p "$DIR"

URL="https://adventofcode.com/$YEAR/day/$DAY/input"

DEST_INPUT="$DIR/input"
DEST_MAIN="$DIR/main.go"

curl -sS -b "session=$SESSION_COOKIE" $URL >$DEST_INPUT

if [ -s $DEST_INPUT ]; then
	echo "Input file '$DEST_INPUT' created successfully with the contents from $URL"
else
	echo "Failed to download the contents from $URL"
	exit 1
fi

cat <<EOM >$DEST_MAIN
package main

import (
	"fmt"
)

func main() {
	fmt.Println("This is main.go for Day $DAY")
	// Your code here
}
EOM
