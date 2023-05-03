class Solution:

    # Solution
    """
    first we are creating the set
    """
    def containsDuplicate(self, nums):
        new_set = set()
        """so next have to check the number is duplicate or not with the help of for loop by itrating nums array"""
        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)
        return False


if __name__=="__main__":
    nums = [1,2,3,5]
    a = Solution()
    b = a.containsDuplicate(nums)
    print(b)