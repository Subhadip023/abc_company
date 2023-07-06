from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

@app.route('/dashboard')
def dashboard():
    # Protected dashboard page
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
