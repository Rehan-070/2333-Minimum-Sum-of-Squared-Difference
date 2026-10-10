# class Solution:
#     def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
#         l=[]
       
#         for i in range(k1):
#             m1=min(nums1)
#             idx=nums1.index(m1)
#             nums1[idx]=m1+1
            
#             m2=min(nums2)
#             idx=nums2.index(m2)
#             nums2[idx]=m2+1

#         for i in range(len(nums1)):
#             l.append((nums1[i]-nums2[i])**2)
#         return sum(l)

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        ans = 0
        maxx = 0
        ops = k1 + k2
        for i in range(len(nums1)):
            maxx = max(maxx, abs(nums1[i] - nums2[i]))

        freq = [0] * (maxx + 1)
        for i in range(len(nums1)):
            freq[abs(nums1[i] - nums2[i])] += 1

        for i in range(maxx, 0, -1):
            if ops <= 0:
                break
            minn = min(ops, freq[i])
            ops -= minn
            freq[i] -= minn
            freq[i - 1] += minn

        for i in range(maxx, 0, -1):
            ans += i * i * freq[i]

        return ans

