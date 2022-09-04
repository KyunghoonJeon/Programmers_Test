def solution(n):
    arr=[[0]*i for i in range(1,n+1)]
    x,y=-1,0
    start=1
    for dir in range(n):
        for j in range(dir,n):
            if dir%3==0:
                x+=1
            elif dir%3==1:
                y+=1
            else:
                x-=1;y-=1
            arr[x][y]=start
            start+=1
    answer=sum(arr,[])
    return answer
