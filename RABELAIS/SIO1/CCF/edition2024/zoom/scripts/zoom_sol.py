def f(lst, k):
    result = []
    for i in range(len(lst)):
        for _ in range(k):
            result.append(lst[i])
    return result

def zoom(lst, k):
    result = []
    for i in range(len(lst)):
        for _ in range(k):
            result.append(f(lst[i],k))
    return result

def affiche(lst):
    for i in range(len(lst)):
        for x in lst[i]:
            print("." if x==0 else "*",end=" ")
        print()


img = [[0,0,1],[1,0,0]]
affiche(zoom(img,3))