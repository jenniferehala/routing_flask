from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<text>')
def say_text(text):
    return f" Hi {text}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return num * word

if __name__=="__main__":  #Ensure file being run directly, not from different module
    app.run(debug=True) # Run the app in debug mode.
