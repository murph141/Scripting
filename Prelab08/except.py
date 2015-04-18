if __name__ == "__main__":
  list_1 = input("Please enter some values: ")

  list_1 = list_1.split(' ')

  sum = 0
  for item in list_1:
    try:
      sum += float(item)
    except ValueError:
      pass

  print(sum)
