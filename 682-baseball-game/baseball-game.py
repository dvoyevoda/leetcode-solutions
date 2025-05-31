class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = operations[0]
        sum = 0
        new_list = []
        for operation in operations:
            if operation.lstrip('-').isdigit():
                score = int(operation)
                new_list.append(score)
            elif operation == "+":
                score = (int(new_list[-1]) + int(new_list[-2]))
                new_list.append(score)
            elif operation == "D":
                score = int(new_list[-1]) * 2
                new_list.append(score)
            elif operation == "C":
                new_list.pop()
        for num in new_list:
            sum += num
        return sum
            