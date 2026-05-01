class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checkif freq of first window match the freq of s2 
        #we will have a window of size s1 on s2 that will
        #do this job of freq checking if not then inrement left pointer 
        #repeat the process again and make sure to delete the lef ptr from map

        count2 = {}
        count1 = {}

        left = 0
        for right in range(len(s1)):
            count1[s1[right]] = 1 + count1.get(s1[right] , 0)

        for right in range(len(s2)):
            
            count2[s2[right]] = 1 + count2.get(s2[right],0)
            
            #window
            while  right - left + 1 > len(s1):
                count2[s2[left]] -=1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left+=1

            if count1 == count2:
                return True
        return False

        


