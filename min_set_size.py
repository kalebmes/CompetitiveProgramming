class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        # Count the frequency of each element in the array
        freq = Counter(arr)
        
        # Sort the elements by frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Remove the elements with the highest frequency until the remaining elements represent at least half of the array
        count = 0
        removed = 0
        for element, frequency in sorted_freq:
            count += frequency
            removed += 1
            if count >= len(arr) // 2:
                break
        
        return removed
