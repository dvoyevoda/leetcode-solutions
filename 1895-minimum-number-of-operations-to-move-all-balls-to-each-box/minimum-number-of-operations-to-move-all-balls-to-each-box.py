class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # for each i check each index, if 1 then add distance from i position

        answer = []

        for i in range(len(boxes)):
            total = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    total += abs(j - i)
            answer.append(total)
        
        return answer

