from flask import Blueprint, render_template, request
from controllers.resultado_controller import  *

resultado_bp = Blueprint('resultado', __name__)

@resultado_bp.route('/resultados', methods=['POST'])
def crear_resultado_route():
    data = request.get_json()
    partido_id = data.get('partido_id')
    goles_equipo1 = data.get('goles_equipo1')
    goles_equipo2 = data.get('goles_equipo2')
    return crear_resultado(partido_id, goles_equipo1, goles_equipo2)

@resultado_bp.route('/resultados', methods=['GET'])
def obtener_resultados_route():
    return obtener_Resultados()

@resultado_bp.route('/resultados/<int:id_res>', methods=['GET'])
def obtener_resultado_route(id_res):
    return obtener_resultado(id_res)

@resultado_bp.route('/resultados/<int:id_res>', methods=['PUT'])
def actualizar_resultado_route(id_res):
    data = request.get_json()
    goles_equipo1 = data.get('goles_equipo1')
    goles_equipo2 = data.get('goles_equipo2')
    return actualizar_resultado(id_res, goles_equipo1, goles_equipo2)

@resultado_bp.route('/resultados/<int:id_res>', methods=['DELETE'])
def eliminar_resultado_route(id_res):
    return eliminar_resultado(id_res)
