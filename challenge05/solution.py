from data import data

list = []
for index, item in enumerate(data):
  list.append(index)

def delete_list(list):
  result = []
  next_index = -1
  for i, item in enumerate(list):
    if next_index == i and flag:
      flag = False
    else:
      flag = True
      result.append(item)
      if i == len(list)-1:
        result.pop(0)
    next_index = i + 1
  return result

while len(list) > 1:
  list = delete_list(list)

index_result = list[0]
print(index_result, data[index_result])
