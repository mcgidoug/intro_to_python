arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 3


def number_filter(arr, number):
  filter_arr = []
  for num in arr:
    if num >= number:
      filter_arr.append(num)
  return filter_arr


print(number_filter(arr, number))
