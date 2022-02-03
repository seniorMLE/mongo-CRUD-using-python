M = [1.4, 777, 2, 4.3, 777, 5, 6.5, 777, 3]
sum_01 = 0
i = 0 # by sublist
i_main = -1 # by all array
flag_01 = -1
current_action = "Action_000"
direction = "Direction_10"

actions = {
    "Action_000":{
        "_action_description":{
            "_010":"--> init action",
            "_020":"--> Set array M, i = -1; sum_01 = 0; flag_01 = 0" 
        },
        "Direction_10":"Action_300",  "_010":"Done"
    },
"Action_010":{
        "_action_description":{
            "_010":"--> i = i + 1",
            "_015":"--> i_main += i",
            "_020":"--> flag_01 = flag_01 + 1",
            "_030":"--> Get element from array"
        },
        "Direction_10":"Action_END", "_010":"Sublist is empty or the end of array",
        "Direction_20":"Action_020",  "_020":"First element of sublist",
        "Direction_30":"Action_040",  "_030":"Not first element of sublist"
    },
"Action_020":{
        "_action_description":{
            "_010":"--> First element"
        },
        "Direction_10":"Action_030", "_010":"Fist element is integer number",
        "Direction_20":"Action_010",  "_020":"First element is real number",
        "Direction_30":"Action_340",  "_030":"First element equal 7",
        "Direction_40":"Action_300",  "_040":"First element equal 777"
    },
"Action_030":{
        "_action_description":{
            "_010":"--> First element is integer number",
            "_020":"--> sum_01 = sum_01 + M[i]"
        },
        "Direction_10":"Action_010", "_010":"Done"
    },
"Action_040":{
        "_action_description":{
            "_010":"--> Not the first element"
        },
        "Direction_10":"Action_050", "_010":"Element is integer number",
        "Direction_20":"Action_060",  "_020":"Element is real number",
        "Direction_30":"Action_340",  "_030":"Element equal 7",
        "Direction_40":"Action_300",  "_040":"Element equal 777"
    },
"Action_050":{
        "_action_description":{
            "_010":"--> Element is integer number"
        },
        "Direction_10":"Action_010", "_010":"Done"
    },
"Action_060":{
        "_action_description":{
            "_010":"--> Element is real number"
        },
        "Direction_10":"Action_010", "_010":"Done"
    },
"Action_300":{
        "_action_description":{
            "_010":"--> i_main = i_main + 1",
            "_020":"--> i = 0",
            "_030":"--> Get element from array"
        },
        "Direction_10":"Action_END", "_010":"Array is empty or the end of array",
        "Direction_20":"Action_010",  "_020":"Element equel 777",
        "Direction_30":"Action_300",  "_030":"Element not equel 777"
    },
"Action_340":{
        "_action_description":{
            "_010":"--> i_main = i_main + 1",
            "_020":"--> Get element from array"
        },
        "Direction_10":"Action_END", "_010":"Array is empty or the end of array",
        "Direction_20":"Action_300",  "_020":"Element equel 777",
        "Direction_30":"Action_330",  "_030":"Element not equel 777"
    }
}
# init block


while 1 == 1:
  # define next action
  action = actions[current_action][direction]
  previous_action = current_action
  current_action = action    
  print(previous_action, "|",direction, "|",current_action, "|", i_main, "|", i, "|", flag_01, "|", sum_01)

  if current_action in actions:
    ### Action_010 ##################################
    if current_action == "Action_010":
      i += 1 
      i_main += 1
      flag_01 += 1
      if i_main > len(M) - 1:
          direction = "Direction_10" # The end of array
      if i_main <= len(M) - 1:
        if i == 1:
          direction = "Direction_20" # First element of sublist
        if i != 1:
          direction = "Direction_30" # Not first element of sublist
    ### Action_020 ##################################
    if current_action == "Action_020":
      if int(M[i_main]) == M[i_main]:
        direction = "Direction_10"
      if int(M[i_main]) != M[i_main]:
        direction = "Direction_20"
      if M[i_main] == 7:
        direction = "Direction_30"
      if M[i_main] == 777:
        direction = "Direction_40"
    ### Action_030 ##################################
    if current_action == "Action_030":
      sum_01 = sum_01 + M[i_main]
      direction = "Direction_10"
    ### Action_040 ##################################
    if current_action == "Action_040":
      if int(M[i_main]) == M[i_main]:
        direction = "Direction_10"
      if int(M[i_main]) != M[i_main]:
        direction = "Direction_20"
      if M[i] == 7:
        direction = "Direction_30"
      if M[i_main] == 777:
        direction = "Direction_40"
    ### Action_050 ##################################
    if current_action == "Action_050":
      if flag_01 == 3:
        sum_01 = sum_01 + M[i_main]
        flag_01 = 0
      direction = "Direction_10"
    ### Action_060 ##################################
    if current_action == "Action_060":
      if flag_01 == 3:
        flag_01 = 0
      direction = "Direction_10"  
    ### Action_300 ##################################
    if current_action == "Action_300":
      i = 0
      i_main += 1 
      if i_main > len(M) - 1:
          direction = "Direction_10" # Array is empty or the end of array
      if i_main <= len(M) - 1:
        if M[i_main] == 777:
          direction = "Direction_20" # Element equel 777
        if M[i_main] != 777:
          direction = "Direction_30" # Element not equel 777    
    ### Action_340 ##################################
    if current_action == "Action_340":
      i_main += 1 
      if i_main > len(M) - 1:
          direction = "Direction_10" # Array is empty or the end of array
      if i_main <= len(M) - 1:
        if M[i_main] == 777:
          direction = "Direction_20" # Element equel 777
        if M[i_main] != 777:
          direction = "Direction_30" # Element not equel 777           
    continue
  break # end of loop where 1 == 1

if current_action.find("END") == 0:
       print("\n\Error: current_action:[" + current_action + "]\n")
if current_action.find("END") != 0:
    print("\nsum is [" + str(sum_01) + ']')
    print('\nThe End')