from random import randint

fout = open('myscore.txt', mode='w')
print('Open file mydata.txt')
scores = []
for n in range(10):
    scores.append(str(randint(1,100)) + '\n')
print('Now, write score to file.')
scoresStr = []
fout.writelines(scores)
fout.close()
print('Now closed file.')