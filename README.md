DESCRIPTION OF THE SOLUTION

For solving this task, I used a dictionary named "roman" that stores the values of Roman numerals along with their Arabic counterparts up to M: 1000.

The program's operation begins by fetching the input text as "values" and splitting it using .split() into three values: romans_1, romans_2, and "operation_sign(values[1])". Next, depending on the "operation_sign(values[1])", the program proceeds to the corresponding loop: Add (addition) or Subtraction (subtraction).

In both loops, we iterate over individual numeral characters using a for loop, iterating for the length of these numerals (len(romans_1) - 1). For each character, we check if the next character is greater than the current one. If so, we subtract the value of the current character from the result. Otherwise, we add the value of the character to the result.

Example: CXL
result = 100
i++
XL X<L
result -= 10 // 90
result += 50 // 140

Then, the result of the operation is passed to the "convert_to_roman" function, which converts the Arabic numeral representation to Roman numeral representation. In this function, there is a loop that iterates over pairs of value-symbol in the "roman_numerals" dictionary. For each pair, the loop checks if the given number is greater than or equal to the value. If so, it adds the corresponding symbol to the "roman" string and subtracts the value from the number. The loop continues as long as the number is greater than or equal to the current value.

In the end, the "convert_to_roman" function returns the final result in Roman numeral representation. In case of an invalid operation sign, attempts to subtract a larger number from a smaller one, or a result equal to zero, the program returns appropriate error messages.

In this way, the program performs addition and subtraction of numbers in Roman numeral representation, providing the result in the same format.
