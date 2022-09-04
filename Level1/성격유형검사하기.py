def solution(survey, choices):
    name_list=['A','N','C','F','M','J','R','T']
    scores=dict(zip(name_list,[0 for i in range(len(name_list))]))
    for idx,choice in enumerate(choices):
        if choice - 4 > 0:
            scores[survey[idx][1]] += choice-4
        elif choice - 4 < 0:
            scores[survey[idx][0]] += 4-choice

    answer = ''

    if scores['R']>=scores['T']:
        type+='R'
    else:
        type+='T'

    if scores['C']>=scores['F']:
        type+='C'
    else:
        type+='F'

    if scores['J']>=scores['M']:
        type+='J'
    else:
        type+='M'

    if scores['A']>=scores['N']:
        type+='A'
    else:
        type+='N'

    return answer