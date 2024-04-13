from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/path/to/the/uploads'  # replace with your desired folder
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'your_secret_key'  # replace with your secret key


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # TODO: Validate the username and password with your user database
    # For now, we'll just redirect to the dashboard
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    # TODO: Check if the user is logged in before rendering
    return render_template('dashboard.html')


@app.route('/dashboardEYE')
def dashboardEYE():
    return render_template('dashboardEYE.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'dataset' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['dataset']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        # TODO: Process the file or redirect to another page
        flash('File successfully uploaded')
        return redirect(url_for('dashboard'))
    else:
        flash('Allowed file types are ' + str(ALLOWED_EXTENSIONS))
        return redirect(request.url)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/check')
def check():
    return render_template('check.html')


@app.route('/customer_check')
def customer_check():
    return render_template('customer_check.html')


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Logic to handle password reset request
        email = request.form.get('email')
        # Here you would typically generate a password reset token and send it via email
        # For now, we'll just pretend we've done that and return a success message
        flash('A password reset link has been sent to your email address.')
        return redirect(url_for('login'))

    return render_template('forgot_password.html')


if __name__ == '__main__':
    app.run(debug=True)
