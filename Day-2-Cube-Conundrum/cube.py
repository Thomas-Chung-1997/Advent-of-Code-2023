import re

CONST_RED = 12
CONST_GREEN = 13
CONST_BLUE = 14
CONST_FIND_CUBES = "(\d+ green| \d+ blue| \d+ red)"

def main():
    print(Cube())
    
def Cube():
    count = 0
    
    with open("test.txt") as file:
        # PART 1
        #i = 1
        #for line in file:
            
        #    if Game(line):
        #        count += i
            
        #    i += 1
        
        for line in file:
            count += Game(line)
            
    return count
        
def Game(line):
    red = 0
    green = 0
    blue = 0
    cubes = GetCubes(line)
    
    #print(line)
    
    for c in cubes:
        c = c.split()
        c[0] = int(c[0])
        
        #print(c[0])
        
        if c[1] == "red" and c[0] > red:
            red = c[0]
        elif c[1] == "green" and c[0] > green:
            green = c[0]
        elif c[1] == "blue" and c[0] > blue:
            blue = c[0]
            
        #print(str(red) + ' ' + str(green) + ' ' + str(blue))
    
    # PART 1
    #if red <= CONST_RED and green <= CONST_GREEN and blue <= CONST_BLUE:
    #    return True
    #else:
    #    return False  
    
    return red * green * blue

def GetCubes(line):
    cubes = re.finditer(CONST_FIND_CUBES, line)
        
    return list(map(lambda x : x.group(), cubes))
        
if __name__ == "__main__":
    main()