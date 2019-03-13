import math


def GenerationSumSin():
    T = int(input("Введите количество периодов - "))
    N = int(input("Введите количество точек - "))
    file = open("sin.txt", "w")
    for i in range(N):
        S = math.sin(2 * math.pi * (i * N / T))
        file.write(str(i)+"  "+str(S)+"\n")
    file.close()
GenerationSumSin()
        

