#depth first search

adj_list=[[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]

n=len(adj_list)
visited=[False]*n

def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in adj_list[v]:
      if not visited[i]:
        dfs(i)

print('DFS 방문 순서 : ')
dfs(0)
