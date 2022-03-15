from prime import *
from time import perf_counter_ns
from plot import Plot
import numpy as np

plot = Plot()

def get_time(data):
    start = perf_counter_ns()
    primes = is_prime(data)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes, finish - start

def get_time_t(data, number_of_threads=5):
    start = perf_counter_ns()
    primes = is_prime_thread(data, number_of_threads)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes, finish - start

def main():
    simple_array = []
    thread_array = []
    thread_60_array = []
    thread_600_array = []

    simple_array_speedup = []
    thread_array_speedup = []
    thread_60_array_speedup = []
    thread_600_array_speedup = []

    with open("dataset/data.csv") as file:
        data = [line.strip() for line in file]
    data = list(map(int, data))

    print('\n\nanalise de %d valores\n\n'%(len(data)))

    for i in range(50):
        tempo1, primo_sp, speed_up_1 = get_time(data)
        tempo2, primo_mt, speed_up_2 = get_time_t(data)
        tempo3, primo_mt, speed_up_60 = get_time_t(data, 60)
        tempo4, primo_mt, speed_up_600 = get_time_t(data, 600)

        simple_array.append(tempo1)
        thread_array.append(tempo2)
        thread_60_array.append(tempo3)
        thread_600_array.append(tempo4)

        simple_array_speedup.append(speed_up_1)
        thread_array_speedup.append(speed_up_2)
        thread_60_array_speedup.append(speed_up_60)
        thread_600_array_speedup.append(speed_up_600)

    media_tempo_s = np.mean(simple_array_speedup)

    plot.plot_bar(np.mean(simple_array), np.mean(thread_array))
    plot.plot_threads(np.mean(thread_array), np.mean(thread_60_array), np.mean(thread_600_array), "Tempo X threads", "Media de tempo")
    plot.plot_threads(media_tempo_s/np.mean(thread_array_speedup), media_tempo_s/np.mean(thread_60_array_speedup), media_tempo_s/np.mean(thread_600_array_speedup), "ApeedUp X threads", "SpeedUp")


if __name__ == '__main__':
    main()