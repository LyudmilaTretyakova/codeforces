if __name__ == "__main__":
    input = input().split(" ")
    inputint=list(map(int, input))
    solve1=0
    solve2 = 0
    solve = 0
    #solve1 = (inputint[0]//inputint[2])*(inputint[1]//inputint[2])
    if inputint[0]%inputint[2]!=0:
        solve1=(inputint[0] // inputint[2])+1
    else:
        solve1 = (inputint[0] // inputint[2])
    if inputint[1]%inputint[2]!=0:
        solve2=(inputint[1] // inputint[2])+1
    else:
        solve2 = (inputint[1] // inputint[2])
    solve = solve1*solve2
    print(solve)