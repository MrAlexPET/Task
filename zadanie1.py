import math

N = 10
M = 5
H = 25

f = open('input.txt', 'w')
f.write(str(N) + '\n')
f.write(str(M) + '\n')
f.write(str(H) + '\n')
f.close()
if (1 <= N <= H <= 100) and (1 <= M <= 100):
    R = math.ceil(M/(math.floor(H/N)))
    f1 = open('output.txt', 'w')
    f1.write(str(R))
    f1.close()
else:
    f1 = open('output.txt', 'w')
    f1.write('У вас не получится построить частокол(')
    f1.close()