## Question

### Two Sum 

__Hardness: <font color=#22822>Easy</font>__

__Language: Python3__

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have __<font size=4>exactly one solution</font>__ , and you may not use the **same element** twice.

#### Example:


    Given nums = [2, 7, 11, 15], target = 9

    Because nums[0] + nums[1] = 2 + 7 = 9,

    return [0, 1].


## Thoughts
* One solution => list with two element

* what if target is even which can be halfed  => two same value elements may appear => learned function enumerate()

* return is a list of index => find index of list  => 
    * list.find(value) 
    * Find another way to do that by using `i in range(len(nums))` and get i `if nums[i] == target - j`< j is obj in nums,however this code is too long to be elegant,so I choose to use the previous one..>

* Time consuming can be imporved maybe.