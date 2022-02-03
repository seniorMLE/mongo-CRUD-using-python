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