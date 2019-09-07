from flask import Flask, request #imports Flask and request classes from flask module
from caesar import rotate_character, encrypt    #imports rotate_character and encrypt classes from caesar module

app = Flask(__name__)   #app will be object created by constructor Flask; __name__ 
                        #is variable controlled by Python that tells code what module it's in
app.config['DEBUG'] = True  #DEBUG configuration setting for Flask application is enabled so it 
                            #can display errors in browser and ensures file changes are reloaded while erver is running

form = """
<!doctype html>
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
        <!--create your form here-->
        <form method="POST">
            <label>Rotate by: 
                <input name="rot" type="text" value="0" />
            </label>

            <br>
            <br>

            <label>Enter your sentence below: 
                <textarea name="text">{0}</textarea>
            </label>

            <br>
            <br>

            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/") #decorator: creates a mapping between the path, in this case root or / and 
                #function that's about to be defined below
def index():    #define index as a function with 0 variables
        return form.format('')    #function returns the form

#encrypt the old message to the new message by rotating it a certain number of characters
@app.route('/', methods=['POST'])
def encrypt_message():
    rotstr = request.form['rot']
    rot = int(rotstr)
    text = request.form['text']
    new_text = encrypt(text, rot)
    return form.format(new_text)

app.run()   #pass control to Flask object; run function loops forever & never returns so it has 
            #to go last; carries out responsibilities of web server, listening for requests & 
            #sending responses over a network connection