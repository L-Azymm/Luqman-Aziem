from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output_files'
ALLOWED_EXTENSIONS = {'enc', 'pem', 'key', 'bin', 'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

# ------------------ AES ------------------
@app.route('/aes')
def aes_menu():
    return render_template('aes_menu.html')

@app.route('/aes/encrypt', methods=['GET', 'POST'])
def aes_encrypt():
    if request.method == 'POST':
        message = request.form['message'].encode()
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message)

        enc_filename = secure_filename(request.form.get('enc_file', 'message.enc'))
        key_filename = secure_filename(request.form.get('key_file', 'key.key'))

        with open(os.path.join(app.config['OUTPUT_FOLDER'], enc_filename), 'wb') as f:
            f.write(cipher.nonce + tag + ciphertext)
        with open(os.path.join(app.config['OUTPUT_FOLDER'], key_filename), 'wb') as f:
            f.write(key)

        flash('✅ AES encryption done. Files saved.', 'success')
        return redirect(url_for('aes_menu'))

    return render_template('aes_encrypt.html')

@app.route('/aes/decrypt', methods=['GET', 'POST'])
def aes_decrypt():
    if request.method == 'POST':
        enc_file = request.files['enc_file']
        key_file = request.files['key_file']

        if enc_file and allowed_file(enc_file.filename) and key_file and allowed_file(key_file.filename):
            enc_filename = secure_filename(enc_file.filename)
            key_filename = secure_filename(key_file.filename)

            enc_path = os.path.join(app.config['UPLOAD_FOLDER'], enc_filename)
            key_path = os.path.join(app.config['UPLOAD_FOLDER'], key_filename)

            enc_file.save(enc_path)
            key_file.save(key_path)

            with open(enc_path, 'rb') as f:
                data = f.read()
            nonce, tag, ciphertext = data[:16], data[16:32], data[32:]

            with open(key_path, 'rb') as f:
                key = f.read()

            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            try:
                decrypted = cipher.decrypt_and_verify(ciphertext, tag)
                flash(f'✅ AES decryption successful: {decrypted.decode()}', 'success')
            except ValueError:
                flash('❌ AES decryption failed - tag verification failed', 'error')

            os.remove(enc_path)
            os.remove(key_path)
        else:
            flash('❌ Invalid file types', 'error')

        return redirect(url_for('aes_menu'))

    return render_template('aes_decrypt.html')

# ------------------ RSA ------------------
@app.route('/rsa')
def rsa_menu():
    return render_template('rsa_menu.html')

@app.route('/rsa/encrypt', methods=['GET', 'POST'])
def rsa_encrypt():
    if request.method == 'POST':
        message = request.form['message'].encode()
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
        ciphertext = cipher.encrypt(message)

        enc_filename = secure_filename(request.form.get('enc_file', 'message.enc'))
        pub_filename = secure_filename(request.form.get('pub_file', 'pub.pem'))
        priv_filename = secure_filename(request.form.get('priv_file', 'priv.pem'))

        with open(os.path.join(app.config['OUTPUT_FOLDER'], enc_filename), 'wb') as f:
            f.write(ciphertext)
        with open(os.path.join(app.config['OUTPUT_FOLDER'], pub_filename), 'wb') as f:
            f.write(public_key)
        with open(os.path.join(app.config['OUTPUT_FOLDER'], priv_filename), 'wb') as f:
            f.write(private_key)

        flash('✅ RSA encryption done. Files saved.', 'success')
        return redirect(url_for('rsa_menu'))

    return render_template('rsa_encrypt.html')

@app.route('/rsa/decrypt', methods=['GET', 'POST'])
def rsa_decrypt():
    if request.method == 'POST':
        enc_file = request.files['enc_file']
        priv_file = request.files['priv_file']

        if enc_file and allowed_file(enc_file.filename) and priv_file and allowed_file(priv_file.filename):
            enc_filename = secure_filename(enc_file.filename)
            priv_filename = secure_filename(priv_file.filename)

            enc_path = os.path.join(app.config['UPLOAD_FOLDER'], enc_filename)
            priv_path = os.path.join(app.config['UPLOAD_FOLDER'], priv_filename)

            enc_file.save(enc_path)
            priv_file.save(priv_path)

            with open(enc_path, 'rb') as f:
                ciphertext = f.read()
            with open(priv_path, 'rb') as f:
                private_key = RSA.import_key(f.read())

            cipher = PKCS1_OAEP.new(private_key)
            try:
                decrypted = cipher.decrypt(ciphertext)
                flash(f'✅ RSA decryption successful: {decrypted.decode()}', 'success')
            except ValueError:
                flash('❌ RSA decryption failed', 'error')

            os.remove(enc_path)
            os.remove(priv_path)
        else:
            flash('❌ Invalid file types', 'error')

        return redirect(url_for('rsa_menu'))

    return render_template('rsa_decrypt.html')

