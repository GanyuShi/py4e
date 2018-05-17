import re

file = input('enter file: ')
if len(file) < 1: 
	file = 'regex_sum_42.txt'
handle = open(file)

sum = 0
for line in handle:
	nums = re.findall('[0-9]+', line)
	for num in nums:
		sum += int(num)
print(sum)

