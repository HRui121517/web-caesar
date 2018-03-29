from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form ="""
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                Rotate by: <input type="number" name="rot" value=0><br><br>
                <textarea name="text" rows="8" cols="50">{0}</textarea><br>
                <input type="submit" value="Submit Query">
            </form>
        </body>
    </html>"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_num = int(request.form['rot'])
    text_to_encrypt = request.form['text']
    encrypttext = rotate_string(text_to_encrypt, rot_num)
    tag = "<h1>"
    tagend="</h1>"
    return form.format(encrypttext)

@app.route("/")
def index():
    return form.format('')

app.run()