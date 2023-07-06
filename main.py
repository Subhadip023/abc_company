from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User_data_base.db"
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    item=db.Column(db.Integer,default=None)

    def __repr__(self) -> str:
        return f"{self.name} - {self.email}"

@app.route('/')
def insert_data():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     phone = str(request.form['phone'])
    #     password = request.form['password']
    #     data = Data(name=name, email=email, phone=phone,password=password)
    #     db.session.add(data)
    #     db.session.commit()
    #     return redirect('/thanks')

    return render_template('index.html')

@app.route('/contact',methods=["POST", "GET"])
def contact():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = str(request.form['phone'])
        password = request.form['password']
        data = Data(name=name, email=email, phone=phone,password=password)
        db.session.add(data)
        db.session.commit()
        return redirect('/thanks')
    
    return render_template('register.html')
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/dashboard')
def show_data():
    alldata=Data.query.all()
    
    return render_template('dashboard.html',alldata=alldata)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform authentication checks
        if username == 'subhadip' and password == '123456':
            # Successful login
            return redirect('/dashboard')
        else:
            # Invalid username or password
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/about')
def products():
    
    return render_template('about.html')
    
@app.route('/products')
def about():
    
    return render_template('products.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.debug = True
    app.run(host='0.0.0.0', port=8000, debug=True)
