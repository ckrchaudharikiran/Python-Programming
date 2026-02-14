Sort Arrays Using a Sorting Algorithm
We implement the classical bubble sort algorithm to obtain the sorted array. To do it, we use two nested loops and swap the elements for rearranging in sorted order.
                                                                                                                                    import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)



# Sort Arrays Using sort() Method of List

# import array as arr
# # creating array
# orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
# print("Original array:", orgnlArray)
# # converting to list 
# sortedList = orgnlArray.tolist()
# # sorting the list
# sortedList.sort()
# # creating array from sorted list
# sortedArray = arr.array('i', sortedList)
# print("Array after sorting:",sortedArray)


# import array as arr
# a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
# sorted(a)
# print(a)
