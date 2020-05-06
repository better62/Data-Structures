def BFS(graph,start_node):
    visit=list()
    queue=list()

    queue.append(start_node)

    while queue:
        vertex = queue.pop(0)
        if vertex not in visit:
            visit.append(vertex)
            for i in graph[vertex]:
                if i not in visit:
                    queue.append(i)
        else:
            pass
    
    return visit
    
graph={'A':['B'],'B':['A','C','H'],'C':['B','D'],'D':['C','E','G'],'E':['D','F'],
'F':['E'],'G':['D'],'H':['B','I','J','M'],'I':['H'],'J':['H','K'],'M':['H'],
'K':['J','L'],'L':['K']}

print(BFS(graph,'A'))
