import timeit
import random


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
            # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def timesort_sort(arr: list):
    return arr.sort()


def main():
    for i in [1000, 10000, 20000]:
        arr = random.sample(range(i), i)
        insertion_sort_time = timeit.timeit(
            lambda: insertion_sort(arr), number=1)
        merge_sort_time = timeit.timeit(lambda: merge_sort(arr), number=1)
        timesort_sort_time = timeit.timeit(
            lambda: timesort_sort(arr), number=1)

        print(f"========== розмір масиву: {i} ==========")
        print(f"{'insertion_sort':<15} > {insertion_sort_time:<}")
        print(f"{'merge_sort':<15} > {merge_sort_time:<}")
        print(f"{'timesort_sort':<15} > {timesort_sort_time:<}")
        print()


if __name__ == "__main__":
    main()
