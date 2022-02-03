M = [1.4, 777, 2, 4.3, 7, 8, 777, 777, 5, 6.5, 777, 3,777]
sum_01 = 0
i = 0 # by sublist
i_main = -1 # by all array
flag_01 = 0
flag_02 = 0
buffer =[]
for a in M:    
    if flag_01 == 1:
        if a == 7:
            flag_01 = 2            
            continue            
    if a==777:        
        if flag_01 ==1 or flag_01 ==2:
            flag_01 =3
        else:
            flag_01 = 1
        
        if flag_01 ==2:            
            flag_01 = 0
            sum_01 += sum(buffer)  
            buffer =[]
            continue
            
        if flag_01 == 3:
            sum_01 += sum(buffer)            
            buffer =[]
            flag_01 = 0
            continue
        
        continue
        
    if int(a) == a:            
        if flag_01 == 1:
            buffer.append(a)          
    if int(a) != a:
        i_main += 1                                 

print(str(sum_01))