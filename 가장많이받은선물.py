def solution(friends, gifts):
    answer = 0
    giver_d = dict()
    receiver_d = dict()
    gift_d = dict()
    answer_d = dict()

    for i in friends:
        inner = dict()
        for j in friends:
            if i == j:
                continue
            inner[j]=0
        gift_d[i]=inner
        answer_d[i]=0
        giver_d[i]=0
        receiver_d[i]=0

    for i in gifts:
        giver, receiver = i.split()
        gift_d[giver][receiver]+=1
        giver_d[giver]+=1
        receiver_d[receiver]+=1

    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            a = friends[i]
            b = friends[j]

            acount = gift_d[a][b]
            bcount = gift_d[b][a]

            if acount>bcount:
                answer_d[a]+=1
            elif acount<bcount:
                answer_d[b]+=1
            else:
                aval = giver_d[a]-receiver_d[a]
                bval = giver_d[b]-receiver_d[b]
                if aval>bval:
                    answer_d[a]+=1
                elif aval<bval:
                    answer_d[b]+=1
    
    answer = max(answer_d.values())

    return answer

friends1 = ["muzi", "ryan", "frodo", "neo"]
gifts1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends1, gifts1))