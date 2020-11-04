import random

card = {1:"黑桃1", 2:"黑桃2", 3:"黑桃3", 4:"黑桃4", 5:"黑桃5", 6:"黑桃6", 7:"黑桃7", 8:"黑桃8", 9:"黑桃9", 10:"黑桃10", 11:"黑桃J", 12:"黑桃Q", 13:"黑桃K",
        14:"梅花1", 15:"梅花2", 16:"梅花3", 17:"梅花4", 18:"梅花5", 19:"梅花6", 20:"梅花7", 21:"梅花8", 22:"梅花9", 23:"梅花10", 24:"梅花J", 25:"梅花Q", 26:"梅花K",
        27:"方塊1", 28:"方塊2", 29:"方塊3", 30:"方塊4", 31:"方塊5", 32:"方塊6", 33:"方塊7", 34:"方塊8", 35:"方塊9", 36:"方塊10", 37:"方塊J", 38:"方塊Q", 39:"方塊K",
        40:"愛心1", 41:"愛心2", 42:"愛心3", 43:"愛心4", 44:"愛心5", 45:"愛心6", 46:"愛心7", 47:"愛心8", 48:"愛心9", 49:"愛心10", 50:"愛心J", 51:"愛心Q", 52:"愛心K"}

cardnum = { 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13,
            14:1, 15:2, 16:3, 17:4, 18:5, 19:6, 20:7, 21:8, 22:9, 23:10, 24:11, 25:12, 26:13,
            27:1, 28:2, 29:3, 30:4, 31:5, 32:6, 33:7, 34:8, 35:9, 36:10, 37:11, 38:12, 39:13,
            40:1, 41:2, 42:3, 43:4, 44:5, 45:6, 46:7, 47:8, 48:9, 49:10, 50:11, 51:12, 52:13}

cardcolor = {   1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1,
                14:2, 15:2, 16:2, 17:2, 18:2, 19:2, 20:2, 21:2, 22:2, 23:2, 24:2, 25:2, 26:2,
                27:3, 28:3, 29:3, 30:3, 31:3, 32:3, 33:3, 34:3, 35:3, 36:3, 37:3, 38:3, 39:3,
                40:4, 41:4, 42:4, 43:4, 44:4, 45:4, 46:4, 47:4, 48:4, 49:4, 50:4, 51:4, 52:4}

ans = {     0:"無",
            1:"皇家同花順",
            2:"同花順",
            3:"四條",
            4:"葫蘆",
            5:"同花",
            6:"順子",
            7:"三條",
            8:"兩對",
            9:"對子",
            10:"高牌"}

ccard = [0, 0, 0, 0, 0]
ccardnum = [0, 0, 0, 0, 0]
ccardcolor = [0, 0, 0, 0, 0]

num = 0
mod = 1
ansnum = 0



num = int(random.uniform(1, 52))

for i in range(5):

    if ccard.count(num) != 0:

        num = int(random.uniform(1, 52))

        if ccard.count(num) != 0:

            num = int(random.uniform(1, 52))

            if ccard.count(num) != 0:

                num = int(random.uniform(1, 52))

    ccard[i] = num

ccard = [40, 27, 1, 25, 51]

ccard.sort()

for i in range(5):
    
    ccardcolor[i] = cardcolor[ccard[i]]

for i in range(5):
    
    ccardnum[i] = cardnum[ccard[i]]

ccardnum.sort()

if mod == 1:

    if ((ccardnum.count(1) == 1) and (ccardnum.count(10) == 1) and (ccardnum.count(11) == 1) and (ccardnum.count(12) == 1) and (ccardnum.count(13) == 1)) == 1:

        if ccardcolor.count(1) == 5:

            ansnum = 1

        elif ccardcolor.count(2) == 5:

            ansnum = 1

        elif ccardcolor.count(3) == 5:

            ansnum = 1

        elif ccardcolor.count(4) == 5:

            ansnum = 1

        else:

            mod = 2

    else:

        mod = 2

if mod == 2:

    if ccardcolor.count(1) == 5:

        if (ccardnum[4] - ccardnum[0]) == 4:

            ansnum = 2

        else:
            
            mod = 3

    elif ccardcolor.count(2) == 5:

        if (ccardnum[4] - ccardnum[0]) == 4:

            ansnum = 2

        else:
            
            mod = 3

    elif ccardcolor.count(3) == 5:

        if (ccardnum[4] - ccardnum[0]) == 4:

            ansnum = 2

        else:
            
            mod = 3

    elif ccardcolor.count(4) == 5:

        if (ccardnum[4] - ccardnum[0]) == 4:

            ansnum = 2

        else:
            
            mod = 3

    else:
        
        mod = 3

if mod == 3:

    for k in range(13):
        
        if ccardnum.count(k) == 4:

            ansnum = 3
            continue
        
        else:

            mod = 4

if mod == 4:

    for k in range(13):
        
        if ccardnum.count(k + 1) == 3:

            for a in range(3):

                ccardnum.remove(k + 1)

            for i in range(13):
                
                if ccardnum.count(i + 1) == 2:

                    ansnum = 4

            break
        
        else:
            
            ccardnum = [0, 0, 0, 0, 0]

            for i in range(5):
    
                ccardnum[i] = cardnum[ccard[i]]

            ccardnum.sort()

            mod = 5

if mod == 5:

    for k in range(4):
        
        if ccardcolor.count(k + 1) == 5:

            ansnum = 5
            continue

        else:

            mod = 6

if mod == 6:

    if (ccardnum[4] - ccardnum[0]) == 4:

        ansnum = 6

    else:

        mod = 7

if mod == 7:

    for k in range(13):

        if ccardnum.count(k + 1) == 3:

            ansnum = 7
            continue

        else:

            mod = 8

if mod == 8:

    for k in range(13):

        if ccardnum.count(k + 1) == 2:
                
            for a in range(2):

                ccardnum.remove(k + 1)

            for k in range(13):

                if ccardnum.count(k + 1) == 2:
                    
                    ansnum = 8
                    continue

                else:

                    ccardnum = [0, 0, 0, 0, 0]

                    for i in range(5):
    
                        ccardnum[i] = cardnum[ccard[i]]

                    mod = 9

        else:

            mod = 9

if mod == 9:

    for k in range(13):

        if ccardnum.count(k + 1) == 2:

            ansnum = 9
            continue

        else:

            mod = 10

if mod == 10:

    # if ccardnum.count(1) == 1:

    #     ansnum = 10
    ansnum = 10

for k in range(5):

    print(card[ccard[k]])

print(ans[ansnum])