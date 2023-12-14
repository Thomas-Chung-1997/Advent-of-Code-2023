import re

DESTINATIONS = "([A-Z][A-Z][A-Z])"
START = "AAA"
END ="ZZZ"


def main():
    print(HauntedWasteland())
    
def HauntedWasteland():
    instructions = list()
    navigation = dict()
    count = 0
    currentLocation = START
    
    with open("test.txt") as file:
        instructions = list(file.readline().strip())
        
        file.readline() # Delete spacer line
        
        for line in file:
            destinations = re.finditer(DESTINATIONS, line)
        
            destinations = list(map(lambda x : x.group(), destinations))
            
            navigation[destinations[0]] = (destinations[1],destinations[2])
    
    while currentLocation != END:
        currentLocation = NextDestination(instructions[count % len(instructions)], navigation[currentLocation])
        count += 1
    
    return count

def NextDestination(direction, location):
    if direction == "L":
        return location[0]
    elif direction == "R":
        return location[1]
    else:
        return START


if __name__ == "__main__":
    main()