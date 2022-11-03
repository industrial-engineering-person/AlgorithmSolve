from itertools import combinations, permutations

def check(user, ban):
    if len(user) != len(ban): return False
    else:
        for idx in range(len(ban)):
            if ban[idx] == "*": continue
            else:
                if user[idx] == ban[idx]: continue
                else: return False
    return True

def solution(user_id, banned_id):
    # 제재 아이디 목록 경우의 수
    result = []
    combi = list(permutations(user_id, len(banned_id)))
    for tup in combi:
        tup = list(tup)
        tmp = 0
        for idx in range(len(tup)):
            # print(tup[idx],banned_id[idx])
            if check(tup[idx],banned_id[idx]):
                tmp += 1
        if tmp == len(banned_id):
            tup.sort()
            if tup not in result:
                result.append(tup)

    return len(result)