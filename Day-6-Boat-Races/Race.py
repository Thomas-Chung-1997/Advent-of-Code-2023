def main():
    print(BoatRaces())
    
def BoatRaces():
    count = 0
    
    with open("test.txt") as file:
        times = file.readline().strip().split(":")[1]
        distance = file.readline().strip().split(":")[1]
            
        times = times.replace(" ", "")
        distance = distance.replace(" ", "")
        
        count = WinningOutcomes(times, distance)
    
    return count

def WinningOutcomes(time, distanceToBeat):
    time = int(time)
    distanceToBeat = int(distanceToBeat)
    count = 0
    
    for i in range(1, time + 1):
        
        if i * (time - i) > distanceToBeat:
            count += 1
    
    return count

if __name__ == "__main__":
    main()