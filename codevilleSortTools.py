class ListSorter:
    @staticmethod
    def sort(array):
        resultList = array
        ListSorter.quicksort(resultList, 0, len(resultList) - 1)
        return resultList

    @staticmethod
    def quicksort(array, low, high):
        if low < high:
            pi = ListSorter.partition(array, low, high)

            ListSorter.quicksort(array, low, pi - 1)
            ListSorter.quicksort(array, pi + 1, high)

    @staticmethod
    def partition(array, low, high):
        i = (low - 1)  # index of smaller element
        pivot = array[high]  # pivot

        for j in range(low, high):

            if array[j].score >= pivot.score:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1