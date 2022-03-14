from prime import *
from time import perf_counter_ns
from plot import Plot
import numpy as np

plot = Plot()

def get_time(data):
    start = perf_counter_ns()
    primes = is_prime(data)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes

def get_time_t(data, number_of_threads=5):
    start = perf_counter_ns()
    primes = is_prime_thread(data, number_of_threads)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes

def main():
    simple_array = []
    thread_array = []
    thread_20_array = []
    thread_60_array = []

    with open("dataset/data.csv") as file:
        data = [line.strip() for line in file]
    data = list(map(int, data))

    print('\n\nanalise de %d valores\n\n'%(len(data)))

    for i in range(50):
        tempo1, primo_sp = get_time(data)

        tempo2, primo_mt = get_time_t(data)

        simple_array.append(tempo1)
        thread_array.append(tempo2)

        tempo3, primo_mt = get_time_t(data, 20)
        tempo4, primo_mt = get_time_t(data, 60)

        thread_20_array.append(tempo3)
        thread_60_array.append(tempo4)

    plot.plot_bar(np.mean(simple_array), np.mean(tempo2))
    plot.plot_threads(np.mean(thread_array), np.mean(thread_20_array), np.mean(thread_60_array))


if __name__ == '__main__':
    main()