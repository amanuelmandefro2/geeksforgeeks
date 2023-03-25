class Solution: 
    def select(self, arr, i):
        return arr[i]  
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            min_index = i
            select_elem = self.select(arr, i)
            for j in range(i+1, n):
                if select_elem > arr[j]:
                    select_elem = arr[j]
                    min_index = j
            arr[min_index] = arr[i]
            arr[i] = select_elem
