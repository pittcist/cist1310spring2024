from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('login.htm')

@app.route('/flask')
def hello_flask():  
    return 'Hello Flask'

@app.route('/python/<name>')
def hello_python(name):
    if name == 'ken':
        return 'Hello Python with {0} as the admin'.format(name)
    else:
        return 'Welcome guest!'

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
    
@app.route('/success/<name>')
def success(name):
    return 'Welcome {0}'.format(name)

if __name__ == '__main__':
    app.run()