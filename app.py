from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Chandra Sagar C M"
    username = os.getenv("chandrasagarcm") 
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1")

    return f"<h1>Name: {name}</h1>" \
           f"<h2>Username: {username}</h2>" \
           f"<h2>Server Time (IST): {server_time}</h2>" \
           f"<pre>{top_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
