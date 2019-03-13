from math import sin, cos, pi, sqrt
import csv
from itertools import zip_longest
from scipy.signal import cwt
import numpy.fft as FustFurieTranformation


class Function:
    def GenerationSumSin(self, T, N):
     
        self.__array = []
        for t in range(1024):
            S = sin(2 * pi * (t * T / N)) + 0.5*sin(2 * pi * (t * 10 * T / N))
            self.__array.append(S)
        return self.__array

    def GenerateSumSinTeta(self):

        self.__array = []
        for t in range(0, 1024):
            if t - 512 < 0:
                teta = 0
                fun = sin(2 * pi * (t / 512))
            elif t - 512 > 0:
                teta = 1
                fun = teta * sin(2 * pi * (5 * t / 512))
            self.__array.append(fun)
        return self.__array

class AddToTXT(Function):
    def make_txt(self, file_name, array):
        file = open(file_name, "w")
        for i in range(0, len(array)):
            file.write(str(i)+"  "+str(array[i])+"\n")
        file.close()
    def make_special_txt(self, file_name, Rezult):
        export_data = zip_longest(*Rezult, fillvalue="")
        with open(file_name, "w", newline="") as myfile:
            wr = csv.writer(myfile, delimiter = " ")
            wr.writerows(export_data)
        myfile.close()
    def make_furie_txt(self, file_name_furie, furie_array):
        file = open(file_name_furie, "w")
        for i in range(0, len(furie_array)):
            file.write(str(i)+"  "+str(array[i])+"\n")
        file.close()

class MakeFurie(Function):

    def FFT(self, array): 
        ft = FustFurieTranformation.fft(array)
        return ft


class MakeWeivlets(Function):

    def Weivlet(self, array):
        count = 0
        C = []
        A = []
        B = []
        Rezult = []
        Rezult.append(array)
        while len(array) != 1: 
            for i in range(0, len(array) - 1, 2):
                c = 1 / sqrt(2) * (array[i] + array[i+1]) 
                C.append(c)
                A.append(c)
            count = count + 1
            array = A
            for i in range(len(C)):
                for j in range(2**count):
                    B.append(C[i])
            C = B
            Rezult.append(C)
            C = []
            B = []
            A = []
        return Rezult


obj = AddToTXT()
obj_furie = MakeFurie()
choose = int(input("""Пожалуйста выберите функцию: 
       1. Сумма синусов
       2. Сумма синусов с тетой 
        - """))
if choose == 1:
    N = int(input("Введите количество точек - ")) 
    T = int(input("Введите количество периодов - "))
    file_name = str(input("Введите название файла: ")+".txt")
    array = obj.GenerationSumSin(T, N)
    file_name_furie = str(input("Введите название файла для разложения Фурье: ")+".txt")
    furie_array = obj_furie.FFT(array)
elif choose == 2:
    file_name = str(input("Введите название файла: ")+".txt")
    array = obj.GenerateSumSinTeta()
    file_name_furie = str(input("Введите название файла для разложения Фурье: ")+".txt")
    furie_array = obj_furie.FFT(array)
obj.make_txt(file_name, array)
obj.make_furie_txt(file_name_furie, furie_array)
waivlets_obj = MakeWeivlets()
file_name = str(input("Введите название файла вейвлет преобразования: ")+".txt")
Rezult = waivlets_obj.Weivlet(array)
obj.make_special_txt(file_name, Rezult)



