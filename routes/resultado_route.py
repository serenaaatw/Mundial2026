from flask import Blueprint,render_template, request, redirect, url_for
from controllers.resultado_controller import *

resultado_bp = Blueprint('resultado', __name__)

#listamos resultados
@resultado_bp.route('/resultados', methods=['GET'])
def obtenerResultados():
    resultados = obtener_Resultados()
    return render_template('resultados.html', resultados=resultados)

#creamos formulario
@resultado_bp.route('/resultados/nuevo')
def formularioCrear():
    return render_template('agregarResultado.html')

#crear
@resultado_bp.route('/resultados/crear', methods=['POST'])
def crearResultado():
    data = request.form.to_dict()
    crear_resultado(data['partido_id'],int(data['goles_equipo1']),int(data['goles_equipo2']))
    return redirect(url_for('resultado.obtenerResultados'))

#form editar:
@resultado_bp.route('/resultados/<int:id_res>/editar', methods=['GET'])
def formularioEditar(id_res):
    resultado = obtener_resultado(id_res)
    return render_template('actualizarResultado.html', resultado=resultado)

#"actualizar:"
@resultado_bp.route('/resultados/<int:id_res>/editar', methods=['POST'])
def actualizarResultado(id_res):
    data = request.form.to_dict()
    actualizar_resultado(id_res, int(data['goles_equipo1']), int(data['goles_equipo2']))
    return redirect(url_for('resultado.obtenerResultados'))

#eliminar
@resultado_bp.route('/resultados/<int:id_res>/eliminar')
def eliminarResultado(id_res):
    eliminar_resultado(id_res)
    return redirect(url_for('resultado.obtenerResultados'))


