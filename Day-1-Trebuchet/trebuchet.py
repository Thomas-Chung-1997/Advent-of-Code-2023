import re

NUMBERS = "(?:zero|one|two|three|four|five|six|seven|eight|nine|[0-9])"
CONVERT_NUMBERS = {"zero" : 0,"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def main():
    print(Trebuchet())
    
def Trebuchet():
    count = 0
    
    with open("test.txt") as file:
        for line in file:
            count += CalibrationValue(line)
            
    return count
    
def CalibrationValue(line):
    digits = GetNumbers(line)
                
    return digits[0] * 10 + digits[-1]

def GetNumbers(line):
    digits = re.finditer(NUMBERS, line)
        
    digits = list(map(lambda x : x.group(), digits))
    
    return ConvertWordsToNumbers(digits)

def ConvertWordsToNumbers(digits):
    for i in range(len(digits)):
        if digits[i] in CONVERT_NUMBERS:
            digits[i] = CONVERT_NUMBERS[digits[i]]
            
    return digits
    
if __name__ == "__main__":
    main()