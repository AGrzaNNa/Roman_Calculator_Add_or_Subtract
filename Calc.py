romans = {
    'CM': 900, 'LM': 950, 'VM': 995, 'IM': 999, 'XM': 990,
    'CD': 400, 'LD': 450, 'VD': 495, 'ID': 499, 'XD': 490,
    'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500,
    'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
}

def Add(input):
    values = input.split()
    romans_1 = values[0]
    romans_2 = values[2]

    result = 0

    for i in range(len(romans_1)):
        if i < len(romans_1) - 1 and romans[romans_1[i]] < romans[romans_1[i+1]]:
            result -= romans[romans_1[i]]
        else:
            result += romans[romans_1[i]]

    for i in range(len(romans_2)):
        if i < len(romans_2) - 1 and romans[romans_2[i]] < romans[romans_2[i+1]]:
            result -= romans[romans_2[i]]
        else:
            result += romans[romans_2[i]]

    return result

def Subtraction(input):
    values = input.split()
    romans_1 = values[0]
    romans_2 = values[2]

    result = 0
    result2= 0
    output =0

    for i in range(len(romans_1)):
        if i < len(romans_1) - 1 and romans[romans_1[i]] < romans[romans_1[i + 1]]:
            result -= romans[romans_1[i]]
        else:
            result += romans[romans_1[i]]

    for i in range(len(romans_2)):
        if i < len(romans_2) - 1 and romans[romans_2[i]] < romans[romans_2[i + 1]]:
            result2 -= romans[romans_2[i]]
        else:
            result2 += romans[romans_2[i]]

    output+=result-result2
    return output


def convert_to_roman(num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
        5: 'V', 4: 'IV', 1: 'I'
    }
    roman = ''
    for value, symbol in roman_numerals.items():
        while num >= value:
            roman += symbol
            num -= value
    return roman


def Action(input_str):
    values = input_str.split()
    if values[1] == "+":
        result = Add(input_str)
        roman_result = convert_to_roman(result)
        return roman_result
    elif values[1] == "-":
        result = Subtraction(input_str)
        if result <= 0:
            return "ERROR - you cannot subtract a larger value from a smaller one or make it 0!"
        else:
            roman_result = convert_to_roman(result)
            return roman_result
    else:
        return "ERROR - The specified operation is invalid or not supported"


print("Welcome to Roman Calculator. Choose one of the following activities: +/- (the maximum range is MM)")
input_str = input("Enter your equation : ")
result = Action(input_str)
print("Answer is:", result)



