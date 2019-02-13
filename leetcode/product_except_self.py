def product_except_self(nums):
    sol = [1] * len(nums)

    left_product = nums[0]
    for i in range(1, len(nums)):
        sol[i] = left_product
        left_product *= nums[i]

    right_product = nums[-1]
    for j in range(len(nums) - 2 , -1, -1):
        sol[j] *= right_product
        right_product *= nums[j]
    return sol


if __name__ == '__main__':
    print(product_except_self([2,2,3,4]))