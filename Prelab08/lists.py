import listmod as l

if __name__ == "__main__":
  list_1 = input("Enter the first list of numbers: ")
  list_2 = input("Enter the second list of numbers: ")

  print("First list: [" + list_1 + "]")
  print("Second list: [" + list_2 + "]")

  list_1 = list(map(int, list_1.split(' ')))
  list_2 = list(map(int, list_2.split(' ')))

  (merged, median) = l.find_median(list_1, list_2)

  print("Merged list: " + str(merged))
  print("Median: " + str(median))
