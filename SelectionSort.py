def select(self, arr, i):
        # code here 
        max = arr[0]
        sort = 0
        for j in range(1, i+1):
            if arr[j] > max:
                sort = j
                max = arr[j]
        return sort
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1, 0, -1):
            j = self.select(arr, i)

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
