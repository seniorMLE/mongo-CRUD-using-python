actions = {
    "Action_000":{
        "_action_description":{
            "_010":"--> init action",
            "_020":"--> Set array M, i = -1; sum_01 = 0; flag_01 = 0" 
        },
        "Direction_10":"Action_010",  "_010":"Done"
    },
"Action_010":{
        "_action_description":{
            "_010":"--> i = i + 1",
            "_020":"--> flag_01 = flag_01 + 1",
            "_030":"--> Get element from array"
        },
        "Direction_10":"Action_END", "_010":"Array is empty or the end of array",
        "Direction_20":"Action_020",  "_020":"First element of array",
        "Direction_30":"Action_040",  "_030":"Not first element of array"
    },
"Action_020":{
        "_action_description":{
            "_010":"--> First element"
        },
        "Direction_10":"Action_030", "_010":"Fist element is integer number",
        "Direction_20":"Action_010",  "_020":"First element is real number",
        "Direction_30":"Action_END",  "_030":"First element equal 7"
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
        "Direction_30":"Action_END",  "_030":"Element equal 7"
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
    }
}