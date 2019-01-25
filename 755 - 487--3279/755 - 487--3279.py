from sys import stdin


dic = {}
dic["A"] = 2
dic["B"] = 2
dic["C"] = 2
dic["D"] = 3
dic["E"] = 3
dic["F"] = 3
dic["G"] = 4
dic["H"] = 4
dic["I"] = 4
dic["J"] = 5
dic["K"] = 5
dic["L"] = 5
dic["M"] = 6
dic["N"] = 6
dic["O"] = 6
dic["P"] = 7
dic["R"] = 7
dic["S"] = 7
dic["T"] = 8
dic["U"] = 8
dic["V"] = 8
dic["W"] = 9
dic["X"] = 9
dic["Y"] = 9


def main():
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        frecu = {}
        res = []
        blank = stdin.readline()
        nums = int(stdin.readline().strip())
        for n in range(nums):
            sNum = ""
            num = stdin.readline().strip()
            for i in range(len(num)):
                asc = ord(num[i])
                if (asc >= 48 and asc <= 57 ):
                    sNum += num[i]
                elif (asc >= 65 and asc <= 90 ):
                    sNum += str(dic[num[i]])
            #print(sNum)
            if sNum in frecu:
                frecu[sNum] += 1
                if frecu[sNum] == 2:
                    res.append(sNum)
                    
            else:
                frecu[sNum] = 1

        res.sort()
        if res:
            for i in range(len(res)):
                num = res[i]
                print(num[:3]+"-"+num[3:],frecu[num])
        else:
            print("No duplicates.")
            
        if ca != cases-1:
            print()
                    

            

main()
