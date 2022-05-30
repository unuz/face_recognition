from flask import Flask, render_template, Response
import deepface_test
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deepface_test', methods=['get', 'post'])
def deepfaceTest():
    obj = deepface_test.deepface();
    print("index.py : ", obj)
    return render_template('index.html', obj = obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)