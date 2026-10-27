class Solution:
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


solver = Solution()

# 3. Call the function using the instance and store the result
output = solver.fizzBuzz(15)

# 4. Print the result to see it
print(output)