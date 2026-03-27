# Problem: Sort an Array
# Language: python
# Runtime: 1490 ms
# Memory: 21.9 MB

class Solution(object):
    
    def merge(self, left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret
    
    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        pivot = int(n/2)
        left  = self.merge_sort(nums[0:pivot])
        right = self.merge_sort(nums[pivot:])
        
        return self.merge(left, right)
    
    
        
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return self.merge_sort(nums)
        