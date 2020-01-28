import sys

sys.setrecursionlimit(40000) # 파이썬이 기본적으로 많은 수의 재귀를 허용하지 않는다. 
                             # 이를 위해서 재귀 한계를 재설정해준다. 

dp = []

def greedyPanda() :
    global dp

    map_size = int(input())

    forest = list()
    for i in range(map_size) : 
        tmp = list(map(int,input().split()))
        forest += tmp
    
    dp = [0 for i in range(map_size*map_size)] 

    for i in range(map_size*map_size) : 
        dp[i] = dfs(i,map_size,forest)
    
    result = max(dp)
    print(result)


def dfs(n,size,forest):

    if dp[n] != 0:
        return dp[n]

    dp[n] = 1

    # upside 
    if n+size < size*size :
        if forest[n+size] > forest[n] : 
            dp[n] = max(dp[n],dfs(n+size,size,forest)+1)
    # downside 
    if n-size > -1  :
        if forest[n-size] > forest[n] :
            dp[n] = max(dp[n],dfs(n-size,size,forest)+1)

    # leftside 
    if n%size != 0 :
        if forest[n-1] > forest[n] :
            dp[n] = max(dp[n],dfs(n-1,size,forest)+1)
    
    # rightside
    if n%size != size-1 :
        if forest[n+1] > forest[n] :
            dp[n] = max(dp[n],dfs(n+1,size,forest)+1)
    
    return dp[n]

greedyPanda()