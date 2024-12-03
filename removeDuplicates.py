def removeDuplicates(self, nums: List[int]):
        l = len(nums)
        k = 1
        
        for i in range(1,l):
            if(nums[i-1] != nums[i]):
                nums[k] = nums[i]
                k=k+1
        return k
