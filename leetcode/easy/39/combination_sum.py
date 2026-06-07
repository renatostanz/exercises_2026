class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combinations = []
        def generate_combinations(partial_combination: list[int], candidates_marker: int = 0, sum_: int = 0) -> None:
            if sum_ == target:
                return combinations.append(partial_combination)
            elif sum_ > target:
                return None

            for i, c in enumerate(candidates[candidates_marker:]):
                new_marker = i + candidates_marker
                generate_combinations(partial_combination + [c], new_marker, sum_ + c)

        generate_combinations([])
        return combinations

