# Day 36 - Destroying Asteroids
# User Input Version

mass = int(input("Enter initial planet mass: "))

n = int(input("Enter number of asteroids: "))

asteroids = list(map(int, input("Enter asteroid masses: ").split()))

asteroids.sort()

can_destroy = True

for asteroid in asteroids:
    if mass >= asteroid:
        mass += asteroid
    else:
        can_destroy = False
        break

print("Can destroy all asteroids:", can_destroy)



# sample input
# Enter initial planet mass: 10
# Enter number of asteroids: 5
# Enter asteroid masses: 3 9 19 5 21

# sample output
# Can destroy all asteroids: True