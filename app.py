from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-segitiga', methods=['POST'])
def generate_segitiga():
    number = int(request.json['number'])
    triangle = []
    current = 10
    while current <= number:
        triangle.append(str(current).ljust(len(str(number)), '0'))
        current *= 10
    return jsonify(triangle)

@app.route('/generate-ganjil', methods=['POST'])
def generate_ganjil():
    number = int(request.json['number'])
    odds = [i for i in range(1, number+1, 2)]
    return jsonify(odds)

@app.route('/generate-prima', methods=['POST'])
def generate_prima():
    number = int(request.json['number'])
    primes = [i for i in range(2, number+1) if is_prime(i)]
    return jsonify(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
