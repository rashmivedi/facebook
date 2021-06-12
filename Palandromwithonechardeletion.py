class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i , j = 0, len(s)-1
        
        def isValid(s, i, j): #method called below
            
            while(i<j):
                if(s[i]!=s[j]):
                    return False
                    
                i += 1
                j -= 1
                
            return True
        

        while(i<j):
        
            if(s[i]!=s[j]): 
                break  # break the while loop if not equal and do not increment and move to isvalid() in return statement
            i += 1
            j -= 1
        

        return(isValid(s,i+1,j) or isValid(s,i,j-1))
