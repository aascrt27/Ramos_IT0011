print("a.")
for i in range(1, 6):
    print(" " * (5 - i), end="   ")
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
print("\nb.")
i = 1
while i <= 5:
    print(" ", end="  ")
    j=1
    while j <= i * 2 - 1:
        print(i * 2 - 1, end="")
        j += 1
    print()
    i += 1