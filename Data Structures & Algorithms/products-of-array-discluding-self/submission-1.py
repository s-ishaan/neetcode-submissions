class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num != 0:    
                prod *= num
            else:
                zero_count += 1
        soln_list = []
        for num in nums:
            if zero_count == 0:
                soln_list.append(prod//num)
            elif zero_count == 1:
                if num != 0:
                    soln_list.append(0)
                else:
                    soln_list.append(prod)
            else:
                soln_list.append(0)
        
        return soln_list