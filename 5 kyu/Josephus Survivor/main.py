def josephus_survivor(n,k):
    if n == 1:
        return 1
    if k == 1:
        return n
    else:
        return 1 + (josephus_survivor(n - 1, k) + k - 1) % n
print(josephus_survivor(7,3))