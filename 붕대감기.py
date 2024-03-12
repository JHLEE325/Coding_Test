def solution(bandage, health, attacks):
    answer = 0
    time = 0
    currhealth = health
    count = 0
    for i in attacks:
        time = i[0]

    att = 0
    for i in range(1, time+1):
        if attacks[att][0]==i:
            print('attack')
            currhealth -= attacks[att][1]
            if currhealth <= 0:
                answer = -1
                return answer
            count = 0
            att+=1
            answer=currhealth
            continue
        
        currhealth += bandage[1]
        count += 1

        if count == bandage[0]:
            count = 0
            currhealth += bandage[2]


        if currhealth>=health:
            currhealth = health

        answer = currhealth
        print(answer)
        
    return answer

bandage=[5, 1, 5]
health=30
attacks=[[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(bandage, health, attacks))