val = []
def fat(x):
    if x == 1:
        return x
    else:
        val.append(x)
        return x * fat(x-1)

print(fat(5))
print(val)