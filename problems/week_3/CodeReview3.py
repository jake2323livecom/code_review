## Zen Of Python #
import this

## Find 3 Highest Numbers #

def highest_nums(nums):
    nums.sort(reverse = True)
    top3 = nums[0:3]
    return(top3)
 Print(return(top3))

nums=[5,10,6,4,3,2]
highest_nums(nums)

## Add a number to its reverse #

def reversi(num):
    num2 = int(str(num)[::-1])
    reversi_sum = num + num2
    return reversi_sum

reversi(27)