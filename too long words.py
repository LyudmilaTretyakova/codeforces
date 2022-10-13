

def long(data):
    if len(data)<=10:
        return data
    else:
        return data[0]+str(len(data)-2)+data[-1]


if __name__ == "__main__":
    count = int(input())
    output =[]
    data=[]
    while count>0:
        data.append( str(input()))
       #
        count-=1
    for i in data:
        output.append(long(i))
    print(*output,sep='\n')