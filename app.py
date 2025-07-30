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

@app.route('/private.key')
def private_key():
    ip = request.remote_addr
    with open("honeypot.log", "a") as f:
        f.write(f"[File Access] IP: {ip} tried to access private.key\n")
    return "\nfakekey5679==\n", 403

@app.route('/.env')
def env_file():
    ip = request.remote_addr
    with open("honeypot.log", "a") as f:
        f.write(f"[File Access] IP: {ip} tried to access .env\n")
    return "API_KEY=fakeapikey123\nSECRET_KEY=fakesecret456", 403

@app.route('/admin')
def fake_admin():
    ip = request.remote_addr
    with open("honeypot.log", "a") as f:
        f.write(f"[ADMIN] Access from {ip}\n")
    return "404 Not Found"

@app.route('/wallet.db')
def fake_wallet_db():
    ip = request.remote_addr
    with open("honeypot.log", "a") as f:
        f.write(f"[WALLET.DB] Access from {ip}\n")
    return "Access Denied"

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
