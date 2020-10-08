from numpy.random import randint
from heapsort import heap_sorting
import time
import csv


tests = [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
         2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,
         100000]

with open('algorithm_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['N', 'Tiempo'])
    for test in tests:
        print(f'-------N = {test}-----')
        array = randint(10000, size=test)
        print(f'Original: {array}')
        t_start = time.time()
        heap_sorting(array)
        t_end = time.time()
        print(f'Final: {array}')
        print(f'Duration: {t_end - t_start}\n')

        writer.writerow([test, t_end - t_start])



