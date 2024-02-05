def spy_game(nums, find='007'):
    return rec_spy(nums=nums, score=0)


def rec_spy(nums, score):
    # print(nums, score)
    if score == 3:
        return True

    find_digit = 0

    if score == 2:
        find_digit = 7
    
    for i, num in enumerate(nums):
        if num == find_digit:
            # print(num)
            return rec_spy(nums=nums[i+1:], score=score+1)
        
    return False