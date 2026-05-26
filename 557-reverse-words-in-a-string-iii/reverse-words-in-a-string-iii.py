class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        last_space_index = -1

        for str_index in range(len(s)):
            if str_index == len(s) - 1 or s[str_index] == ' ':
                if str_index == len(s) - 1:
                    reverse_str_index = str_index
                else:
                    reverse_str_index = str_index - 1
                while reverse_str_index > last_space_index:
                    result.append(s[reverse_str_index])
                    reverse_str_index -= 1
                if str_index != len(s) - 1:
                    result.append(' ')
                last_space_index = str_index

        return ''.join(result)