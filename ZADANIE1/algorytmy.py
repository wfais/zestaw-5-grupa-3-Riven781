from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3




def merge_sort(array: MonitorowanaTablica, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        q = (left + right) // 2
        merge_sort(array, left, q)
        merge_sort(array, q + 1, right)
        merge(array, left, q, right)





def merge(array: MonitorowanaTablica, left, middle, right):
    """Merges two sorted subarrays."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if array[left1] <= array[left2]:  # mniejsze lub równe
            T[i] = array[left1]
            left1 += 1
        else:
            T[i] = array[left2]
            left2 += 1
        i += 1

    while left1 <= right1:
        T[i] = array[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = array[left2]
        left2 += 1
        i += 1
    for i in range(right - left + 1):
        array[left + i] = T[i]


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if right > left:
        q = partition(array, left, right)
        quick_sort(array,left, q-1)
        quick_sort(array, q+1, right)

def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    pivot = array[right]
    i = left
    j = left
    while i < right:
        if array[i] <= pivot:
            array[i], array[j] = array[j], array[i]
            j+=1
        i+=1
    array[right], array[j] = array[j], array[right]
    return j



def tim_sort(array: MonitorowanaTablica):
    RUN = 32
    n = len(array)

    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort(array, start, end)

    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(array, left, mid, right)

        size *= 2


algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]