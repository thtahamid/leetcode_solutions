class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Use a dictionary to store the elements and their ranks
        rank_map = {}
        
        # Sort the array and assign ranks
        rank = 1
        for val in sorted(set(arr)):  # Using set to remove duplicates, then sorting
            rank_map[val] = rank
            rank += 1
        
        # Create the result array with corresponding ranks
        result = [rank_map[val] for val in arr]
        
        return result