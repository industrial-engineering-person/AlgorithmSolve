from collections import defaultdict, deque

def solution(n, path, order):
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    
    for a,b in path:
        adj[a].append(b)
        adj[b].append(a)
    
    parent = defaultdict(int) # 0으로 default, key가 자식, value가 부모
    child = defaultdict(int) # key가 부모, value가 자식
    
    for o in order:
        parent[o[1]] = o[0] # key로 가기전에 value 먼저 가야함
    
    if 0 in parent.keys(): # 0가기전에 어디들러야하면 안됨. 입구는 0뿐!
        return False
    
    # stk = [0] # DFS로 풀어보장, 입구는 항상 0임
    stk = deque([0])
    
    while stk:
        
        curr = stk.popleft()

        if curr in parent.keys() and not visited[parent[curr]]: # nxt부모있는데 부모는 방문안했다면 킵해놔야함. 
            # 부모가 방문할때 같이 처리해놓을거니까 키를 부모로 해놔야 찾기편함.
            
            child[parent[curr]] = curr
            continue #밑에 안하고 넘어감
        
        
        # 부모가 없거나 부모 이미 방문했음 이 아이도 방문 ok
        
        visited[curr] = True
        
        for nxt in adj[curr]:
            if not visited[nxt]:
                stk.append(nxt)
                
        # 자식 있는 경우? 이제 방문해도됨
        
        if curr in child.keys(): 
            stk.append(child[curr])
            
    if False in visited: 
        return False
    else: return True