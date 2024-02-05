def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        
    return False


def has_33_alt(nums):
    for i in range(len(nums)):
        if nums[i] == 33:
            return True
        
        if nums[i] == 3:
            if str(nums[i+1])[0] == '3':
                return True 
        
    return False