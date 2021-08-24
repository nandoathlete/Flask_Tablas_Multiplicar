from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getvalue', methods = ['POST'])
def tablaDeMultilplicar():
    if request.method == "POST":
        Number = int(request.form["Number"])
        return render_template('table.html', Number = Number)

if __name__ == '__main__':
    app.run(debug = True)