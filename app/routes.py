from app import app
from flask import flash, render_template, request, redirect, Markup
from .utils import qr_form_handler


@app.route(rule='/', methods=["GET"])
def index():
    user = {'username': 'Любитель нагенерировать код'}
    # flash("This is a flashed message.")
    return render_template(template_name_or_list='gen_1.html', title='Главная')


@app.route(rule='/handler', methods=["POST"])
def handle_data():
    report_type = request.form.get("Report")
    numbers = request.form.get("Serial_numbers")
    # print(request.form["Input1"], request.form["Report"], request.form["Serial_numbers"])
    message = qr_form_handler(report_type, numbers)
    flash(Markup(message))
    # return render_template('gen_1.html', title='Главная')
    return redirect(location='/')
