def array_of_array_products(nums):
    size = len(nums)
    prods = [1] * size
    Lp = Rp = 1
    for i in range(size):
        prods[i] *= Lp
        prods[~i] *= Rp
        Lp *= nums[i]
        Rp *= nums[~i]
    return prods


if __name__ == '__main__':
    print(array_of_array_products([8, 10, 2]))