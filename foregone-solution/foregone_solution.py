# Solution to first qualification problem, "Foregone Solution".
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

from sys import stdin

num_cases = int(stdin.readline())
# print(num_cases)

for case in range(1, num_cases + 1):
    line = stdin.readline().strip()

    num1, num2 = 0, 0
    for digit in line:
        # Shift any existing digits one place to the left.
        num1 = 10 * num1
        num2 = 10 * num2

        if digit != '4':
            num1 += int(digit)
        else:
            num1 += 2           # Split the 4 into a couple of 2s.
            num2 += 2

    print("Case #{}: {} {}".format(case, num1, num2))
