class Solution:
    def get_permutations(self, used_nums: list[bool], used_nums_count: int, permutations: list[list[int]]):
        if len(self.nums) == used_nums_count:
            return permutations

        new_permutations = []
        for p in permutations:
            for i, n in enumerate(self.nums):
                if used_nums[i]:
                    continue

                used_nums[i] = True

                tmp_permutations = self.get_permutations(used_nums[:], used_nums_count+1, [p+[n]])
                for new_p in tmp_permutations[:]:
                    new_permutations.append(new_p)

                used_nums[i] = False

        return new_permutations


    def permute(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums

        used_nums = [False for u in range(len(nums))]
        permutations = []
        for i, n in enumerate(self.nums):
            used_nums[i] = True
            permutations += self.get_permutations(used_nums[:], 1, [[n]])
            used_nums[i] = False
        return permutations
