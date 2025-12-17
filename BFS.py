with open('input.txt') as f:
    nums = list(map(int, f.read().split()))

if not nums or len(nums) < 3:
    with open('output.txt', 'w') as f:
        f.write('')
    exit()

n, m = nums[0], nums[1]
if len(nums) < 2 + 2 * m + 1:
    with open('output.txt', 'w') as f:
        f.write('Ошибка: недостаточно данных')
    exit()

edges = [(nums[i], nums[i + 1]) for i in range(2, 2 + 2 * m, 2)]
start = nums[2 + 2 * m]
all_vertices = set([start])
for u, v in edges:
    all_vertices.add(u)
    all_vertices.add(v)

min_vertex = min(all_vertices)
max_vertex = max(all_vertices)

if min_vertex == 1:
    graph_size = max_vertex + 1  
    graph = [[] for _ in range(graph_size)]

    for u, v in edges:
        if 1 <= u <= max_vertex and 1 <= v <= max_vertex:
            graph[u].append(v)
            graph[v].append(u)
    if start < 1 or start > max_vertex:
        print(f"Ошибка: стартовая вершина {start} не существует")
        exit()

    for i in range(min_vertex, n+min_vertex):
        graph[i].sort()

    visited = [False] * graph_size
    visited[start] = True

else:
    graph_size = n
    graph = [[] for _ in range(n)]

    for u, v in edges:
        if 0 <= u < n and 0 <= v < n:
            graph[u].append(v)
            graph[v].append(u)

    for i in range(min_vertex, n+min_vertex):
        graph[i].sort()


    if start < 0 or start >= n:
        print(f"Ошибка: стартовая вершина {start} не существует")
        exit()

    visited = [False] * n
    visited[start] = True

queue = [start]
front = 0
result = []

while front < len(queue):
    current = queue[front]
    front += 1
    result.append(current)

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
    result_str=''
    for i in range(len(result)):
        if i > 0:
            result_str += " "
        result_str += str(result[i])


print("Порядок обхода BFS:")
print(result_str)
with open('output.txt', 'w') as f:

    f.write(result_str)
