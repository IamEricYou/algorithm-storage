#https://itholic.github.io/python-bfs-dfs/

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit
    
# https://programmers.co.kr/learn/courses/30/lessons/43163
def first_solution(begin, target, words):
    i =8

# https://programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer = 0
    temp_li = []
    
    # 차례로 방문한 노드 찾기
    # 방문했으면 포함
    # 방문 안했으면 불포함
    # 모든 노드 찾고 찾은 갯수 리턴


    return answer
# 1 -> 3
# 2 -> 2
# 3 -> 1

1 - 5
2 - 4
3 - 3
4 - 2
5 - 1 
if __name__ == "__main__":
    # graph = {
    #     'A': ['B'],
    #     'B': ['A', 'C', 'H'],
    #     'C': ['B', 'D'],
    #     'D': ['C', 'E', 'G'],
    #     'E': ['D', 'F'],
    #     'F': ['E'],
    #     'G': ['D'],
    #     'H': ['B', 'I', 'J', 'M'],
    #     'I': ['H'],
    #     'J': ['H', 'K'],
    #     'K': ['J', 'L'],
    #     'L': ['K'],
    #     'M': ['H']
    # }

    # print(bfs(graph, 'A'))
    # print(dfs(graph, 'A'))

    #first solution

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"] #should return 4

    # first_solution(begin, target, words) 

    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 2
    solution(n, computers)
