def u(nums: list[int], thers: int) -> list:
    return_num = []
    for num in nums:
        if num < thers:
            return_num.append(num)
    return return_num


print(u([], 7))
