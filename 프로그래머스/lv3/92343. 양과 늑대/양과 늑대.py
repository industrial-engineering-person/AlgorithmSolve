answer = 0
node = []
tree = []

def solution(info, edges):
    global node, tree
    node = info
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    search({0}, 1)
    return answer

def search(animals, sheep):
    if len(animals) >= 2 * sheep: return
    global answer
    answer = max(answer, sheep)
    
    for animal in animals:
        for child in tree[animal]:
            if child in animals: continue
            animals.add(child)
            if node[child] == 0: search(animals, sheep+1)
            else: search(animals, sheep)
            animals.remove(child)