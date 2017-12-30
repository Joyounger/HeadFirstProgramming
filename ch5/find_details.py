def find_details(id2find):
    file = open("surfing_data.csv")
    for line in file:
        info_hash = {}
        (info_hash['id'], info_hash['name'], info_hash['country'], info_hash['average'], info_hash['board'], info_hash['age']) = line.split(";")
        if int(info_hash['id']) == id2find:
            file.close()
            return(info_hash) #从函数中返回一个hash,调用代码只需了解函数返回了一个可以直接处理的hash
    file.close()
    return({})


lookup_id = int(input("enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:          " + surfer['id'])
    print("NAME:        " + surfer['name'])
    print("country:     " + surfer['country'])
    print("average:     " + surfer['average'])
    print("board:       " + surfer['board'])
    print("age:         " + surfer['age'])
