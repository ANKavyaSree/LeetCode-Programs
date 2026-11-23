class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]


# User input
n = int(input("Enter number of operations: "))

product = ProductOfNumbers()

for _ in range(n):
    operation = input().split()

    if operation[0] == "add":
        num = int(operation[1])
        product.add(num)

    elif operation[0] == "getProduct":
        k = int(operation[1])
        print(product.getProduct(k))
