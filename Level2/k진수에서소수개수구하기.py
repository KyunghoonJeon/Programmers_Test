import math

def makeprime(n, q): # k 진법으로 바꾸는 함수
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def primenumber(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x))+1):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True

def solution(n, k):
    answer = 0
    n=makeprime(n,k)
    n=n.split('0')
    l=[]
    for i in n:
        if len(i)>0:
            l.append(i)
    for i in l:
        if primenumber(int(i)):
            answer+=1
    return answer

print(solution(36,3))