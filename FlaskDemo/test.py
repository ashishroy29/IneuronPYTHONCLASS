from flask import Flask, request, jsonify

#Creating an object
app = Flask(__name__) #here we are just creating an object called Flask, so that i will be able to utilize the function which is written inside a class

#creating a route (incase we are trying to invoke it on a different place to my system)

@app.route('/xyz',methods = ['GET','POST']) #This is behaving ling a decorator,. get and post sends a data.
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/ashi',methods = ['POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/ashi/kumar',methods = ['POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a+b
        return jsonify(str(result))

@app.route('/abcxyz',methods = ['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['ashi']
        b = request.json['roy']
        result = a+b
        return jsonify(str(result))

if __name__=='__main__':
    app.run()