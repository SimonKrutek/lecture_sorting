import csv
import os
import numpy


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in  reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction = "ascending"):
    """

    :param list number_array: list numeric array
    :param str direction: string indicating sorting directions: ascending ,descending
    :return: sorted numeric array
    """
    n = len(number_array)
    for i in range(n):
        min_max_i = i
        for j in range(i+1 , n):
            if direction == "ascending":
                if number_array[j] < number_array[min_max_i]:
                    min_max_i = j
            elif direction == "descending":
                if number_array[j] > number_array[min_max_i]:
                    min_max_i = j
        number_array[i],number_array[min_max_i] = number_array[min_max_i] , number_array[i]
    return number_array

def bubble_sort(number_array):
    """

    :param list number_array: list with numeric array
    :return: sorted numeric array
    """
    n = len(number_array)
    for i in range(n - 1):
        for ii in range(n - i - 1):
            if number_array[ii] > number_array[ii+1]:
                number_array[ii], number_array[ii+1] = number_array[ii+1], number_array[ii]

    return number_array


def insertion_sort(number_array):
    """

    :param number_array: list with numeric array
    :return: sorted numeric array
    """
    n = len(number_array)
    for i in range(1,n):
        key = number_array[i]
        j = i - 1
        while j >= 0 and number_array[j] > key:
            number_array[j+1] = number_array[j]
            j = j-1
        number_array[j+1] = key
    return number_array



def main():
    data = read_data("numbers.csv")
    print(data)
    sorted_num_arr = selection_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61])
    print(sorted_num_arr)
    sorted_bubble_arr = bubble_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61])
    print(sorted_bubble_arr)
    sorted_insertion = insertion_sort([88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61])
    print(sorted_insertion)
    pass


if __name__ == '__main__':
    main()

