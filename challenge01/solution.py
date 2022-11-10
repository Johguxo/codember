with open('users.txt') as f:
  lines = f.readlines()
  i = 0
  user = []
  correct = 0
  total = 0
  for line in lines:
    if line == '\n':
      flag_usr = False
      flag_eme = False
      flag_psw = False
      flag_age = False
      flag_loc = False
      flag_fll = False
      for item in user:
        if 'usr' in item:
          flag_usr = True
        if 'eme' in item:
          flag_eme = True
        if 'psw' in item:
          flag_psw = True
        if 'age' in item:
          flag_age = True
        if 'loc' in item:
          flag_loc = True
        if 'fll' in item:
          flag_fll = True
      if flag_usr and flag_eme and flag_psw and flag_age and flag_loc and flag_fll:
        flag_total = True
        correct += 1
        lastUser = user
      user = []
      total += 1
    else:
      user.append(line)
print('Total: ', total, ' - Correctas: ',correct)
print("Ultimo: ", lastUser)
    