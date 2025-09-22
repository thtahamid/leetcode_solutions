class Solution:
    def maxFrequencyElements(self, nums):
        # Find the frequency of each element
        frequencies = [0] * 100
        for num in nums:
            frequencies[num - 1] += 1

        # Determine the maximum frequency, stored in the last index of the sorted array
        frequencies.sort()
        max_freq_index = len(frequencies) - 1
        total_frequencies = frequencies[max_freq_index]

        # Calculate the total frequencies of elements with the maximum frequency
        # Start from the last index and iterate right to left
        while max_freq_index > 0 and frequencies[max_freq_index] == frequencies[max_freq_index - 1]:
            total_frequencies += frequencies[max_freq_index]
            max_freq_index -= 1
        return total_frequencies
        