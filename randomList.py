import random

def randomList(n):
    iList =[]
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList

if __name__ == "__main__":
    ilist = randomList(10)
    print(ilist)
