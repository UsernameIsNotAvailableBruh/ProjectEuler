Reverser = lambda x: x[::-1]

def idk():
    biggestPalindrome = []
    for x in range(999, 500, -1):
        for y in range(999, 500, -1):
            if (str(x*y) == Reverser(str(x*y))):
                biggestPalindrome.append(x*y)
                break
    return str(max(biggestPalindrome))

print(idk())
