def main():
    print(trebuchet())
    
def trebuchet():
    count = 0
    
    with open("test.txt") as file:
        for line in file:
            count += CalibrationValue(line)
            
    return count
    
def CalibrationValue(line):
    firstDigit = 0
    secondDigit = 0
    firstflag = True
    
    for char in line:
        if char.isnumeric():
            number = int(char)
            
            if firstflag:
                firstDigit = number
                secondDigit = number
                firstflag = False
            else:
                secondDigit = number
                
    #print(line)
    #print(firstDigit * 10 + secondDigit)
                
    return firstDigit * 10 + secondDigit
    
if __name__ == "__main__":
    main()