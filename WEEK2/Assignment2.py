from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def Calculator():
    return """
    <style>
        body {
            background: linear-gradient(109.6deg, rgb(0, 0, 0) 11.2%, rgb(11, 132, 145) 91.1%);
            color:#fbf2d5
        }
        #calculator {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }

        #display {
            font-size: 20px;
            text-align: center;
            height: 40px;
            width: 200px;
            margin-bottom: 10px;
        }

        .button-row {
            display: flex;
            justify-content: center;
        }

        .button {
            margin: 5px;
            width: 50px;
            height: 50px;
            font-size: 20px;
        }

        #result {
            font-size: 20px;
            margin-top: 10px;
        }
    </style>
    <div id="calculator">
        <input type="text" id="display" name="cal" placeholder="Enter expression" readonly>
        <div class="button-row">
            <button class="button" onclick="updateDisplay('1')">1</button>
            <button class="button" onclick="updateDisplay('2')">2</button>
            <button class="button" onclick="updateDisplay('3')">3</button>
            <button class="button" onclick="updateDisplay('+')">+</button>
        </div>
        <div class="button-row">
            <button class="button" onclick="updateDisplay('4')">4</button>
            <button class="button" onclick="updateDisplay('5')">5</button>
            <button class="button" onclick="updateDisplay('6')">6</button>
            <button class="button" onclick="updateDisplay('-')">-</button>
        </div>
        <div class="button-row">
            <button class="button" onclick="updateDisplay('7')">7</button>
            <button class="button" onclick="updateDisplay('8')">8</button>
            <button class="button" onclick="updateDisplay('9')">9</button>
            <button class="button" onclick="updateDisplay('*')">*</button>
        </div>
        <div class="button-row">
            <button class="button" onclick="updateDisplay('0')">0</button>
            <button class="button" onclick="updateDisplay('/')">/</button>
            <button class="button" onclick="clearDisplay()">C</button>
            <button class="button" onclick="calculate()">=</button>
        </div>
        <div id="result"></div>
    </div>

    <script>
        function updateDisplay(value) {
            document.getElementById('display').value += value;
        }

        function clearDisplay() {
            document.getElementById('display').value = '';
            document.getElementById('result').innerText = '';
        }

        function calculate() {
            var expression = document.getElementById('display').value;
            var result = eval(expression);
            document.getElementById('result').innerText = 'Result: ' + result;
        }
    </script>
    """


@app.route("/calculate", methods=["POST"])
def calculate():
    oper = request.form['cal']
    result = str(eval(oper))
    return """
    <style>
        #result { font-size: 20px; margin-left: 10px;}
    </style>
    <span id="result">Result: {}</span>
    """.format(result)


if __name__ == '__main__':
    app.run(debug=True)
