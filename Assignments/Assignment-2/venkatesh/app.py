from flask import *  #imports

app = Flask(__name__)  #Creating Instance for Flask to use easier 

cars = {"1":"Ferari","2":"Lamborghini","3":"BMW","4":"Audi","5":"Benz"}   #Dictionary for Operation

#route for insert and view

@app.route("/",methods=['POST','GET']) 
def getpost():
    if request.method=='GET':
        return cars
    if request.method=='POST':
        ip = request.json
        cars.update(ip)
        return 'data inserted'

#route for update
@app.route('/<id>',methods=['PUT'])
def put(id):
    ip = request.form['carname']
    cars[str(id)] = ip
    return 'updated successfully'

#route for delete
@app.route("/<id>",methods=['DELETE'])
def dele(id):
    cars.pop(str(id))
    return 'deleted successfully'


#running the app
if __name__ == "__main__":
    app.run(debug=True)