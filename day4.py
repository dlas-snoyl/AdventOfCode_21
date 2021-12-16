def main():
    boards, nums = get_boards()
    
# Get the bingo boards and the order of the values
def get_boards():

    rawInput = [line.split("\n") for line in open("test4.txt", "r").read().split("\n\n")]
    nums = [int(x)for x in rawInput[0][0].split(",")]
    rawInput.pop(0)

    boards = []

    for i in range(len(rawInput)):
        boards.append(list())
        for j in range(len(rawInput[i])):
            boards[i].append([int(x) for x in rawInput[i][j].split()])

    return boards, nums

if __name__ == '__main__':
    main()