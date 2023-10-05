import math


def two_sum(nums, target):
    comp_map = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in comp_map:
            return [comp_map[compliment], i]
        comp_map[nums[i]] = i


def remove_duplicates(nums):
    unique_pos = 1
    for i in range(len(nums)):
        if nums[unique_pos - 1] != nums[i]:
            nums[unique_pos] = nums[i]
            unique_pos += 1
    return unique_pos


def sorted_squares(nums):
    largest_sqaure_ndex = len(nums) - 1
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    while left <= right:
        leftSquare = nums[left] * nums[left]
        rightSquare = nums[right] * nums[right]
        if leftSquare > rightSquare:
            result[largest_sqaure_ndex] = leftSquare
            left += 1
        else:
            result[largest_sqaure_ndex] = rightSquare
            right -= 1
        largest_sqaure_ndex -= 1
    return result


def three_sum(nums):
    nums.sort()
    triplets = []
    nums_length = len(nums)
    for i in range(nums_length):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, nums_length - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] + nums[i] < 0:
                left += 1
            else:
                right -= 1
    return triplets


def three_sum_closest1(nums, target):
    nums.sort()
    nums_length = len(nums)
    min_sum_triplet = math.inf
    dist_from_target = math.inf
    for i in range(nums_length - 2):
        left, right = i + 1, nums_length - 1
        while left < right:
            curr_pair_sum = nums[i] + nums[left] + nums[right]
            if curr_pair_sum == target:
                dist_from_target = 0
                min_sum_triplet = min(min_sum_triplet, curr_pair_sum)
                left += 1
                right -= 1
            elif dist_from_target != 0:
                curr_dist_from_target = abs(curr_pair_sum - target)
                if curr_dist_from_target == dist_from_target:
                    min_sum_triplet = min(min_sum_triplet, curr_pair_sum)
                elif curr_dist_from_target < dist_from_target:
                    dist_from_target = curr_dist_from_target
                    min_sum_triplet = curr_pair_sum
                if curr_pair_sum < target:
                    left += 1
                else:
                    right -= 1
    return min_sum_triplet


def three_sum_closest(nums, target):
    nums.sort()
    nums_length = len(nums)
    min_sum = math.inf
    for i in range(nums_length - 2):
        l, r = i + 1, nums_length - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == target:
                return curr_sum
            elif (abs(curr_sum - target) < abs(min_sum - target)) or (
                abs(curr_sum - target) == abs(min_sum - target) and curr_sum < min_sum
            ):
                min_sum = curr_sum

            if curr_sum < target:
                l += 1
            else:
                r -= 1
    return min_sum


def three_sum_smaller(nums, target):
    nums.sort()
    triplet_count = 0
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] < target:
                triplet_count += right - left
                left += 1
            else:
                right -= 1
    return triplet_count
