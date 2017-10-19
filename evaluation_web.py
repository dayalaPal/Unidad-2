from flask import Flask, render_template, request, redirect
from circulo import ecu, ecu2

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Evaluacion')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    r = float(request.form['r'])
    z = float(request.form['z'])
    title = 'This is the equation\'s result'
    result = ecu(r)
    result2= ecu2(z)
    return render_template('result.html',
                           the_title=title,
                           the_r=r,
                           the_z=z,
                           the_result=result,
                           the_result2= result2)


if __name__ == '__main__':
    app.run(debug=True)
