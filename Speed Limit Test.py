# cook your dish here
for i in range(int(input())):
    a,x,b,y = map(int,input().split())
    alice = a/x 
    bob = b/y  
    if alice > bob:
        print('ALICE')
    elif alice < bob:
        print('BOB')
    else:
        print('EQUAL')
