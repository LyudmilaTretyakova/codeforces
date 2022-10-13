if __name__ == "__main__":
    count = int(input())
    output =[]
    data=[]
    while count>0:
        data.append(input().split(" "))
        count-=1
    for i in data:
        li = list(map(int, i))
        if ((li[0]+li[1]==li[2])or(li[0]+li[2]==li[1])or(li[1]+li[2]==li[0])):
            output.append("YES")
        else:
            output.append("NO")
    print(*output,sep='\n')