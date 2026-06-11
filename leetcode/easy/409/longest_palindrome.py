class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars_count = dict()

        for c in s:
            if c not in chars_count:
                chars_count[c] = 1
            else:
                chars_count[c] += 1

        has_odd_count = False
        max_len_palindrome = 0
        for count in chars_count.values():
            max_len_palindrome += 2*(count // 2)
            if not has_odd_count and count % 2 == 1:
                has_odd_count = True
                max_len_palindrome += 1

        return max_len_palindrome

