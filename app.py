from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return jsonify({'sum': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001, debug=True)
