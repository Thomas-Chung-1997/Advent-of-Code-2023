def main():
    print(CropRotation())
    
def CropRotation():
    seeds = list()
    almanac = dict()
    
    with open("test.txt") as file:
        seeds = list(map(lambda x : int(x), file.readline().strip().split(": ")[1].split(" ")))
        name = ""
        section = False
        
        for line in file:
            line = line.strip()
            
            if line == "":
                name = ""
                section = False
            else:
                if section:
                    almanac[name].append(list(map(lambda x : int(x), line.split(" "))))
                else:
                    almanac[line] = list()
                    name = line
                    section = True
                    
        #seeds = list(set(UnpackSeeds(seeds)))
        
        for section in almanac:
            for i in range(len(seeds)):
                seeds[i] = SourceToDestination(seeds[i], almanac[section])
    
    return min(seeds)

#def UnpackSeeds(seeds):
#    unpackedSeeds = list()
#    
#    for i in range(0, len(seeds), 2):
#        unpackedSeeds.extend(range(seeds[i], seeds[i] + seeds[i + 1]))
#            
#    return unpackedSeeds

def SourceToDestination(source, destinations):
    converts = list()
    
    for conversion in destinations:
        if conversion[1] <= source and conversion[1] + conversion[2] >= source:
            difference = conversion[1] + conversion[2] - source
            converts.append(conversion[0] + conversion[2] - difference)
            
    if converts:
        return min(converts)
    else:
        return source

if __name__ == "__main__":
    main()