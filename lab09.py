# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #  What the function needs to do: Return the indices of the numbers in the nums list that add up target value.
    # Step 1: Loop through all values in nums
    # Step 2: Using a second loop, loop through all the values in nums but starting at index 1 rather than 0
    # Step 3: Compare the current value the loop is on to the next value
    # - If the current value and the value on the next index add up to target, then return those indices

    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.

    for i in range(len(nums)): #loops through the amount of values in nums
        for j in range(i+1, len(nums)): # starts on the next index of i and loops through the amount of values in nums
            if nums[i] == nums[j] == target: #checks if the two values add up to the target value
                return [i,j] #returns the indices


def max_profit(prices):
    # Outline (write your plan here first):
    #  What the function needs to do: Return the highest amount of profit by buying something on one day then selling it on another day where the prices have either increased or decreased for that specific item
    # This function also needs a nested loop to iterate through the buy days (i) then the sell days (j)
    # Step 1: Initialize a variable that will keep track of the max profit (we will just call this highest_profit)
    # Step 2: First for loop will loop through the buy days
    # Step 3: Second (the nested for loop) for loop will loop through the sell days. This loop starts on index i+1 and also loops through the rest of the prices array.
    # Step 4: Create a variable profit that subtracts the buy day price from the sell day price to determine the profit
    # Step 5: Compare the profit variable to the highest_profit variable and see which one is a bigger amount
    # Step 6: Return the highest profit 
    # 
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    
    highest_profit: int = 0

    for i in range(len(prices)): #loops through the buy days
        for j in range(i+1, len(prices)): #loops through the sell days
            profit: int =  prices[j] - prices[i] #profit is the difference between the sell day price of the item and the buy day price of the item.

        if profit > highest_profit: #compares profit and highest profit. checks to see if profit is greater than the highest profit already recorded.
            highest_profit = profit # if a different profit is higher than the previous highest_profit, then highest_profit is updated to the value of the current profit variable.

        return highest_profit #returns the highest profit


def max_subarray(nums):
    # Outline (write your plan here first):
    #  What the function needs to do: This array has to return the largest sum of a specific array. The largest sum must be calculated by neighboring numbers. This can be done by checking every start/end position combination for neighboring numbers.
    # Step 1: Start at index 0 and set/initialize nums[0] as the largest sum.
    # Step 2: Loop through the nums array with a for loop and initialize a variable to keep track of the total sum. Every iteration it will reset back to 0 so then the sum of the next subarray can be calculated.
    # Step 3: Use a second for loop to loop through the array starting at index i until the end of the array
    # - increment the total sum by the value of the number at a specific index (so nums[j])
    # Step 4: Compare the largest sum to the total sum. If total sum is larger than the largest sum recorded, the largest sum value is replaced by the value of the total sum.
    # Step 5: Return the largest sum.
    # 
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.

    largest_sum: int = nums[0] #setting the largest sum to the first value in nums
 
    for i in range(len(nums)): #loops through all the values in nums
        total: int = 0 #initializes variable total and sets it to 0. stays in the for loop because the total needs to be reset every iteration.
        for j in range(i, len(nums)): #loops through all the values in nums but starts on the index of i
            total += nums[j] #increments total based on the value of the number on that specific index

        if total > largest_sum: #compares the total calculated to the largest sum recorded. 
            largest_sum = total #if the total of the current subarray is larger than the original largest_sum then largest_sum takes the value of the total

    return largest_sum #returns the largest sum
    

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
