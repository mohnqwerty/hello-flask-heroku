from flask import Flask
app = Flask(__name__)

@app.route('/poc')
def hello_world():
    return 'takeover by pacmanx'

if __name__ == '__main__':
    app.run()
