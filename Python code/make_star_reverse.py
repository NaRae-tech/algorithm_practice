T = int(input())
for i in range(1, T+1):
    for j in range (0,T-i):
        print(' ', end='')
    for k in range(0,i):
        print('*',end='')
    print('', end='\n')