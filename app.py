from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/sm4423', methods=['GET'])
def sm4423():
    return render_template('sm4423.html')

if __name__ == '__main__':
    app.run()
