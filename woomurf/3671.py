import math

def spy(prime) :
    num = input()

    num_list = list()

    for i in range(len(num)):
        num_list.append(num[i])
    
    selected = [False for i in range(len(num_list))]
    perm = list()
    answer = set()

    answer = dfs(0, num_list, selected, perm, prime, answer)

    print(len(answer))



def dfs(count, num_list, selected, perm, prime, answer) : 
    length = len(num_list)

    if count > length:
        return answer
    
    sum = 0
    for i in range(len(perm)) : 
        sum += int(perm[i])

        if i != len(perm)-1 : 
            sum *= 10
    #print("sum : {}".format(sum))

    # if prime[sum] != 0:
    #     answer += 1
    #     prime[sum] = 0
    #     #print("prime sum : {}".format(sum))
    check = True
    for i in range(2,int(math.sqrt(sum))+1) : 
        #print("i : {}".format(i))
        if sum%i == 0 :
            check = False
            break
    
    if check and sum != 0 and sum != 1: 
        answer.add(sum)

    for i in range(length) : 
        if selected[i] == True:
            continue
            
        perm.append(num_list[i])
        selected[i] = True
        answer = dfs(count+1, num_list, selected, perm, prime, answer)
        perm.pop()
        selected[i] = False

    return answer 

def get_prime():
    prime = [1 for i in range(10000000)]

    for i in range(2,int(math.sqrt(10000000))) : 
        if prime[i] == 0:
            continue
        
        for j in range(i+i,10000000,i):
            prime[j] = 0
    
    prime[0] = 0
    prime[1] = 0

    return prime


def main() : 
#    p = get_prime()

    testCase = int(input())

    for i in range(testCase) :
        prime = []
        spy(prime)

main()