A = {'a', 'g', 'b', 'd', 'f', 'c'}
B = {'l', 'm', 'o', 'b', 'h', 'c'}
C = {'k', 'i', 'j', 'h', 'd', 'f', 'c'}

elements_in_A_and_B = A & B
print("How many elements are there in set A and B:", len(elements_in_A_and_B))
elements_in_B_not_A_or_C = B - (A | C)
print("How many elements are there in B that is not part of A and C:", len(elements_in_B_not_A_or_C))

i = C - A  # [h, i, j, k]
ii = C & A  # [c, d, f]
iii = (B & C) | {'b'}  # [b, c, h]
iv = A & C - {'c'}  # [d, f]
v = C & {'c'}  # [c]
vi = B - (A | C)  # [l, m, o]

print("i:", i)
print("ii:", ii)
print("iii:", iii)
print("iv:", iv)
print("v:", v)
print("vi:", vi)