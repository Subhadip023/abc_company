from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing functions
from werkzeug.utils import secure_filename
import time


def check(password,hashed_password):
    
    if check_password_hash(hashed_password, password):
    # Password is correct
        return True
    else:
    # Password is incorrect
        return False

app = Flask(__name__)

# Configuration for the user data database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User_data_base.db"
db = SQLAlchemy(app)


# User data model
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    item = db.Column(db.Integer, default=None)

    def __repr__(self):
        return f"{self.name} - {self.email} - {self.password_hash}"

    def set_password(self, password):
        # generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        self.password_hash = generate_password_hash(password,method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        # print(self.password_hash)
        return check_password_hash(self.password_hash, password)
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

# products data model
class product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(500), nullable=False)
    item = db.Column(db.Integer, nullable=False)
    prize = db.Column(db.Integer, nullable=False)
   
    def __repr__(self):
        return f"{self.name} - {self.item}"

@app.route('/', methods=["POST", "GET"])
def insert_data():

    allproducts=product.query.all()
    return render_template('index.html',allproducts=allproducts)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        email_verification = request.form['email_verification']
        phone = str(request.form['phone'])
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if email != email_verification:
            error_message = 'Email and email verification do not match.'
            return render_template('register.html', error_message=error_message)


        if password != confirm_password:
            error_message = 'Password and confirm password do not match.'
            return render_template('register.html', error_message=error_message)

        # Check if the email is already registered
        existing_user = Data.query.filter_by(email=email).first()
        if existing_user:
            error_message = 'Email already registered.'
            return render_template('register.html', error_message=error_message)



        
        # # Save the data to the database
        # data = Data(name=name, email=email, phone=phone)
        # data.set_password(password)      
        # db.session.add(data)
        # db.session.commit()

        return redirect('/verify?email=' + email+'&name=' + name+"&password="+password+'&phone='+phone)

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Retrieve the user by email
        user = Data.get_user_by_email(email)
          

        if user and user.check_password(password):
            # Successful login
            return redirect ('/thanks')
        else:
            # Invalid password
            error_message = 'Invalid email or password'
            print(error_message)
            return render_template('register.html', error_message=error_message)

    return render_template('register.html')


@app.route('/verify')
def varify():
    email = request.args.get('email')
    name = request.args.get('name')
    phone = request.args.get('phone')
    password= request.args.get('password')

    return render_template("varify.html",email=email,name=name,password=password,phone=phone)




@app.route('/thanks')
def thanks():
    time.sleep(0)
    massge="Welcome"
    # return redirect('/',)
    return render_template('index.html',massge=massge)

@app.route('/about')
def about():
    
    return render_template('about.html')
    
@app.route('/products')

def products():
    allproducts=product.query.all()
    return render_template('products.html',allproducts=allproducts)


@app.route('/products_details/<int:id>')
def products_detals(id):
   
    find=product.query.filter_by(id=id).first()
    return render_template('product_details.html',find=find)

@app.route('/Buy/<int:id>')
def buy_now(id):
    find=product.query.filter_by(id=id).first()
    return render_template('buy_now.html',find=find)



# For office 


@app.route('/dashboard')
def show_data():
    alldata=Data.query.all()
    allproducts=product.query.all()
    return render_template('dashboard.html',alldata=alldata,allproducts=allproducts)

@app.route('/login_ofice', methods=['GET', 'POST'])
def login_office():
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
            return render_template('/login.html', error_message=error_message)

    return render_template('login.html')
@app.route('/delete/<int:id>')
def delete(id):
    delete=product.query.filter_by(id=id).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/dashboard#ProductdataBase')
@app.route('/addproducts', methods=['GET', 'POST'])

def alproducts():
    if request.method == 'POST':
        file = request.files['imageUpload']
        name=request.form['name']
        company_name=request.form['company_name']
        item=request.form['item']
        prize=request.form['prize']
        if file:
            # Generate a secure filename
            filename = secure_filename(file.filename).split('.')[1]
            filename='products/'+name+'.'+filename
            # Specify the directory to save the file
            directory = '/home/subhadip/Desktop/abc_company/static/'
            # Save the file with the generated filename
            file.save(directory + filename)
            print(name)
            print(company_name)
            print(item)
            print(prize)
            print(filename)
            new_product = product(name=name,company_name=company_name,filename=filename,item=item,prize=prize)
            db.session.add(new_product)
            db.session.commit()
            return redirect('/dashboard#ProductdataBase')
            # return 'File uploaded successfully!'

    return render_template('add_product.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    #app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)
