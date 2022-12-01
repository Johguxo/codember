start = 11098
end = 98123

list_numbers = range(start,end+1)
list_results = []

for number in list_numbers:
  flag = False
  strNumber = str(number)
  if '55' in strNumber:
    before_digit = 0
    for digit in strNumber:
      if before_digit <= int(digit):
        flag = True
      else:
        flag = False
        break
      before_digit = int(digit)
    if flag:
      list_results.append(strNumber)

print("Correctas: ", len(list_results))
print(list_results)
print("55:", list_results[55])