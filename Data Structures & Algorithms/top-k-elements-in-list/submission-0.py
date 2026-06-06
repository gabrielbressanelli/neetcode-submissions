class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1

        bucket = []

        for _ in range(len(nums)+1):
            bucket.append([])
        
        for num, count in frequencies.items():
            bucket[count].append(num)

        top_k = []

        for i in range(len(bucket) -1, -1, -1):
            if bucket[i]:
                for i in bucket[i]:
                    top_k.append(i)

                    if len(top_k) == k:
                        return top_k
