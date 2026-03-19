if __name__ == '__main__':
    N = int(input())
    
lst = []
for i in range(N):
    inp = input().split()
    if(inp[0] == "insert"):
        lst.insert(int(inp[1]), int(inp[2])) 
    elif(inp[0] == "append"):
        lst.append(int(inp[1]))
    elif(inp[0] == "remove"):
        lst.remove(int(inp[1]))
    elif(inp[0] == "sort"):
        lst.sort()
    elif(inp[0] == "pop"):
        lst.pop(len(lst) - 1)
    elif(inp[0] == "reverse"):
        lst.reverse()
    elif(inp[0] == "print"):
        print(lst)
        
