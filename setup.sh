#!/bin/bash

SESSION_COOKIE=$(<session.txt)
DAY=$1
YEAR=$2

if [ "$YEAR" -ge 2015 ] && [ "$YEAR" -le 2023 ]; then
	DIR="${YEAR}/day${DAY}"
else
	echo "Invalid year. Please provide a year between 2015 and 2023."
	exit 1
fi

mkdir -p "$DIR" || {
	echo "Failed to create directory '$DIR'."
	exit 1
}

URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"

DEST_INPUT="$DIR/input"
DEST_MAIN="$DIR/main.py"

# Create main.py file
cat <<EOM >"$DEST_MAIN"
def part1():
    print("This is main.py for Day $DAY")
    # Your code here

def part2():
    print("This is main.py for Day $DAY")
    # Your code here

if __name__ == "__main__":
    part1()
    part2()
EOM

# Download input file
if ! curl -sS --cookie "session=$SESSION_COOKIE" "$URL" >"$DEST_INPUT"; then
	echo "Failed to download the contents from $URL"
	exit 1
fi

if [ -s "$DEST_INPUT" ]; then
	echo "Input file '$DEST_INPUT' created successfully with the contents from $URL"
else
	echo "The downloaded input file is empty or incomplete."
	exit 1
fi
