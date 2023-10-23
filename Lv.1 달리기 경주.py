#달리기 경주

def solution(players, callings):
    for k in callings:
        ch=players.index(k)
        players[ch-1],players[ch]=players[ch],players[ch-1]
    answer=players
    return answer
#시간초과

 

def solution(players, callings):
    answer = []
    dic_players = {}
    dic_lank = {}
    
    for idx, i in enumerate(players):
        dic_players[i] = idx
        dic_lank[idx] = i
    
    for i in callings:
        cur_idx = dic_players[i]
        
        dic_players[i] = cur_idx - 1
        dic_players[dic_lank[cur_idx-1]] = cur_idx
        
        dic_lank[cur_idx] = dic_lank[cur_idx - 1]
        dic_lank[cur_idx - 1] = i
    
    answer = list(dic_lank.values())
             
    return answer
