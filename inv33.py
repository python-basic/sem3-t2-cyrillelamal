def fib(num):
    a = b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b

nums = list(fib(22))
print(nums[10:12])
print(nums[4:2:-1])
