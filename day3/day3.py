def get_bits_array(lines):
    
    bitsArray = [0] * len(lines[0])

    for i in lines:
        for j in range(len(bitsArray)):
            bitsArray[j] += int(i[j])

    return bitsArray

def get_gamma_array(gammaArray, lineLen):

    for i in range(len(gammaArray)):
        if (gammaArray[i] > lineLen):
            gammaArray[i] = 1
        else:
             gammaArray[i] = 0

    return gammaArray

def get_value(array):

    val = 0
    index = 0

    for i in range(len(array)-1, -1, -1):
        if (array[i] == 1):
            val += pow(2, index)
        index += 1

    return val

def get_epsilon_array(gammaArray):
    
    epsilonArray = [0] * len(gammaArray)

    for i in range(len(epsilonArray)):
        if (gammaArray[i] == 1):
            epsilonArray[i] = 0
        else:
            epsilonArray[i] = 1

    return epsilonArray

def get_epsilon_value(gammaArray):

    val = 0
    index = 0

    epsilonArray = get_epsilon_array(gammaArray)

    for i in range(len(epsilonArray)-1, -1, -1):
        if (epsilonArray[i] == 1):
            val += pow(2, index)
        index += 1

    return val

def most_common(lst, index):
    
    ones = 0
    zeros = 0

    for i in lst:
        if (i[index] == '1'):
            ones += 1
        else:
            zeros += 1

    return ones >= zeros

def get_o_two(lines):
    
    index = 0
    val = [0] * len(lines[0])
    temp = lines.copy()

    while(len(temp) > 1):
        cmn = most_common(temp, index)
        new = temp.copy()

        for i in temp:
            if (int(i[index]) != cmn):
                new.remove(i)

        temp = new.copy()

        index += 1

    tmp = temp[0]
    for i in range(len(val)):
        if (tmp[i] == '1'):
            val[i] = 1

    return val

def get_c_scrub(lines):

    index = 0
    val = [0] * len(lines[0])
    temp = lines.copy()

    while(len(temp) > 1):
        cmn = not most_common(temp, index)
        new = temp.copy()

        for i in temp:
            if (int(i[index]) != cmn):
                new.remove(i)

        temp = new.copy()

        index += 1
    
    tmp = temp[0]
    for i in range(len(val)):
        if (tmp[i] == '1'):
            val[i] = 1
    
    return val

def main(): 

    # Open/store the file/data
    f = open("input3.txt", "r")
    lines = f.read().splitlines()

    # Find gamma and epsilon values
    bitsArray = get_bits_array(lines)
    gammaArray = get_gamma_array(bitsArray.copy(), len(lines)/2)
    gamma = get_value(gammaArray)
    epsilon = get_epsilon_value(gammaArray)

    # Get O2 generator and CO2 scrubber data
    oGenArray = get_o_two(lines)
    oGen = get_value(oGenArray)
    cScrubArray = get_c_scrub(lines)
    cScrub = get_value(cScrubArray)

    print(gamma * epsilon)
    print(oGen * cScrub)

main()