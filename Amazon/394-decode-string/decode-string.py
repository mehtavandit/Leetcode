class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                string = ""
                
                while stack and stack[-1] != "[":
                    string = stack.pop() + string  
                
                stack.pop()  
                
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num  
                number = int(num)  
                
                
                temp_result = string * number
                
                # Append the result back to the stack
                stack.append(temp_result)
        
        return "".join(stack)  # Join all elements of the stack to get the final string
