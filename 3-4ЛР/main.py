from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
temporary_storage = []
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", len = len(temporary_storage), temporary_storage = temporary_storage)
# Create add_number route
@app.route('/add_number', methods=['POST'])
def add_message():
    # Cleaning list
    temporary_storage.clear()
    try:
        deposit_amount = int(request.form['deposit_amount'])
        deposit_term = int(request.form['deposit_term'])
        interest_rate = float(request.form['interest_rate'])
        if deposit_amount is not None or deposit_term is not None or interest_rate is not None:
            if deposit_amount < 100000000 and deposit_term < 50 and interest_rate < 100:
                # Performing Calculations
                for i in range(1, deposit_term + 1):
                    temporary_variable = (deposit_amount * interest_rate) / 100
                    deposit_amount = round(deposit_amount + temporary_variable, 2)
                    temporary_storage.append(deposit_amount)
    except ValueError:
        pass
    return redirect(url_for('index'))
# Start
if __name__ == "__main__":
    app.run(debug=True)
