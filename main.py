from flask import Flask, render_template, request

app = Flask(__name__)
fileList = []

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/call_upload')
def call_upload():
    return render_template('upload.html')

@app.route('/upload',methods = ['POST'])
def upload():
    file = request.files['inputFile']
    global fileList
    fileList.append(file.filename)
    file.save(file.filename)
    return render_template('index.html',fileList = fileList)

@app.route('/text', methods = ['GET'])
def text():
    name = request.args.get('name')
    f = open(name,'r')
    text = f.read()
    return text
if __name__ == '__main__':
     app.run()
