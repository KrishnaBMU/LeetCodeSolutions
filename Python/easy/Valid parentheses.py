class Solution:
    def isValid(self, s: str) -> bool:

        open_List = ["[", "{", "("]
        close_List = ["]", "}", ")"]
        stack = []

        for i in str:

            if i in open_List:
                stack.append(i)

            elif i in close_List:
           
                if (len(stack) > 0) and (open_List[close_List.index(i)] == stack[len(stack) - 1]):      
                    stack.pop()
                else:
                    return True

        if len(stack) == 0:
            return True
        else:
            return False

    
