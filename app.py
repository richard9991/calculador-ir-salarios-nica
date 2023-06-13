from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        salario_mensual = int(request.form['salario'])
        inns_laboral = salario_mensual * 0.07
        base_imponible = salario_mensual - inns_laboral
        salario_anual = base_imponible * 12

        if salario_anual <= 100000:
            salario_deducible = salario_anual - 0
            porcentaje_aplicable = salario_deducible
            impuesto_aplicable = 0
            ir_anual = porcentaje_aplicable + impuesto_aplicable
            ir_mensual = ir_anual / 12
            ir_diario = ir_mensual / 30

        elif salario_anual <= 200000:
            salario_deducible = salario_anual - 100000
            porcentaje_aplicable = salario_deducible * 0.15
            impuesto_aplicable = 0
            ir_anual = porcentaje_aplicable + impuesto_aplicable
            ir_mensual = ir_anual / 12
            ir_diario = ir_mensual / 30

# lo qu ese hace aki es que va de 2000000 ah 350000 y este que se aplica la baesse impoonible y est los datos que ocmo el 0.20

        elif salario_anual <= 350000:
            salario_deducible = salario_anual - 200000
            porcentaje_aplicable = salario_deducible * 0.20
            impuesto_aplicable = 15000
            ir_anual = porcentaje_aplicable + impuesto_aplicable
            ir_mensual = ir_anual / 12
            ir_diario = ir_mensual / 30
# lo que se hace akii es que  va de 350000 ah 500000 y este lo que se le aplilca es  lo que se le aplico la ves pasada 

        elif salario_anual <= 500000:
            salario_deducible = salario_anual - 350000
            porcentaje_aplicable = salario_deducible * 0.25
            impuesto_aplicable = 45000
            ir_anual = porcentaje_aplicable + impuesto_aplicable
            ir_mensual = ir_anual / 12
            ir_diario = ir_mensual / 30
# lo que se hace aki es que va de 500000 ah mas y lo que se hace es que se le apllica el 0.30 a mas para las retenciones y este que tiene una base imponible de 
#82500 y este que un deducible de 500000 al ano todo para calcular el ir que es lo que importa 
        elif salario_anual >= 500000:
            salario_deducible = salario_anual - 500000
            porcentaje_aplicable = salario_deducible * 0.30
            impuesto_aplicable = 82500
            ir_anual = porcentaje_aplicable + impuesto_aplicable
            ir_mensual = ir_anual / 12
            ir_diario = ir_mensual / 30

        return render_template('calculator.html', salario_mensual=salario_mensual, inns_laboral=inns_laboral,
                               ir_anual=ir_anual, ir_mensual=ir_mensual, ir_diario=ir_diario)

    return render_template('calculator.html')
# para que sse ejecute lo que se le tiene que dar es que el run ell ejecute y seguir el enlace que te brincda con el puerto de ( 5000)


if __name__ == '__main__':
    app.run()
