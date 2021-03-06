class Solution:
    def romanToInt(self, s: str) -> int:
        num_value = 0
        letter_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        str_len = len(s)
       
        for i in range(str_len):
            if i == str_len - 1:
                num_value += letter_dict[s[i]]
                break
            elif letter_dict[s[i]] < letter_dict[s[i+1]]:
                num_value -= letter_dict[s[i]]
            else:
                num_value += letter_dict[s[i]]
                
        print(num_value)