import os
import requests
SESSION_COOKIE = open("session.txt").read().strip()
DAY = int(input("Enter the day: "))
YEAR = int(input("Enter the year: "))

if YEAR >= 2015 and YEAR <= 2023:
    DIR = f"{YEAR}/day{DAY}"
else:
    print("Invalid year. Please provide a year between 2015 and 2023.")
    exit(1)

try:
    os.makedirs(DIR)
except OSError:
    print(f"Failed to create directory '{DIR}'.")
    exit(1)

URL = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
DEST_INPUT = f"{DIR}/input"
DEST_MAIN = f"{DIR}/main.py"

# Create main.py file
with open(DEST_MAIN, "w") as file:
    file.write(f'''
def part1():
    print("This is main.py for {YEAR} Day {DAY}")
    # Your code here

def part2():
    print("This is main.py for {YEAR} Day {DAY}")
    # Your code here

if __name__ == "__main__":
    part1()
    part2()
''')

# Download input file
response = requests.get(URL, cookies={"session": SESSION_COOKIE})
if response.status_code == 200:
    with open(DEST_INPUT, "w") as file:
        file.write(response.text)
    print(f"Input file '{DEST_INPUT}' created successfully with the contents from {URL}")
else:
    print(f"Failed to download the contents from {URL}")
    exit(1)

if os.path.getsize(DEST_INPUT) > 0:
    print(f"Input file '{DEST_INPUT}' is not empty.")
else:
    print("The downloaded input file is empty or incomplete.")

try:
    os.chdir(DIR)
except OSError:
    print(f"Failed to change directory to '{DIR}'.")
    exit(1)
