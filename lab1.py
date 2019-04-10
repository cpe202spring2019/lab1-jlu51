
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None
   if int_list is None:
      raise ValueError
   temp = int_list[0]
   for i in range(1, len((int_list))):
      if temp < int_list[i]:
         temp = int_list[i]
   return temp

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if len(int_list) == 1:
      return int_list
   else:
      return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   if high >= 1:
      midpoint = ((high - low) // 2) + low
      if int_list[midpoint] == target:
         return midpoint
      elif int_list[midpoint] < target:
         # low = midpoint + 1
         return bin_search(target, midpoint + 1, high, int_list)
      else:  # int_list[midpoint] > target
         return bin_search(target, low, midpoint, int_list)
      # high = midpoint - 1
   else:
      return None

list_val =[1,2,3,4,7,8,9,10]
low = 0
high = len(list_val)-1
#self.assertEqual(bin_search(55, 0, len(list_val) - 1, list_val), 0)
# print(bin_search(3, 0, 5, [3, 7, 10, 16, 28, 32]))
# print(bin_search(1, 0, len(list_val) - 1, list_val))
# print(bin_search(0, low, len(list_val) - 1, list_val))

print(bin_search(1, low, len(list_val) - 1, list_val))

# def binary_search(target, low, high, int_list):
#    if target not in int_list:
#       return None
#    while high >= 1:
#       midpoint = ((high - low) // 2) + low
#       if int_list[midpoint] == target:
#          return midpoint
#       elif int_list[midpoint] < target:
#          low = midpoint + 1
#       else:  # int_list[midpoint] > target
#          high = midpoint - 1
#    else:
#       return None
#
#
# print(binary_search(387, 0, 5, [3, 7, 10, 16, 28, 32]))



