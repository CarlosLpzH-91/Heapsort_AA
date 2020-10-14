"""
Test the execution time of the HeapSort algorithm.

This program was created with academic purposes as an assaigment for the "Análisis de Algoritmos" curse
of MIA, UV.

Created on 09/10/2020 by Carlos A. López Herrera.
"""


from numpy.random import randint
from heapsort import heap_sorting
import time
import csv

# 10 test of different array's size
tests = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

# Create and open a new csv file to register the time measures of the execution of the program.
with open('time_measures.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # write the headers.
    writer.writerow(['N', 'Tiempo'])
    # Iterate the tests
    for test in tests:
        # Initialize a array of random integers from 0 to 10,000 of the correspondent size.
        array = randint(10000, size=test)
        # Get the initial time.
        t_start = time.time()
        heap_sorting(array)
        # Get the final time.
        t_end = time.time()

        # Write the array's size and the execution time on the next row.
        writer.writerow([test, t_end - t_start])



