import math

def solution(enroll, referral, seller, amount):

    tree=dict(zip(enroll,referral))
    answer=dict(zip(enroll,[0 for _ in range(len(enroll))]))

    for i in range(len(seller)):
        money=amount[i]*100
        get=seller[i]

        while True:
            if money<10:
                answer[get]+=money
                break
            else:
                answer[get]+=math.ceil(money*0.9)
                if tree[get]=="-":
                    break
                else:
                    money=math.floor(money*0.1)
                    get=tree[get]

    return list(answer.values())
