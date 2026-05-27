class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        string_arr = []
        new_string = ""

        for char in s:
            string_arr.append(char)
        
        left = 0
        right = len(string_arr) - 1

        while left < right:

            left_char = string_arr[left]
            right_char = string_arr[right]

            if left_char.isalpha() and right_char.isalpha():
                temp = left_char
                string_arr[left] = right_char
                string_arr[right] = temp                

                left += 1
                right -= 1
            elif not right_char.isalpha() and not left_char.isalpha():
                left += 1
                right -= 1
            else:
                if not left_char.isalpha() and right_char.isalpha():
                    left += 1
                if not right_char.isalpha() and left_char.isalpha():
                    right -=1

        
        for char in string_arr:
            new_string += char

        return new_string


        