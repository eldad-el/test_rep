import sys

nums = sys.argv[1:]
if len(nums) > 1:
    print(sum([int(num) for num in nums]))
else:
    print("Usage: python <filename> <param1> <param2> [...]")