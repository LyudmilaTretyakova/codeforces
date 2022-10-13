if __name__ == "__main__":
    count = int(input())
    listt =[]
    solve=[]
    output=0
    while count>0:
        solve.append( input().split(" "))
       # list.append(solve)
        count-=1
    for i in solve:
        if sum(list(map(int, i)))>=2:
            output+=1
    print(output)