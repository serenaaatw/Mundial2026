from flask import Blueprint, request, render_template
from controllers.partido_controller import *

partido_bp = Blueprint('partido', __name__)

@partido_bp.route('/partidos', methods=['POST'])
def crearPartido():
    data = request.form.to_dict()
    nuevo_partido = crear_partido(data)
    return render_template('partido_creado.html', partido=nuevo_partido)

@partido_bp.route('/partidos', methods=['GET'])
def obtenerPartidos():
    partidos= obtener_partidos()
    return render_template('partidos.html', partidos=partidos) 

@partido_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def obtenerPartido(partido_id):
    partido = obtener_partido(partido_id)
    return render_template('partido.html', partido=partido)

@partido_bp.route('/partidos/<int:partido_id>', methods=['PUT'])
def actualizarPartido(partido_id):
    data = request.form.to_dict()
    return render_template('actualizarPartido.html', partido=actualizar_partido(partido_id, data))

@partido_bp.route('/partidos/<int:partido_id>', methods=['DELETE'])
def eliminarPartido(partido_id):
    success= eliminar_partido(partido_id)
    return render_template('partido_eliminado.html', success=success)