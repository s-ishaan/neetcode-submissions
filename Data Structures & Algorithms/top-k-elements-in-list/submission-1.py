class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        counter = []
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        frequency_counter = {}
        for key in count_dict:
            value = count_dict[key]
            if value not in frequency_counter:
                frequency_counter[value] = [key]
            else:
                frequency_counter[value].append(key)
        soln_list = []
        for i in range(len(nums), -1, -1):
            if i in frequency_counter:
                for num in frequency_counter[i]:
                    soln_list.append(num)

                if len(soln_list) == k:
                    return soln_list

