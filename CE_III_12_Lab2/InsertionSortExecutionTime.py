

import random
import time
from InsertionSort import insertion_sort
from CommonPlot import plot_sorting_algorithm

def insertion_sort_time():

    #Create empty dictionary
    execution_time = {}

    for i in range(800,88888,800):
        
        try:
            unsorted_array = sorted(random.sample(range(i), i))
        except ValueError:
            print("Sample is larger  Or Negative")
            
        start_time = time.time()
        sorted_array = insertion_sort(unsorted_array)
        end_time = time.time()
        
        #Input size and its corresponding execution time is added to dictionary
        execution_time[i] = end_time - start_time
        
    print(execution_time)
    plot_sorting_algorithm(execution_time)
    
if __name__ == "__main__":
    insertion_sort_time()
    
