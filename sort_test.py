#NAME : SACHINA KOIRALA
#STUDENT ID : 18281333
"""
File name: sort_test.py

Description:
------------
This file implements Insertion and Bubble sort based on the pseudocode.
It then generates multiple random lists, calculate the time of execution for each sorting method, and displays the results.

Requirements:
-----
1. Sorting is done in place , so no new list is returned.
2. To measure the sorting time in nanoseconds, time.perf_counter_ns() is used.
3. Numpy-style docstrings are followed and built-in generics for type hints are used.
"""
#import the necessary libraries
import random,time
import matplotlib.pyplot as plt  

def InsertionSort(A: list[int]) -> None:
    """
    Sorts the list A using the Insertion Sort algorithm

    Parameters
    ----------
    A : list[int]
        The list of integers to sort in place.

    Returns
    -------
    None
        The function sorts the list A in place and does not return anything.
    """
    n: int = len(A)
    for i in range(1, n):
        key: int = A[i]
        j: int = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def BubbleSort(A: list[int]) -> None:
    """
    Sorts the list A in place using the Bubble Sort algorithm.

    Parameters
    ----------
    A : list[int]
        The list of integers to sort in place.

    Returns
    -------
    None
        The function sorts the list A in place and does not return anything.

    """
    n: int = len(A)
    # pseudocode: for i = 1 to n - 1
    # python code: for i in range(n - 1)
    for i in range(n - 1):
        # pseudocode: for j = n downto i + 1
        # python: for j in range(n-1, i, -1)
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                # swap A[j] with A[j - 1]
                A[j], A[j - 1] = A[j - 1], A[j]

# sample list to test correct implementation of pseudocode
    # arr_insertion = [5, 2, 9, 1, 5, 6]
    # arr_bubble = [5, 2, 9, 1, 5, 6]
    # print()
    # InsertionSort(arr_insertion)
    # print("Sorted list using Insertion: ", arr_insertion)
    # BubbleSort(arr_bubble)
    # print("Sorted list using Bubble: ", arr_bubble)


if __name__ == "__main__":
    #Experimentation code
    #create 10 lists of sizes 10,000, 20,000, 30,000, · · · , 100,000
    sizes: list[int] = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    # to store the execution times in nanoseconds
    insertion_times_ns: list[int] = []
    bubble_times_ns: list[int] = []

    # looping through each list size and time the sorts
    for idx, size in enumerate(sizes, start=1):
        # generaye random list of 'size' integers between 1 and 1000
        rand_input: list[int] = [random.randrange(1, 1000, 1) for _ in range(size)]
        
        # Create separate copies for each sort so they work on the same unsorted data
        list_for_insertion: list[int] = rand_input[:]
        list_for_bubble: list[int] = rand_input[:]
        
        # Print the timing results for each list of sizes (in nanoseconds)
        # For InsertionSort
        start_ns: int = time.perf_counter_ns()
        InsertionSort(list_for_insertion)
        end_ns: int = time.perf_counter_ns()
        insertion_time: int = end_ns - start_ns
        insertion_times_ns.append(insertion_time)
        print(f"Execution time for InsertionSort on list {idx} (size {size}): {insertion_time} ns")
        
        # For BubbleSort
        start_ns = time.perf_counter_ns()
        BubbleSort(list_for_bubble)
        end_ns = time.perf_counter_ns()
        bubble_time: int = end_ns - start_ns
        bubble_times_ns.append(bubble_time)
        print(f"Execution time for BubbleSort on list {idx} (size {size}): {bubble_time} ns\n")

# plot the graph of time complexity for insertion and bubble sort
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times_ns, 'o-', label="InsertionSort", linewidth=2, markersize=6)
plt.plot(sizes, bubble_times_ns, 's-', label="BubbleSort", linewidth=2, markersize=6)
plt.xlabel("Input Size")
plt.ylabel("Execution Time (ns)")
plt.title("Time complexity of Insertion and Bubble sort")
plt.legend()
plt.grid(True)
plt.show()