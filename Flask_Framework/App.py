from flask import Flask ,request,jsonify


app=Flask(__name__)


Data =[
    {
    "task_id": 1,
    "name": "Complete Python logging practice",
    "description": "Practice different logging levels and create log files"
    },
    {
    "task_id": 2,
    "name": "Build a simple Flask To-Do app",
    "description": "Create a basic To-Do application using Flask framework"
    }
]




# Welcome message 
@app.route("/")
def home():
    return "Welcome to the TO DO LIST "

# Get :retrive all the Item
@app.route ("/items",methods=['GET'])
def get_items():
    return jsonify(Data)



# retrive a specifics Task on the basis of ID 
@app.route("/items/<int:Task_id>",methods=["GET"])
def get_Item(Task_id):
    item = next((i for i in Data if i['task_id'] == Task_id), None)
    if item is None:
        return jsonify({"Error":"The Item Not Found "})
    return jsonify(item)

        

# POST :Create New Task 
@app.route("/Add_item",methods=['POST','GET'])
def Add_Item():
    if not request.json or not 'name' in  request.json :
        return jsonify({"Error":"The Item Not Found "})
    new_item={
    "task_id": Data[-1]['task_id']+1 if Data else 1,
    "name": request.json['name'],
    "description": request.json["description"]
    }
    Data.append(new_item)
    return jsonify(new_item)



# PUT :Update an Existing Task
@app.route('/Update/<int:task_id>',methods=['PUT'])
def Update (task_id):
    item = next((i for i in Data if i['task_id'] == task_id), None)
    if item is None:
        return jsonify({"Error":"The Item Not Found "})
    item['name'] = request.json.get('name',item["name"])
    item['description'] = request.json.get('description',item["description"])
    return jsonify(item)


# Delete an existing Item 
@app.route('/Delete/<int:task_id>',methods=['DELETE'])
def Delete_item(task_id):
    global items
    items=[i for i in Data if i["task_id"]!= task_id]  
    return jsonify ({"result":"Item Deleted"})
  

    

if __name__=="__main__":
    app.run(debug=True,port=8000)
    