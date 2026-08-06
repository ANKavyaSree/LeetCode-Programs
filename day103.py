n = int(input("Enter n: "))
t = int(input("Enter t: "))

while True:
    product = 1
    for digit in str(n):
        product *= int(digit)

    if product % t == 0:
        print("Smallest number:", n)
        break

    n += 1
