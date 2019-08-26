from flask import Flask, render_template, request, json, jsonify


app = Flask(__name__)

arr = [
  {'name': 'Muthu', 'id':1},
  {'name': 'Jayarakash', 'id':2},
  {'name': 'Mani', 'id':3}
]
 

@app.route('/element/<id>',methods = ['GET', 'PUT', 'DELETE'])  
def show(id):
    if request.method == 'GET':
      data = {}
      for x in arr:
        if x['id'] == int(id):
          data = x
      return data

    if request.method == 'DELETE':
      data = {}
      for x in arr:
        if x['id'] == int(id):
          data = x
          del data
      return ''

    if request.method == 'PUT':
      data = {}
      for x in arr:
         if x['id'] == int(id):
           data = x
           data['name']=request.json['name']
          
      return data

    
      

    

@app.route('/array',methods = ['GET', 'POST'])  
def get():
    
    if request.method == "GET":
      return jsonify({'arr' : arr})

    if request.method == "POST":
      data = {'id': request.json['id'], 'name' : request.json['name'] }
      arr.append(data)
      return data

       
    

  
    

if __name__ == '__main__':
    app.run(debug=True)