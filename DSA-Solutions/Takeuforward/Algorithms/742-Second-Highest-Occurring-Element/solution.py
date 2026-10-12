class Solution:
    def secondMostFrequentElement(self, nums):
        freq = {}

        # Step 1: Count frequencies
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Step 2: Find the highest and second-highest frequencies
        max_freq = 0
        second_max_freq = 0

        for i in freq:
            if freq[i] > max_freq:
                second_max_freq = max_freq
                max_freq = freq[i]

            elif freq[i] < max_freq and freq[i] > second_max_freq:
                second_max_freq = freq[i]

        # Step 3: Check whether a second-highest frequency exists
        if second_max_freq == 0:
            return -1

        # Step 4: Find the smallest element with that frequency
        res = None

        for i in freq:
            if freq[i] == second_max_freq:
                if res is None or i < res:
                    res = i

        return res