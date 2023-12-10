# 53616c7465645f5ff5a4de6b64d2b0a8573796f4adeee30561705dfafcb505724e106668068eb54717e1d0b8ab1a996b25c94391c87b65a71c3b9a4f8a110129
SESSION_COOKIE="53616c7465645f5ff5a4de6b64d2b0a8573796f4adeee30561705dfafcb505724e106668068eb54717e1d0b8ab1a996b25c94391c87b65a71c3b9a4f8a110129"

# Day number provided as argument
DAY=$1

# Create directory for the day
DIR="day${DAY}"
mkdir -p "$DIR"

# URL to fetch data from
URL="https://adventofcode.com/2023/day/$DAY/input"

# Destination file names and paths
DEST_INPUT="$DIR/input.txt"
DEST_MAIN1="$DIR/main1.go"
DEST_MAIN2="$DIR/main2.go"
DEST_COMMON="$DIR/common.go"

# Fetch the data from the URL and save it to the input file
curl -sS -b "session=$SESSION_COOKIE" $URL >$DEST_INPUT

# Check if the input file was created successfully
if [ -s $DEST_INPUT ]; then
	echo "Input file '$DEST_INPUT' created successfully with the contents from $URL"
else
	echo "Failed to download the contents from $URL"
	exit 1
fi

# Create main1.go file
cat <<EOM >$DEST_MAIN1
package main

import (
	"fmt"
)

func main() {
	fmt.Println("This is main1.go for Day $DAY")
	// Your code here
}
EOM

# Create main2.go file
cat <<EOM >$DEST_MAIN2
package main

import (
	"fmt"
)

func main() {
	fmt.Println("This is main2.go for Day $DAY")
	// Your code here
}
EOM

# Create common.go file
cat <<EOM >$DEST_COMMON
package main

// Your common functions or structs here
EOM

echo "Directory 'day$DAY' created with necessary files."
