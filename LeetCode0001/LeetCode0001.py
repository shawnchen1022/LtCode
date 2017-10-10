#class LeetCode0001:
def solution(nums,target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''

        for i in nums:
            if target - i in nums:
                if target-i == i:
                    if nums.count(i)==2:
                        return [j for (j, q) in enumerate(nums) if q == i]
                else:
                    return [nums.index(i),nums.index(target-i)]

        '''''
        for i in nums:
            return [j for j,i in enumerate(nums) if target-i in nums]
            '''

def main():
        nums = [3,2,4]
        target = 6
        ls = solution(nums,target)
        print(ls)

if __name__ == '__main__':
        main()
