#!/usr/bin/python3

elves = []
with open('input.txt', 'r') as f:
    calories = 0
    for x in f:
        if x != '\n':
            calories += int(x.strip())
        else:
            elves.append(calories)
            calories = 0
    print(sum(sorted(elves)[-1:-4:-1]))
