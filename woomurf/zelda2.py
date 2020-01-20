import heapq

def zelda(size,problemNumber) :  
    
    # 정점의 정보
    nodes = list() 

    for i in range(size) : 
        tmp = list(map(int,input().split()))
        nodes += tmp
    
    # 우선순위 큐
    queue = list()

    queue.append((nodes[0],0))
    for i in range(1,size*size) : 
        heapq.heappush(queue, (99*size*size,i))
    
    # 각 노드의 최소거리를 저장하는 배열 
    dist = list()
    for i in range(size*size) : 
        dist.append(99*size*size)

    dist[0] = nodes[0]

    while(len(queue) > 0 ) : 
        node = heapq.heappop(queue)[1]
        #print("{} : {}".format(node, dist[node]))
        # 상하좌우 검사합니다. 
        if ( node%size != 0) : 
            if ( dist[node-1] > dist[node] + nodes[node-1]) : 
                dist[node-1] = dist[node] + nodes[node-1]
                heapq.heappush(queue,(dist[node-1],node-1))
        
        if ( node%size != size-1) : 
            if ( dist[node+1] > dist[node] + nodes[node+1]) : 
                dist[node+1] = dist[node] + nodes[node+1]
                heapq.heappush(queue,(dist[node+1],node+1))

        if ( node+size < size*size ) :
            if ( dist[node+size] > dist[node] + nodes[node+size]) : 
                dist[node+size] = dist[node] + nodes[node+size]
                heapq.heappush(queue,(dist[node+size],node+size))
            
        if ( node-size > 0 ) : 
            if ( dist[node-size] > dist[node] + nodes[node-size]) : 
                dist[node-size] = dist[node] + nodes[node-size]
                heapq.heappush(queue,(dist[node-size],node-size))
        

    print("Problem {}: {}".format(problemNumber,dist[size*size-1]))


def main() : 
    problemNumber = 1

    while(True) : 
        size = int(input()) 

        if ( size == 0 ) :
            break
        
        zelda(size,problemNumber)
        problemNumber += 1

main()


        



