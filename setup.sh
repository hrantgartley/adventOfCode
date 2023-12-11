SESSION_COOKIE=$(<session.txt)
DAY=$1
YEAR=$2

if [ "$YEAR" -ge 2015 ] && [ "$YEAR" -le 2023 ]; then
	DIR="${YEAR}/day${DAY}"
else
	echo "Invalid year. Please provide a year between 2015 and 2023."
	exit 1
fi

mkdir -p "$DIR"

URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"

DEST_INPUT="$DIR/input"
DEST_MAKEFILE="$DIR/Makefile"

if [ "$YEAR" -lt 2023 ]; then
	DEST_MAIN="$DIR/main.go"

	# Create main.go file
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

	# Create an empty input file
	touch $DEST_INPUT

	curl -sS --cookie "session=$SESSION_COOKIE" $URL >$DEST_INPUT
	echo "Directory 'day$DAY' created with necessary files for years 2015-2022."
    cat <<EOM >$DEST_MAKEFILE
main:
	go build main.go

.PHONY: run clean

run: main
	./main <input

clean:
	rm -f main
EOM

else

	curl -sS --cookie "session=$SESSION_COOKIE" $URL >$DEST_INPUT

	if [ -s $DEST_INPUT ]; then
		echo "Input file '$DEST_INPUT' created successfully with the contents from $URL"
	else
		echo "Failed to download the contents from $URL"
		exit 1
	fi

	DEST_MAIN1="$DIR/main1.go"
	DEST_MAIN2="$DIR/main2.go"
	DEST_COMMON="$DIR/common.go"

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

	echo "Directory 'day$DAY' created with necessary files for 2023."

fi


if [ "$YEAR" -eq 2023 ]; then
cat <<EOM >$DEST_MAKEFILE
main1:
    go build -o main1 main1.go common.go

main2:
    go build -o main2 main2.go common.go

.PHONY: run1 run2 clean

run1: main1
    ./main1 <input

run2: main2
    ./main2 <input

clean:
    rm -f main1 main2
EOM
fi

if [ -s $DEST_MAKEFILE ]; then
	echo "Makefile created successfully"
else
	echo "Failed to create Makefile"
	exit 1
fi

cd "$DIR" || exit
go mod init $DAY
go mod tidy

echo "go.mod and go.sum created successfully"
