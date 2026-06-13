from flask import Blueprint, redirect, request, render_template, url_for
from controllers.partido_controller import *

partido_bp = Blueprint('partido', __name__)

@partido_bp.route('/partidos/crear', methods=['POST'])
def crearPartido():
    data = request.form.to_dict()
    try:
        nuevo_partido = crear_partido(data)
        return redirect(url_for('partido.obtenerPartidos'))
    except ValueError as e:
        return render_template('agregarPartido.html', error=str(e))

@partido_bp.route('/partidos/nuevo')
def formularioCrear():
    return render_template('agregarPartido.html')

@partido_bp.route('/partidos', methods=['GET'])
def obtenerPartidos():
    partidos= obtener_partidos()
    return render_template('partidos.html', partidos=partidos) 

@partido_bp.route('/partidos/<int:partido_id>/editar', methods=['GET'])
def formularioEditar(partido_id):
    partido = obtener_partido(partido_id)
    return render_template('actualizarPartido.html', partido=partido)

@partido_bp.route('/partidos/<int:partido_id>', methods=['GET'])
def obtenerPartido(partido_id):
    partido = obtener_partido(partido_id)
    return render_template('partidos.html', partido=partido)

@partido_bp.route('/partidos/<int:partido_id>', methods=['POST'])
def actualizarPartido(partido_id):
    data = request.form.to_dict()
    try:
        actualizar_partido(partido_id, data)
        return redirect(url_for('partido.obtenerPartidos'))
    except ValueError as e:
        partido = obtener_partido(partido_id)
        return render_template('actualizarPartido.html', partido=partido, error=str(e))

@partido_bp.route('/partidos/<int:partido_id>/eliminar')
def eliminarPartido(partido_id):
    eliminar_partido(partido_id)
    return redirect(url_for('partido.obtenerPartidos'))

@partido_bp.route('/suspendidos')
def partidosSuspendidos():
    suspendidos = obtener_suspendidos()
    return render_template('suspendidos.html', partidos=suspendidos)

@partido_bp.route('/suspendidos/<int:partido_id>/reprogramar', methods=['GET'])
def formularioReprogramar(partido_id):
    partido = obtener_partido(partido_id)
    return render_template('reprogramar.html', partido=partido)

@partido_bp.route('/suspendidos/<int:partido_id>/reprogramar', methods=['POST'])
def reprogramarPartido(partido_id):
    try:
        reprogramar_partido(partido_id, request.form['fecha'], request.form['hora'], request.form['id_estadio'])
        return redirect(url_for('partido.partidosSuspendidos'))
    except ValueError as e:
        partido = obtener_partido(partido_id)
        return render_template('reprogramar.html', partido=partido, error=str(e))
    
@partido_bp.route("/general", methods=["GET"])
def partidosproximos():
    partidos = partidos_proximos()
    return render_template("general.html", partidos = partidos)
    
