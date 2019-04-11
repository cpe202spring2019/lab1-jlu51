
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
   if int_list == None:
      raise ValueError
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







