from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('index.html', name=name, email=email)
    return render_template('index.html', name=None, email=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)