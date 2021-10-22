class Solution:
    def segregate(self,s):
        l = []
        item = ''
        for char in s:
            if char.isspace():
                if item != '':
                    l.append(int(item))
                    item = ''
            if char in ["(",")","+","-"]:
                if item != '':
                    l.append(int(item))
                    item = ''
                l.append(char)
            if char.isnumeric():
                item += char
        return l
            
    def calculate(self, s: str) -> int:
        l = self.segregate("("+s+")")
        #print("initial",l)
        
        
        ops = {
            "+": (lambda x,y: x+y), 
            "-": (lambda x,y: x-y),
        }
        stack = []
        for index,item in enumerate(l):
            if item != ')':
                stack.append(item)
                #print(stack)
            else:
                open_brac = len(stack)-1
                while stack[open_brac-1] != "(":
                    open_brac -= 1
                while stack[-2] != "(":
                    x,op,y = stack.pop(open_brac),stack.pop(open_brac),stack.pop(open_brac)
                    stack.insert(open_brac,int(ops[op](x,y))) 
                temp = stack.pop()
                stack.pop()
                stack.append(temp)
                #print(stack)
        return stack.pop()
