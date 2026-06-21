from flask import Blueprint,render_template, request, redirect, url_for
from controllers.resultado_controller import *
from controllers.partido_controller import *
from controllers.equipo_controller import *
from utils.auth import login_required


resultado_bp = Blueprint('resultado', __name__)

#listamos resultados
@resultado_bp.route('/resultados', methods=['GET'])
@login_required
def obtenerResultados():
    try:
        resultados = obtener_Resultados()
        return render_template('resultados.html', resultados=resultados)
    except ValueError as e:
        return render_template("agregarResultado.html", error=str(e))
        
#creamos formulario

@resultado_bp.route('/resultados/nuevo')
@login_required
def formularioCrear():
    partidos = obtener_partidos() 
    return render_template('agregarResultado.html', partidos=partidos)

#crear
@resultado_bp.route('/resultados/crear', methods=['POST'])
@login_required
def crearResultado():
    data = request.form.to_dict()
    try: 
        crear_resultado(int(data['partido_id']),int(data['goles_equipo1']),int(data['goles_equipo2']))
        return redirect(url_for('resultado.obtenerResultados'))
    except ValueError as e:
        return render_template("agregarResultado.html", error=str(e))

#form editar:
@resultado_bp.route('/resultados/<int:id_res>/editar', methods=['GET'])
@login_required
def formularioEditar(id_res):
    resultado = obtener_resultado(id_res)
    if not resultado:
        resultados = obtener_Resultados()
        return render_template('resultados.html', resultados=resultados, erroreditar="Resultado no encontrado o inexistente")
    partido = Partido.query.get(resultado.partido_id)

    equipo1 = Equipo.query.get(partido.id_equipo1)
    equipo2 = Equipo.query.get(partido.id_equipo2)

    resultado.nombre_equipo1 = equipo1.pais
    resultado.nombre_equipo2 = equipo2.pais
    return render_template('actualizarResultado.html', resultado=resultado)

#"actualizar:"
@resultado_bp.route('/resultados/<int:id_res>/editar', methods=['POST'])
@login_required
def actualizarResultado(id_res):
    data = request.form.to_dict()
    actualizar_resultado(id_res, int(data['goles_equipo1']), int(data['goles_equipo2']))
    return redirect(url_for('resultado.obtenerResultados'))

#eliminar
@resultado_bp.route('/resultados/<int:id_res>/eliminar')
@login_required
def eliminarResultado(id_res):
    eliminar_resultado(id_res)
    return redirect(url_for('resultado.obtenerResultados'))


