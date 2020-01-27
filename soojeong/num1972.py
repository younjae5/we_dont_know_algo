def surprising_str(str_sup):
    if len(str_sup) == 1:
        print('{} is surprising.'.format(str_sup))
        return 
    for i in range(len(str_sup)-1):
        c_list = []
        state = False
        for j in range(len(str_sup)-1-i):
            a = [str_sup[j], str_sup[j+1+i]]
            if a in c_list:
                state = True
                # print('{} is NOT surprising.'.format(str_sup))
                break
            else:
                c_list.append(a)
        if state == True:
            break
    if state == True:
        print('{} is NOT surprising.'.format(str_sup))
    else:
        print('{} is surprising.'.format(str_sup))


for i in range(101):
    is_sup = str(input())
    if is_sup == '*':
        break
    else:
        # function call
        surprising_str(is_sup)

