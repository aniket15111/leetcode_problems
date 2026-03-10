#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        
        hash_table={}
        
        for i in arr:
            if i not in hash_table:
                hash_table[i]=0
            else:
                hash_table[i]+=1
        for key, value in hash_table.items():
            if value == 0:
                return key
        return 0