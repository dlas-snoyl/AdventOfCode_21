def main():
    boards, nums = get_boards()
    boardNum, mask, lastVal = check_boards(boards, nums)
    score_board(boards[boardNum], mask, lastVal)
    
# Get the bingo boards and the order of the values
def get_boards():

    rawInput = [line.split("\n") for line in open("input4.txt", "r").read().split("\n\n")]
    nums = [int(x)for x in rawInput[0][0].split(",")]
    rawInput.pop(0)

    boards = []

    for i in range(len(rawInput)):
        boards.append(list())
        for j in range(len(rawInput[i])):
            boards[i].append([int(x) for x in rawInput[i][j].split()])

    return boards, nums

# Check if current board is solved
def is_solved(mask):

    solved = False

    for i in mask:
        if (0 not in i):
            solved = True
    
    if (not solved):
        for i in range(5):
            tmp = []
            for j in range(5):
                tmp.append(mask[j][i])

            if (0 not in tmp):
                solved = True
                break

    return solved

# Iterate through boards until one is solved
def check_boards(boards, nums):
    
    mask = [[[0 for i in range(5)] for j in range(5)] for k in range(len(boards))]

    for i in range(len(nums)):
        for j in range(len(boards)):

            for k in range(5):
                for l in range(5):
                    if (boards[j][k][l] == nums[i]):
                        mask[j][k][l] = 1

                    if (is_solved(mask[j])):
                        return j, mask[j], nums[i]

# Score the first winning board
def score_board(board, mask, val):

    unmarked = 0

    for i in range(5):
        for j in range(5):
            if (not mask[i][j]):
                unmarked += board[i][j]
                
    print(unmarked * val)

if __name__ == '__main__':
    main()