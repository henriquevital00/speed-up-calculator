import matplotlib.pyplot as plt
import numpy as np

class Plot():
    def plot_bar(self, simple_method_quantity, thread_quantity):
        legend = ['sem thread', 'Thread']
        pos = np.arange(len(legend))
        print('pos' + str(pos))
        plt.ylabel('Media de tempo')
        plt.title('Quantidade de números primos encontrados')
        size_s = [simple_method_quantity]
        size_t = [thread_quantity]
        plt.bar(0, size_s, color='yellow', edgecolor='black')
        plt.bar(1, size_t, color='blue', edgecolor='black')
        plt.xticks(pos, legend)
        plt.legend(legend, loc=2)
        plt.show()

    def plot_threads(self, *args):
        legend = ['5 Threads', '20 Thread', '60 Threads']
        pos = np.arange(len(legend))
        print('pos' + str(pos))
        plt.ylabel('Media de tempo')
        plt.xlabel('Numero de threads')
        plt.title('Tempo X threads')
        plt.bar(0, args[0], color='yellow', edgecolor='black')
        plt.bar(1, args[1], color='blue', edgecolor='black')
        plt.bar(2, args[2], color='red', edgecolor='black')
        plt.xticks(pos, legend)
        plt.legend(legend, loc=2)
        plt.show()
