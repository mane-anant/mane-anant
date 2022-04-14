# DATABASE
# Columns: | Player Id | Player Name | Team Name | Age | Average Score | 

Database={
    1:["Akash", "A", 23, 58],
    2:["Ashish", "B", 22, 60],
    3:["Ashok", "C", 23, 56],
    4:["Ayush", "A", 24, 53]
        }



# API simulation of READ operation

# Input Payload
'''
    payload={
            "Player_id": id
        }
'''

def read_player(payload):
    id = payload["Player_id"]
    if id in Database:
        entry=Database[id]
        return {"Code":200, 
                "Response":{"Name":entry[0],"Team":entry[1],"Age":entry[2],"Average":entry[3]},
                "Message":"Read Operation Succesful"}

    else:
        return {"Code":404,"Message":"Player does not exists"}



# API Testing Function

# Testing function

test_payload={
        "Player_id":5
    }

def test_read_player():
    response=read_player(test_payload)
    assert response.get("Code")==200