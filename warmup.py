# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d8efe7f8694f3655d60712
def contains_duplicate(list):
    store = set()
    for i in range(len(list)):
        if list[i] in store:
            return True
        store.add(list[i])
    return False


def is_pangram(list):
    unique_alphabets = set()
    for alphabet in list.lower():
        if alphabet.isalpha():
            unique_alphabets.add(alphabet)
    return len(unique_alphabets) == 26


def square_root(num: int):
    if num <= 1:
        return num
    left, right = 2, num // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > num:
            right = mid - 1
        elif mid * mid < num:
            left = mid + 1
        else:
            return mid
    return right


def reverse_vowels(input: str) -> str:
    result = list(input)
    vowels = "aeiouAEIOU"
    start, end = 0, len(input) - 1

    while start <= end:
        if result[start] in vowels and result[end] in vowels:
            result[start], result[end] = result[end], result[start]
            start += 1
            end -= 1
        elif result[start] in vowels:
            end -= 1
        else:
            start += 1

    return "".join(result)


def is_valid_palindrome(s: str) -> bool:
    s = s.lower()
    start, end = 0, len(s) - 1
    while start <= end:
        if s[start].isalnum() and s[end].isalnum():
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        elif s[start].isalnum():
            end -= 1
        else:
            start += 1
    return True


def is_anagram(s, t) -> bool:
    if len(s) != len(t):
        return False
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    for char in t:
        if char in freq_map:
            freq_map[char] -= 1
        else:
            return False

    for freq in freq_map.values():
        if freq != 0:
            return False

    return True


# ["practice", "makes", "perfect", "coding", "makes"], "coding","practice"


def shortest_word_distance(words, word1, word2):
    shortest_distance = len(words)
    pos_word1, pos_word2 = -1, -1
    for i in range(len(words)):
        if words[i] == word1:
            pos_word1 = i
        if words[i] == word2:
            pos_word2 = i
        if pos_word1 != -1 and pos_word2 != -1:
            shortest_distance = min(shortest_distance, abs(pos_word2 - pos_word1))
    return shortest_distance


def num_of_good_pairs(nums: list[int]) -> int:
    freq_map = {}
    num_of_good_pairs = 0
    for num in nums:
        if num in freq_map:
            num_of_good_pairs += freq_map[num]
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    return num_of_good_pairs
