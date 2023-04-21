list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def takeId(elem) :
    return elem['id']

def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.
    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    list_1.sort(key=takeId)
    list_2.sort(key=takeId)
    list_3 = []
    
    list_1_i = 0 
    list_2_i = 0
    
    while list_1_i < len(list_1) and list_2_i < len(list_2) :
        if list_1[list_1_i]['id'] == list_2[list_2_i]['id'] :
            d = list_1[list_1_i]
            for l2 in list_2[list_2_i]:
                d[l2] = list_2[list_2_i][l2]
            list_3.append(d)
            list_2_i+=1
            list_1_i+=1
        elif list_1[list_1_i]['id'] < list_2[list_2_i]['id']:
            list_3.append(list_1[list_1_i])
            list_1_i+=1
        else: 
            list_3.append(list_2[list_2_i])
            list_2_i+=1
    
    while list_1_i < len(list_1): 
        list_3.append(list_1[list_1_i])
        list_1_i+=1
    
    while list_2_i < len(list_2): 
        list_3.append(list_2[list_2_i])
        list_2_i+=1
        
    return list_3


list_3 = merge_lists(list_1, list_2)
print(list_3)
