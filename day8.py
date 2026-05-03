def rotateString(s, goal):
    # Length mismatch → not possible
    if len(s) != len(goal):
        return False
    
    # Core trick
    return goal in (s + s)


# -------- User Input --------
s = input("Enter string s: ")
goal = input("Enter goal string: ")

if rotateString(s, goal):
    print("true")
else:
    print("false")



##sample input
# Enter string s: abcde
# Enter goal string: cdeab
# #sample output
# true