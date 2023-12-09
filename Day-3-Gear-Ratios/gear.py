CONST_SYMBOLS = ["-", "+", "/", "$", "@", "=", "*", "&", "#", "%"]
array2D = []

def main():
    print(Gear())
    
def Gear():
    
    with open("test.txt") as file:
        for line in file:
            array2D.append(line[0: -1])
    
    return FindParts()

def FindParts():
    count = 0
    
    for line in range(len(array2D)):
        count += ScanLine(line)
    
    return count
    
def ScanLine(currentLine):
    count = 0;
    currentNumber = 0
    partFlag = False
    
    for x in range(len(array2D[currentLine])):
        if array2D[currentLine][x].isdigit():
            if currentNumber == 0:
                currentNumber = int(array2D[currentLine][x])
            else:
                currentNumber = currentNumber * 10 + int(array2D[currentLine][x])
                
            if IsPart(x, currentLine):
                partFlag = True
            
        else:
            if partFlag:
                count += currentNumber
            
            currentNumber = 0
            partFlag = False
        
    
    return count
    
    
def IsPart(posX,poxY):
    left, right , top, bottom = posX - 1, posX + 1, poxY - 1, poxY + 1
    
    if left < 1:
        left = 0
    if right > len(array2D[poxY]) - 1:
        right = len(array2D[poxY]) - 1
    if top < 1:
        top = 0
    if bottom < len(array2D) - 1:
        bottom = len(array2D) - 1
        
    for x in range(left, right):
        for y in range(top, bottom):
            if array2D[y][x] in CONST_SYMBOLS:
                return True
    
    return False
    
    
    #return True
    
    
    

if __name__ == "__main__":
    main()