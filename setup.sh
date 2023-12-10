SESSION_COOKIE=$(<session.txt)

DAY=$1

DIR="day${DAY}"
mkdir -p "$DIR"

URL="https://adventofcode.com/2023/day/$DAY/input"

DEST_INPUT="$DIR/input"
DEST_MAIN1="$DIR/main1.go"
DEST_MAIN2="$DIR/main2.go"
DEST_COMMON="$DIR/common.go"

curl -sS -b "session=$SESSION_COOKIE" $URL >$DEST_INPUT

if [ -s $DEST_INPUT ]; then
	echo "Input file '$DEST_INPUT' created successfully with the contents from $URL"
else
	echo "Failed to download the contents from $URL"
	exit 1
fi

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

cat <<EOM >$DEST_COMMON
package main

// Your common functions or structs here
EOM

echo "Directory 'day$DAY' created with necessary files."
