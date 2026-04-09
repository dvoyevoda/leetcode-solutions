class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix_array = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix_array.append(nums[i] + prefix_array[-1])
            
        subarrays = []
        
        for i in range(len(nums)):
            left = i - k
            right = i + k
            if left < 0 or right > len(nums) - 1:
                subarrays.append(-1)
            else:
                total = prefix_array[right] - prefix_array[left] + nums[left]
                avg = total // ((k * 2) + 1)
                subarrays.append(avg)
                
        
        return subarrays