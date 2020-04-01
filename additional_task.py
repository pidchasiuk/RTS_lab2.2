import random
import math
import numpy.fft as np
from time import time


class Lab3:
    def __init__(self):
        self.N = int(math.pow(2, 12))
        self.w = 1200
        self.n = 8
        self.t = [i for i in range(self.N)]
        self.pi = math.pi

    def count_sin(self):
        """Розрахунок n сигналів"""
        res = []
        for i in range(self.n):
            A = random.random()
            fi = random.random() * 6.28
            res_i = [A * math.sin(self.w * self.t[i] * i + fi) for i in range(self.N)]
            res.append(res_i)
        return res

    def count_x_t(self):
        """Розрахунок випадкового сигналу"""
        res = self.count_sin()
        x_t = []
        for i in range(self.N):
            x = 0
            for j in range(self.n):
                x += res[j][i]
            x_t.append(x)
        return x_t

    def count_f_x(self, x_t):
        """Розрахунок ФФТ"""
        len_xt = len(x_t)
        if len_xt <= 1: return x_t
        even = self.count_f_x(x_t[0::2])
        odd = self.count_f_x(x_t[1::2])
        t = [complex(math.cos(-2 * self.pi * i / len(x_t)), math.sin(-2 * self.pi * i / len(x_t))) * odd[i] for
             i in range(len_xt // 2)]
        return [even[i] + t[i] for i in range(len_xt // 2)] + [even[i] - t[i] for i in range(len_xt // 2)]


    def result(self):
        x_t = self.count_x_t()
        time_start1 = time()
        self.count_f_x(x_t)
        time_end1 = time()
        time_res1 = time_end1-time_start1

        time_start2 = time()
        np.fft(x_t)
        time_end2 = time()
        time_res2 = time_end2 - time_start2

        print("Розрахунок по формулі з методички:", time_res1)
        print("Розрахунок по вбудованій формулі:", time_res2)



Lab3().result()
