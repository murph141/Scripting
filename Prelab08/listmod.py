import math as m

def find_median(list_1, list_2):
  merged = sorted(list_1 + list_2)

  return(merged, merged[m.floor((len(merged) - 1) / 2)])
