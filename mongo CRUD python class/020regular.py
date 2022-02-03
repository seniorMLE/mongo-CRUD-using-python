M = [1, 2, 3.5, 4, 5.3, 6.5, 7]
sum_01 = 0
flag_01 = -1 
flag_02 = 0
for a in M:
  flag_01 += 1
  if a == 7:
    print('break-' + str(sum_01))
    break
  if int(a) == a:
    if flag_02 == 0:
      sum_01 += a
      print('p1-' + str(a) + '-' + str(sum_01))
      flag_02 = 1
    if flag_01 == 3:
      sum_01 += a
      print('p2-' + str(a) + '-' + str(sum_01))
      flag_01 = 0
  if int(a) != a:
    if flag_02 == 0:
      flag_02 = 1
    if flag_01 == 3:
      flag_01 = 0
print(str(sum_01))