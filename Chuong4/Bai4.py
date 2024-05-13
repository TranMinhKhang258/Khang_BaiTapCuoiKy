class Solution:
    def HauTo(self, bt):
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack_operator = []
        postfix = []

        for char in bt.split():
            if char.isdigit(): 
                postfix.append(char)
            elif char in priority: 
                while stack_operator and priority[stack_operator[-1]] >= priority[char]:
                    postfix.append(stack_operator.pop())
                stack_operator.append(char) 
            elif char == '(': 
                stack_operator.append(char)
            elif char == ')':  
                while stack_operator and stack_operator[-1] != '(':
                    postfix.append(stack_operator.pop())
                stack_operator.pop()  

        while stack_operator:
            postfix.append(stack_operator.pop())

        return ' '.join(postfix)


solution = Solution()
bt = '2 + 3 * 5'
print("Biểu thức hậu tố của '{}' là: {}".format(bt, solution.HauTo(bt)))
