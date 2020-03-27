import random
import math
import matplotlib.pyplot as plt


class Lab3:
    def __init__(self):
        self.N = 1024
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

    def show_spectr(self, Fx):
        """Показує графік функції"""
        x = []
        for i in Fx:
            x.append(i.real)
        plt.plot([i for i in range(self.N)], x, label='Fx', color='gold')
        plt.legend()
        plt.grid(True)
        plt.show()

    def result(self):
        self.show_spectr(self.count_f_x(self.count_x_t()))


Lab3().result()
