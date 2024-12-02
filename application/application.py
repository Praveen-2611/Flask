from flask import Flask,render_template


FAI=Flask(__name__)

@FAI.route('/first')
def  first():
    return 'This is first flask class'

@FAI.route('/hello')
def  hello():
    return render_template('hello.html')


@FAI.route('/fun')
def fun():
    return render_template('hai.html',name='praveen',id=468)

@FAI.route('/one/<data>/')
def one(data):
    return (f'hi i am {data},how r u')




FAI.run(debug=True,host='192.168.3.146',port=5001)