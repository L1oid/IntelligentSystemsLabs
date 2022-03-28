nums = [int(s) for s in input().split()]
print(*sorted(nums, key=lambda s: abs(s), reverse=True))
