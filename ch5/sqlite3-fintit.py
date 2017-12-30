import sqlite3


def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        info_hash = {}
        if id2find == row['id']:
            info_hash['id'] = str(row['id'])
            info_hash['name'] = row['name']
            info_hash['country'] = row['country']
            info_hash['average'] = str(row['average'])
            info_hash['board'] = row['board']
            info_hash['age'] = str(row['age'])
            cursor.close()
            return(info_hash)
    cursor.close()
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
