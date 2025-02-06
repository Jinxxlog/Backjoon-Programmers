def solution(picks, minerals):
    tired = {"diamond" : 25, "iron" : 5, "stone" : 1}
    values = []
    valuesum = 0
    cnt = 0
    dcnt = 0
    mcnt = 0
    
    minerals = minerals[:sum(picks) * 5]
    
    
    for i in minerals:
        valuesum += tired[i]
        cnt += 1
        if i == 'diamond':
            dcnt += 1
        else:
            mcnt += 1
            
        if cnt == 5:
            values.append([valuesum, dcnt, mcnt])
            valuesum = 0
            cnt = 0
            dcnt = 0
            mcnt = 0

    if cnt != 0:
        values.append([valuesum, dcnt, mcnt])
        
    values.sort(reverse=True, key = lambda x:x[0])
    res = 0
        
    for i in range (len(values)):
        if picks[0] > 0:
            res += values[i][1] + values[i][2]
            picks[0] -= 1

        elif picks[1] > 0:
            res += values[i][1]*5 + values[i][2]
            picks[1] -= 1

        elif picks[2] > 0: 
            res += values[i][0]
            picks[2] -= 1
            
        else:
            continue
        
    return res