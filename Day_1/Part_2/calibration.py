# To find the calibration values first we need to combine the sum of the first
# and last digit to create a two number. Then we need to sum the total of
# every line of input to get the final result.
#
# We have a file named input from where we will pull our sample data.

from datetime import date
import re


# Parse a given string for the first digit found
def ParseFirstDigit(input_line):
    regex = re.search("[0-9]", input_line)
    return input_line[regex.start()]

# Parse a string in reverse for the first digit found.
# This will give us the last digit on a given input.
def ParseLastDigit(input_line):
    reverse_input=input_line[::-1]
    regex=re.search("[0-9]",reverse_input)
    return reverse_input[regex.start()]

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
