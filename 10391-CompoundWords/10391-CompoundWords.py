from sys import stdin


def main():
    word = stdin.readline().strip()
    words = []
    frecu = {}
    reps = []
    
    while word:
        if not (word in frecu):
            frecu[word] = 1
            words.append(word)
        
        
        word = stdin.readline().strip()

        for i in range(len(words)):
            for j in range(i,len(words)):
                word1 = words[i]
                word2 = words[j]
                if (word1 + word2) in frecu and frecu[word1 + word2] == 1:
                    reps.append(word1+word2)
                    frecu[word1 + word2] += 1
                elif(word2+word1) in frecu and frecu[word2 + word1] == 1:
                    reps.append(word2+word1)
                    frecu[word2 + word1] += 1
    reps.sort()
    for i in reps:
        print(i)
    
main()
