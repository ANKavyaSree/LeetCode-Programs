n = int(input("Enter the number of piles: "))
piles = list(map(int, input("Enter the stones in each pile: ").split()))

# Under the given constraints, Alice always wins.
print("Alice wins:", True)
