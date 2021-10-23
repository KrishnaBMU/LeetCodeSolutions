class Solution:
    def segregate(self,s):
        result = list()
        operator_count = {
            "+": 0,
            "-": 0,
            "*": 0,
            "/": 0
        }
        item = ""
        # space_count = 0
        for index, char in enumerate(s):
            if char.isspace():
                # space_count += 1
                if item != "":
                    result.append(int(item))
                    item = ""
            if char in ["+", "-", "*", "/"]:
                operator_count[char]+=1
                if item != "":
                    result.append(int(item))
                    item = ""
                result.append(char)
            if char.isnumeric():
                item += char
        if item != "":
            result.append(int(item))
        return result, operator_count
    
    def calculate(self, s: str) -> int:
        exp, operator_count = self.segregate(s)
        # print("Initial", exp)
        # print(operator_count)

        ops = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x // y)
        }
        index=0
        while index < len(exp):
            if exp[index] in ["/","*"]:
                exp[index - 1] = ops[exp[index]](exp[index - 1], exp[index + 1])
                exp.pop(index)
                exp.pop(index)
                index-=1
            index+=1
        index = 0
        while index < len(exp):
            if exp[index] in ["-", "+"]:
                exp[index - 1] = ops[exp[index]](exp[index - 1], exp[index + 1])
                exp.pop(index)
                exp.pop(index)
                index-=1
            index += 1
        return exp[0]
