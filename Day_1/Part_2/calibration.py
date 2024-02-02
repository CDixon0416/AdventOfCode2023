# To find the calibration values first we need to combine the sum of the first
# and last digit to create a two number. Then we need to sum the total of
# every line of input to get the final result.
#
# We have a file named input from where we will pull our sample data.

from datetime import date
import re

# Parse a given string for the first digit found
def ParseFirstDigit(input_line):
    int_regex = re.search("[0-9]", input_line)
    str_regex = re.findall("one|two|three|four|five|six|seven|eight|nine", input_line)

    if not str_regex or int_regex.start() < re.search(str_regex[0], input_line).start():
        return input_line[int_regex.start()]
    else:
        match str_regex[0]:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9

# Parse a string in reverse for the first digit found.
# This will give us the last digit on a given input.
def ParseLastDigit(input_line):
    reverse_input=input_line[::-1]

    int_regex = re.search("[1-9]", reverse_input)
    str_regex = re.findall("eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", reverse_input)

    if not str_regex or int_regex.start() < re.search(str_regex[0], reverse_input).start():
        return reverse_input[int_regex.start()]
    else:
        match str_regex[0]:
            case "eno":
                return 1
            case "owt":
                return 2
            case "eerht":
                return 3
            case "ruof":
                return 4
            case "evif":
                return 5
            case "xis":
                return 6
            case "neves":
                return 7
            case "thgie":
                return 8
            case "enin":
                return 9

# Add our two values together to create our initial calibration.
def CreateInitialCalibration(input_line):
    first_digit=ParseFirstDigit(input_line)
    last_digit=ParseLastDigit(input_line)

    initial_calibration=str(first_digit) + str(last_digit)

    return int(initial_calibration)

# Find our end result as an answer and save it a file for convenience.
def SumCalibrationTotal(input_line):
    return CreateInitialCalibration(input_line)

def main():
    calibration_total=0
    with open('input') as file:
        for line in file:
            calibration_total+=SumCalibrationTotal(line)
    file.close()
    result=open("result.txt", "a")
    result.write(str(date.today()) + ": " + str(calibration_total) + "\n")
    result.close()

if __name__ == "__main__":
    main()
