n=int(input())# n সংখ্যক input 
list=[]
for i in range(n):
    cmd = input().split()# split() কাজ হচ্ছে string input কে space এর সাথে divied করা। 
    #cmd ='append 1' after using split() cmd= ['append','1']
    if cmd[0] == 'insert':
        list.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == 'print':
        print(list)
    elif cmd[0] == 'remove':
        list.remove(int(cmd[1]))
    elif cmd[0]== 'append':
        list.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list.sort()
    elif cmd [0] == 'pop':
        list.pop()
    else:
        list.reverse()