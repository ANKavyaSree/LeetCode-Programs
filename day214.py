n = int(input())

remove = 10
alice_turn = True

while n >= remove:
    n -= remove
    alice_turn = not alice_turn
    remove -= 1

print(alice_turn)
