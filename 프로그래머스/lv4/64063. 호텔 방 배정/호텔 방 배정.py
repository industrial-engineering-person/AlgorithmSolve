def solution(k, room_number):
    roomDict = {}
    roomValDict = {}
    answer = []
    for r in room_number:
        ri = r
        if r in roomDict:
            ri = roomDict[r]                    
        while ri in roomValDict:
            tri = ri
            ri = roomDict[roomValDict[ri]]+1
            roomDict[roomValDict[tri]] = ri
        roomDict[r] = ri
        roomValDict[ri] = r

        answer.append(ri)
    return answer