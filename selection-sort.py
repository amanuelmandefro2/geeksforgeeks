#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, arr,n):
        i = 0;

        
        while i < n-1:
            min_elem = self.select(arr, i)
            min_index = i
            for j in range(i+1, n):
                if min_elem > arr[j]:
                    min_index = j
                    min_elem = arr[j]
            
            (arr[i], arr[min_index]) = (arr[min_index], arr[i])
            i = i+ 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
