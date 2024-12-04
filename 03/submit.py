import sys
import re

with open(sys.argv[1], 'r') as f:
    content = f.read()
print(content)
matches = re.findall("mul\(\d{1,3},\d{1,3}\)", content)
answer = 0
for match in matches:
    print(match)
    nums = re.findall(r'\d+', match)
    answer += int(nums[0]) * int(nums[1])
print(answer)
