class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def max_heapify(heap, length, i) -> None:
            if i >= len(heap):
                return None

            left = 2*i+1
            right = left + 1
            biggest = i
            if left < length and heap[biggest] < heap[left]:
                biggest = left
            if right < length and heap[biggest] < heap[right]:
                biggest = right
                
            if biggest > i:
                heap[biggest], heap[i] = heap[i], heap[biggest]
                max_heapify(heap, length, biggest)

                
        for i in range((len(nums))//2, -1, -1):
            max_heapify(nums, len(nums), i)

        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(nums, i, 0)

        return nums
