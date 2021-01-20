n = int(input("Place a value for n: "))

value_1 = n

value_2 = int('{}{}'.format(n,n))


value_3 = int('{}{}{}'.format(n,n,n))


value_4 = int('{}{}{}{}'.format(n,n,n,n))

ans = value_1 + value_2 + value_3 + value_4

print("Your answer for n+nn+nnn+nnnn is:", ans)

input("Press Enter to finish")


