import heapq

def merge_k_lists(unsorted: list):
    [item.sort() for item in unsorted]
    return list(heapq.merge(*unsorted))

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [7, 2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
