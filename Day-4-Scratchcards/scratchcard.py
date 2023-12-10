cards = dict()

def main():
    print(ScratchCard())
    
def ScratchCard():
    global cards
    
    with open("test.txt") as file:
        count = 1
        
        for line in file:
            split = line.strip().split(": ")[1].split(" | ")
            userNumbers = set(split[1].split(" "))
            winningNumbers = set(split[0].split(" "))
            
            userNumbers.discard("")
            winningNumbers.discard("")
            
            if count not in cards:
                cards[count] = 1
            else:
                cards[count] += 1
            
            Game(count, userNumbers, winningNumbers)
            
            count += 1
            
    total = 0
    
    for i in range(1,count):
        total += cards[i]
    
    return total
    

def Game(currentCard, numbers, winningNumbers):
    global cards
    total = len(numbers.intersection(winningNumbers))
        
    multiplier = cards[currentCard]
    
    for c in range(1, total + 1):
        if currentCard + c not in cards:
            cards[currentCard + c] = multiplier
        else:
            cards[currentCard + c] += multiplier

if __name__ == "__main__":
    main()