from random import seed, randint
class Solution:
    seed(777)

    def partition(self, arr: list[int], head: int, tail: [int]) -> int:
        smaller = []
        bigger = []
        pivot_index = randint(head, tail)
        pivot = arr[pivot_index]

        tmp = arr[tail]
        arr[tail] = pivot
        arr[pivot_index] = tmp
        pivot_index = tail

        for i in range(tail - 1, head - 1, -1):
            if arr[i] >= pivot:
                tmp = arr[i]

                for u in range(i, pivot_index, 1):
                    arr[u] = arr[u+1]

                arr[pivot_index] = tmp
                pivot_index -= 1

        return pivot_index


    def quicksort(self, arr: list[int], head: int, tail: [int]) -> None:
        if head >= tail:
            return None

        pivot = self.partition(arr, head, tail)
        self.quicksort(arr, head, pivot-1)
        self.quicksort(arr, pivot+1, tail)


    def sortArray(self, nums: list[int]) -> list[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def start(self):
        ls = [5,2,3,1]
        ll = [5,1,1,2,0,0]
        self.sortArray(ls)
        self.sortArray(ll)
        print(ls)
        print(ll)
