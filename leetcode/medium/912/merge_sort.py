from random import seed, randint
class Solution:
    seed(777)

    def merge(self, head_1: int, tail_1: int, head_2: int, tail_2: int) -> None:
        if head_1 >= head_2:
            return None

        marker_1 = head_1
        marker_2 = head_2
        tmp_arr = []

        while marker_1 <= tail_1 or marker_2 <= tail_2:
            if marker_1 > tail_1:
                tmp_arr.append(self.arr[marker_2])
                marker_2 += 1

            elif marker_2 > tail_2:
                tmp_arr.append(self.arr[marker_1])
                marker_1 += 1

            elif self.arr[marker_1] <= self.arr[marker_2]:
                tmp_arr.append(self.arr[marker_1])
                marker_1 += 1

            elif self.arr[marker_1] > self.arr[marker_2]:
                tmp_arr.append(self.arr[marker_2])
                marker_2 += 1

        for i, val in enumerate(tmp_arr):
            self.arr[head_1+i] = val



    def mergesort(self, head: int, tail: [int]):
        if head >= tail:
            return None

        head_1 = head
        tail_1 = (2*head + tail + 1) // 3
        self.mergesort(head_1, tail_1)

        head_2 = tail_1 + 1
        tail_2 = (2*(tail_1 + 1) + head) // 3
        self.mergesort(head_2, tail_2)

        head_3 = tail_2 + 1
        tail_3 = tail
        self.mergesort(head_3, tail_3)

        self.merge(head_1, tail_1, head_2, tail_2)
        self.merge(head_1, tail_2, head_3, tail_3)


    def sortArray(self, nums: list[int]) -> list[int]:
        self.arr = nums
        self.mergesort(0, len(self.arr)-1)
        return nums
    
    def start(self):
        ls = [5,2,3,1]
        ll = [5,1,1,2,0,0]
        self.sortArray(ls)
        print(self.arr)
        self.sortArray(ll)
        print(self.arr)
