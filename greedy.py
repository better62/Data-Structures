#greedy search
class Graph:
    def __init__(self,size):
        self.adj_list=[[0 for _ in range(size)] for i in range(size)]
        self.size=size
        self.visited=[0]*size #방문 여부 체크하는 리스트
        self.cost=0 #가중치 체크
        
    def give_weight(self,u,v,w):
        self.adj_list[u][v]=w
        self.adj_list[v][u]=w

    def greedy_search(self,u,v): 
        if u==v: 
            return 0
        self.visited[u]=1
        min_value=max(self.adj_list[u])
        min_index=0
        for i in range(u,self.size):
            if self.adj_list[u][i] != 0 and self.visited[i] == 0:
                if min_value>self.adj_list[u][i]:
                    min_value = self.adj_list[u][i]
                    min_index = i
                    self.cost += min_value
        self.greedy_search(min_index, v)
        return self.cost

def main():
    
    graph=Graph(8)
    graph.give_weight(0,1,2)
    graph.give_weight(0,2,3)
    graph.give_weight(1,3,3)
    graph.give_weight(1,4,2)
    graph.give_weight(3,5,1)
    graph.give_weight(3,6,4)
    graph.give_weight(5,7,1)
    graph.give_weight(6,7,3)
    graph.give_weight(2,4,1)
    graph.give_weight(4,6,1)
    graph.give_weight(6,7,3)
    answer=graph.greedy_search(0,7)
    print(answer)
    
main()

'''
answer : 8
'''
