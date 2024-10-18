def pull(n:int):
    four_stars = 0
    five_stars = 0
    c5 = 0
    c4 = 0
    skip = False
    for i in range(1,n+1):
        if skip:
            skip = False
            continue
        c4+=1
        c5+=1
        if c4 == 10 and c5==90:
                five_stars+=1
                c5 =1
                four_stars+=1
                c4=0
                skip = True
                continue
        if c5==90:
            five_stars+=1
            c5=0
        if c4==10:
            four_stars+=1
            c4=0
    return four_stars,five_stars
print(pull(191))
