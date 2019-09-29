def solution(number):
    l=[]
    x=3
    while x<number:
        if x%3==0 or x%5==0:
            l.append(x)
        x+=1
    return sum(l)


