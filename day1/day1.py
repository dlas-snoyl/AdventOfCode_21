nums = []
f = open("input1.txt", "r")

nums = list(map(int, f.read().splitlines()))

a = nums[0]
b = nums[1]
c = nums[2]
prev = a+b+c
curr = 0
count = 0

for i in range(1, len(nums)-2):
    a = nums[i]
    b = nums[i+1]
    c = nums[i+2]
    
    curr = a+b+c
    #print(f"{prev} -> {curr} = {a} + {b} + {c}")

    if curr > prev:
        count += 1

    prev = curr

print(count)