from func import GetState
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    state=GetState()
    if state[0] < 4:
        return "<html><img src='"+url_for('static',filename='g.jpg')+"'><p>"+str(state[1])+"</html>"
    if state[0] < 7:
        return "<html><img src='"+url_for('static',filename='y.jpg')+"'><p>"+str(state[1])+"</html>"
    return "<html><img src='"+url_for('static',filename='r.jpg')+"'><p>"+str(state[1])+"</html>"
app.run()
