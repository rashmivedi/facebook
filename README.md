# facebook
#Facebook screening
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, str1, str2):
        """
        :type str1: List[int]
        :type str2: List[int]
        :rtype: List[int]
        """  
        set1 = set(str1)
        set2 = set(str2)
        return list(set2 & set1)