# ------------------ SHA-256 ------------------
@app.route('/sha256', methods=['GET', 'POST'])
def sha256_hashing():
    if request.method == 'POST':
        msg1 = request.form['msg1'].encode()
        msg2 = request.form['msg2'].encode()

        hash1 = hashlib.sha256(msg1).hexdigest()
        hash2 = hashlib.sha256(msg2).hexdigest()

        result = {
            'hash1': hash1,
            'hash2': hash2,
            'match': hash1 == hash2
        }

        return render_template('sha256_result.html', result=result)

    return render_template('sha256_hashing.html')

# ------------------ Digital Signature ------------------
@app.route('/signature')
def signature_menu():
    return render_template('signature_menu.html')

@app.route('/signature/sign', methods=['GET', 'POST'])
def sign_message():
    if request.method == 'POST':
        message = request.form['message'].encode()
        use_custom_key = 'use_custom_key' in request.form

        if use_custom_key and 'priv_key_file' in request.files:
            priv_key_file = request.files['priv_key_file']

            if priv_key_file and allowed_file(priv_key_file.filename):
                priv_filename = secure_filename(priv_key_file.filename)
                priv_path = os.path.join(app.config['UPLOAD_FOLDER'], priv_filename)
                priv_key_file.save(priv_path)

                with open(priv_path, 'rb') as f:
                    private_key = RSA.import_key(f.read())

                public_key = private_key.publickey().export_key()
                os.remove(priv_path)
            else:
                flash('❌ Invalid or missing private key file', 'error')
                return redirect(url_for('sign_message'))
        else:
            key = RSA.generate(2048)
            private_key = key
            public_key = key.publickey().export_key()

        hash_obj = SHA256.new(message)
        signature = pkcs1_15.new(private_key).sign(hash_obj)

        sig_filename = secure_filename(request.form.get('sig_file', 'sig.bin'))
        pub_filename = secure_filename(request.form.get('pub_file', 'pub.pem'))
        msg_filename = secure_filename(request.form.get('msg_file', 'msg.txt'))

        with open(os.path.join(app.config['OUTPUT_FOLDER'], sig_filename), 'wb') as f:
            f.write(signature)
        with open(os.path.join(app.config['OUTPUT_FOLDER'], pub_filename), 'wb') as f:
            f.write(public_key)
        with open(os.path.join(app.config['OUTPUT_FOLDER'], msg_filename), 'wb') as f:
            f.write(message)

        flash('✅ Message signed and files saved.', 'success')
        return redirect(url_for('signature_menu'))

    return render_template('sign_message.html')

@app.route('/signature/verify', methods=['GET', 'POST'])
def verify_signature():
    if request.method == 'POST':
        sig_file = request.files['sig_file']
        pub_file = request.files['pub_file']
        msg_file = request.files['msg_file']

        if (sig_file and allowed_file(sig_file.filename) and
            pub_file and allowed_file(pub_file.filename) and
            msg_file and allowed_file(msg_file.filename)):

            sig_filename = secure_filename(sig_file.filename)
            pub_filename = secure_filename(pub_file.filename)
            msg_filename = secure_filename(msg_file.filename)

            sig_path = os.path.join(app.config['UPLOAD_FOLDER'], sig_filename)
            pub_path = os.path.join(app.config['UPLOAD_FOLDER'], pub_filename)
            msg_path = os.path.join(app.config['UPLOAD_FOLDER'], msg_filename)

            sig_file.save(sig_path)
            pub_file.save(pub_path)
            msg_file.save(msg_path)

            with open(sig_path, 'rb') as f:
                signature = f.read()
            with open(pub_path, 'rb') as f:
                public_key = RSA.import_key(f.read())
            with open(msg_path, 'rb') as f:
                message = f.read()

            hash_obj = SHA256.new(message)
            try:
                pkcs1_15.new(public_key).verify(hash_obj, signature)
                flash('✅ Signature is valid.', 'success')
            except (ValueError, TypeError):
                flash('❌ Signature is invalid or message has been tampered.', 'error')

            os.remove(sig_path)
            os.remove(pub_path)
            os.remove(msg_path)
        else:
            flash('❌ Invalid file types', 'error')

        return redirect(url_for('signature_menu'))

    return render_template('verify_signature.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
