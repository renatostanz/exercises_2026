class Solution:
    def get_letters(self, digit: str):
        if digit == '2':
            return ['a', 'b', 'c']
        if digit == '3':
            return ['d', 'e', 'f']
        if digit == '4':
            return ['g', 'h', 'i']
        if digit == '5':
            return ['j', 'k', 'l']
        if digit == '6':
            return ['m', 'n', 'o']
        if digit == '7':
            return ['p', 'q', 'r', 's']
        if digit == '8':
            return ['t', 'u', 'v']
        if digit == '9':
            return ['w', 'x', 'y', 'z']


    def generate_combinations(self, letters_sets: list[str]):
        combinations = letters_sets[0]
        for i, letters in enumerate(letters_sets):
            if i == 0:
                continue
            new_combinations = []
            for c in combinations:
                for l in letters:
                    new_combinations.append(c+l)
            combinations = new_combinations

        return combinations


    def letterCombinations(self, digits: str) -> list[str]:
        letters_sets = []
        for i, d in enumerate(digits):
            letters_sets.append(
                self.get_letters(d)
            )

        return self.generate_combinations(letters_sets)

