def swap_values(numbers):

  # 7
  numbers['a'] = numbers['a'] + numbers['b']
  # 3
  numbers['b'] = numbers['a'] - numbers['b']
  # 4
  numbers['a'] = numbers['a'] - numbers['b']

  return numbers
