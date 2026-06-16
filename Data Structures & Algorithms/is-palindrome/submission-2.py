class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_first=s.lower()
        cleaned_string="".join(char for char in lower_first if char.isalnum())
        new_string=cleaned_string.replace(" ", "")
        print(new_string)
        new_reversed = new_string[::-1]
        if new_string == new_reversed:
            return True
        else:
            return False
            