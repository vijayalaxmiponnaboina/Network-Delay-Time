import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj=[]
        for i in range(n+1):
            adj.append([])
        for edge in times:
            u=edge[0]
            v=edge[1]
            w=edge[2]
            adj[u].append([v,w])

        dist=[float('inf')]*(n+1)
        dist[k]=0
        min_heap=[(0,k)]
        while min_heap:
            curr_dist,node=heapq.heappop(min_heap)
            
            if curr_dist > dist[node]:
                continue
            for ne,we in adj[node]:
                new_dist=curr_dist+we
                if new_dist < dist[ne]:
                    dist[ne]=new_dist
                    heapq.heappush(min_heap,(new_dist,ne))
        for i in range(1,n+1):
            if dist[i] == float('inf'):
                return -1
        return max(dist[1:]) 