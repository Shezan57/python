# Write a function that takes a list of integers as input and returns the sorted
# version of the list. The sorting should be done using the bubble sort algorithm.


# Step1:	Understand the basic principles of the bubble sort algorithm.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):      # Step2:	Implement bubble sort using nested for loops.
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                
    return lst

print(bubble_sort([64,34,25,12,22,11,90]))  # Step3:Create an integer list outside the function,
                                            #call the sorting function, and print the sorted result.
