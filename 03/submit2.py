import sys
import re

with open(sys.argv[1], 'r') as f:
    content = f.read()
print(content)
matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", content)
print(matches)
answer = 0
do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        nums = re.findall(r'\d+', match)
        answer += int(nums[0]) * int(nums[1])
print(answer)
