from flask import Blueprint, redirect, request, render_template, url_for
from controllers.partido_controller import *
from controllers.equipo_controller import ver_equipos
from controllers.estadio_controller import ver_estadios
from utils.auth import login_required

partido_bp = Blueprint('partido', __name__)

@partido_bp.route('/partidos/crear', methods=['POST'])
@login_required
def crearPartido():
    data = request.form.to_dict()
    try:
        nuevo_partido = crear_partido(data)
        return redirect(url_for('partido.obtenerPartidos'))
    except ValueError as e:
        equipos= ver_equipos()
        estadios= ver_estadios()
        return render_template('agregarPartido.html', error=str(e), estadios= estadios, equipos= equipos)

@partido_bp.route('/partidos/nuevo')
@login_required
def formularioCrear():
    equipos= ver_equipos()
    estadios= ver_estadios()
    return render_template('agregarPartido.html', estadios= estadios, equipos= equipos)

@partido_bp.route('/partidos', methods=['GET'])
@login_required
def obtenerPartidos():
    partidos= obtener_partidos()
    return render_template('partidos.html', partidos=partidos) 

@partido_bp.route('/partidos/<int:partido_id>/editar', methods=['GET'])
@login_required
def formularioEditar(partido_id):
    partido = obtener_partido(partido_id)
    equipos= ver_equipos()
    estadios= ver_estadios()
    return render_template('actualizarPartido.html', partido=partido, equipos= equipos, estadios=estadios)

@partido_bp.route('/partidos/<int:partido_id>', methods=['GET'])
@login_required
def obtenerPartido(partido_id):
    partido = obtener_partido(partido_id)
    return render_template('partidos.html', partido=partido)

@partido_bp.route('/partidos/<int:partido_id>', methods=['POST'])
@login_required
def actualizarPartido(partido_id):
    data = request.form.to_dict()
    try:
        actualizar_partido(partido_id, data)
        return redirect(url_for('partido.obtenerPartidos'))
    except ValueError as e:
        partido = obtener_partido(partido_id)
        equipos= ver_equipos()
        estadios= ver_estadios()
        return render_template('actualizarPartido.html', partido=partido, error=str(e), equipos= equipos, estadios=estadios)

@partido_bp.route('/partidos/<int:partido_id>/eliminar')
@login_required
def eliminarPartido(partido_id):
    eliminar_partido(partido_id)
    return redirect(url_for('partido.obtenerPartidos'))

@partido_bp.route('/suspendidos')
@login_required
def partidosSuspendidos():
    suspendidos = obtener_suspendidos()
    return render_template('suspendidos.html', partidos=suspendidos)

@partido_bp.route('/suspendidos/<int:partido_id>/reprogramar', methods=['GET'])
@login_required
def formularioReprogramar(partido_id):
    partido = obtener_partido(partido_id)
    estadios= ver_estadios()
    return render_template('reprogramar.html', partido=partido, estadios= estadios)

@partido_bp.route('/suspendidos/<int:partido_id>/reprogramar', methods=['POST'])
@login_required
def reprogramarPartido(partido_id):
    try:
        reprogramar_partido(partido_id, request.form['fecha'], request.form['hora'], request.form['id_estadio'])
        return redirect(url_for('partido.partidosSuspendidos'))
    except ValueError as e:
        partido = obtener_partido(partido_id)
        estadios= ver_estadios()
        return render_template('reprogramar.html', partido=partido, error=str(e), estadios=estadios)
    
@partido_bp.route("/general", methods=["GET"])
@login_required
def partidosproximos():
    destacado, lista, clima = partidos_proximos()
    return render_template("general.html", destacado=destacado,partidos=lista, clima = clima)
    
