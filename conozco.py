#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Conozco
# Copyright (C) 2008, 2012 Gabriel Eirea
# Copyright (C) 2011, 2012 Alan Aguiar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Gabriel Eirea geirea@gmail.com
# Alan Aguiar alanjas@hotmail.com
# Ceibal Jam

import os
import random
import time
import importlib.util
import gettext
import configparser
from gettext import gettext as _
import pygame
gtk_present = True
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except (ImportError, ValueError):
    gtk_present = False

# constantes
RADIO = 10
XMAPAMAX = 786
DXPANEL = 414
XCENTROPANEL = 1002
YGLOBITO = 100
DXBICHO = 255
DYBICHO = 412
XBICHO = 1200-DXBICHO
YBICHO = 900-DYBICHO-80
XPUERTA = 786
YPUERTA = 279
XBARRA_P = 840
YBARRA_P = 790
ABARRA_P = 40
YTEXTO = 370
XBARRA_A = XMAPAMAX+20
YBARRA_A = 900 - ABARRA_P - 20
ABARRA_A = DXPANEL-40
# control
TOTALAVANCE = 7
TIEMPORESPUESTA = 2300
TIEMPOREFRESCO = 250
ESTADONORMAL = 1
ESTADOPESTANAS = 2
ESTADOFRENTE = 3
ESTADODESPEGUE = 4
# paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINORECURSOS = os.path.join(BASE_DIR, "recursos")
CAMINOCOMUN = "comun"
CAMINOFUENTES = "fuentes"
CAMINODATOS = "datos"
CAMINOIMAGENES = "imagenes"
CAMINOSONIDOS = "sonidos"

ARCHIVONIVELES = "levels"
ARCHIVOEXPLORACIONES = "explorations"
# colors
COLORNOMBREDEPTO = (10, 10, 10)
COLORNOMBRECAPITAL = (10, 10, 10)
COLORNOMBRERIO = (10, 10, 10)
COLORNOMBRERUTA = (10, 10, 10)
COLORNOMBREELEVACION = (10, 10, 10)
COLORESTADISTICAS1 = (10, 10, 150)
COLORESTADISTICAS2 = (10, 10, 10)
COLORPREGUNTAS = (80, 80, 155)
COLORPANEL = (156, 158, 172)
COLORBARRA_P = (255, 0, 0)
COLORBARRA_A = (0, 0, 255)
COLORBARRA_C = (0, 0, 0)
COLOR_FONDO = (0, 0, 0)
COLOR_ACT_NAME = (255, 255, 255)
COLOR_OPTION_B = (20, 20, 20)
COLOR_OPTION_T = (200, 100, 100)
COLOR_BUTTON_B = (20, 20, 20)
COLOR_BUTTON_T = (100, 200, 100)
COLOR_NEXT = (100, 100, 200)
COLOR_STAT_N = (100, 100, 200)
COLOR_SKIP = (255, 155, 155)
COLOR_CREDITS = (155, 155, 255)
COLOR_SHOW_ALL = (100, 20, 20)

# Categoria: lista, fuente, color, tipos de punto, imagen, tipo de pregunta.
CATEGORIAS = {
    "deptos": ("listaDeptos", "fuente32", COLORNOMBREDEPTO,
               None, "deptosLineas", 1),
    "rios": ("listaRios", "fuente24", COLORNOMBRERIO,
             None, "rios", 3),
    "rutas": ("listaRutas", "fuente24", COLORNOMBRERUTA,
              None, "rutas", 6),
    "cuchillas": ("listaCuchillas", "fuente24", COLORNOMBREELEVACION,
                  None, "cuchillas", 4),
    "capitales": ("listaLugares", "fuente24", COLORNOMBRECAPITAL,
                  (0, 1), None, 2),
    "ciudades": ("listaLugares", "fuente24", COLORNOMBRECAPITAL,
                 (2,), None, 2),
    "cerros": ("listaLugares", "fuente24", COLORNOMBREELEVACION,
               (5,), None, 5),
}

# variables globales para adaptar la pantalla a distintas resoluciones
scale = 1
shift_x = 0
shift_y = 0
xo_resolution = True


def escalar(valor):
    """Escala una longitud y conserva el truncamiento a pixeles enteros"""
    return int(valor * scale)

def coordenada_x(x):
    """Convierte una coordenada horizontal del lienzo base a la pantalla"""
    return int(x * scale + shift_x)

def coordenada_y(y):
    """Convierte una coordenada vertical del lienzo base a la pantalla"""
    return int(y * scale + shift_y)

def posicion(x, y):
    """Convierte una posicion del lienzo de 1200 x 900 a la pantalla"""
    return coordenada_x(x), coordenada_y(y)

def rectangulo(x, y, ancho, alto):
    """Convierte un rectangulo base; el desplazamiento solo afecta al origen"""
    return pygame.Rect(*posicion(x, y), escalar(ancho), escalar(alto))

clock = pygame.time.Clock()

def load_source(modname, filename):
    spec = importlib.util.spec_from_file_location(modname, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Punto():
    """Clase para objetos geograficos que se pueden definir como un punto.

    La posicion esta dada por un par de coordenadas (x,y) medida en pixels
    dentro del mapa.
    """

    def __init__(self, nombre, tipo, simbolo, posicion, postexto):
        self.nombre = nombre
        self.tipo = int(tipo)
        self.posicion = (coordenada_x(int(posicion[0])),
                         coordenada_y(int(posicion[1])))
        self.postexto = (escalar(int(postexto[0]))+self.posicion[0],
                         escalar(int(postexto[1]))+self.posicion[1])
        self.simbolo = simbolo

    def estaAca(self, pos):
        """Devuelve un booleano indicando si esta en la coordenada pos,
        la precision viene dada por la constante global RADIO"""
        radio = RADIO * scale
        dx = pos[0] - self.posicion[0]
        dy = pos[1] - self.posicion[1]

        return dx * dx + dy * dy < radio * radio

    def dibujar(self, pantalla):
        """Dibuja un punto en su posicion"""
        rect = self.simbolo.get_rect(center=self.posicion)
        pantalla.blit(self.simbolo, rect)

    def mostrarNombre(self, pantalla, fuente, color):
        """Escribe el nombre del punto en su posicion"""
        text = fuente.render(self.nombre, 1, color)
        textrect = text.get_rect()
        textrect.center = (self.postexto[0], self.postexto[1])
        pantalla.blit(text, textrect)


class Zona():
    """Clase para objetos geograficos que se pueden definir como una zona.

    La posicion esta dada por una imagen bitmap pintada con un color
    especifico, dado por la clave (valor 0 a 255 del componente rojo).
    """

    def __init__(self, mapa, nombre, claveColor, tipo, posicion, rotacion):
        self.mapa = mapa  # esto hace una copia en memoria o no????
        self.nombre = nombre
        self.claveColor = int(claveColor)
        self.tipo = int(tipo)
        self.posicion = (coordenada_x(int(posicion[0])),
                         coordenada_y(int(posicion[1])))
        self.rotacion = int(rotacion)

    def estaAca(self, pos):
        """Devuelve True si la coordenada pos esta en la zona"""
        if pos[0] < XMAPAMAX*scale+shift_x:
            try:
                colorAca = self.mapa.get_at((int(pos[0]-shift_x),
                                             int(pos[1]-shift_y)))
            except:  # probablemente click fuera de la imagen
                return False
            if colorAca[0] == self.claveColor:
                return True
            else:
                return False
        else:
            return False

    def mostrarNombre(self, pantalla, fuente, color):
        """Escribe el nombre de la zona en su posicion"""
        text = fuente.render(self.nombre, 1, color)
        textrot = pygame.transform.rotate(text, self.rotacion)
        textrect = textrot.get_rect()
        textrect.center = (self.posicion[0], self.posicion[1])
        pantalla.blit(textrot, textrect)


class Nivel():
    """Clase para definir los niveles del juego.

    Cada nivel tiene un dibujo inicial, los elementos pueden estar
    etiquetados con el nombre o no, y un conjunto de preguntas.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.dibujoInicial = []
        self.nombreInicial = []
        self.preguntas = []
        self.indicePreguntaActual = 0
        self.elementosActivos = []

    def prepararPreguntas(self):
        """Este metodo sirve para preparar la lista de preguntas al azar."""
        random.shuffle(self.preguntas)
        self.indicePreguntaActual = 0

    def siguientePregunta(self, listaSufijos, listaPrefijos):
        """Prepara el texto de la pregunta siguiente"""
        self.preguntaActual = self.preguntas[self.indicePreguntaActual]
        lineas = random.choice(listaPrefijos).split("\n")
        lineas.extend(self.preguntaActual[0].split("\n"))
        lineas.extend(random.choice(listaSufijos).split("\n"))
        self.indicePreguntaActual = self.indicePreguntaActual+1
        if self.indicePreguntaActual == len(self.preguntas):
            self.indicePreguntaActual = 0
        return lineas

    def devolverAyuda(self):
        """Devuelve la linea de ayuda"""
        self.preguntaActual = self.preguntas[self.indicePreguntaActual-1]
        return self.preguntaActual[3].split("\n")


class Conozco():
    """Clase principal del juego.

    """

    def change_sound(self, enabled):
        """Enable sound only when the audio device and sample are available."""
        self.sound = bool(enabled and self.click is not None)
        return self.sound

    def mostrarTexto(self, texto, fuente, posicion, color):
        """Muestra texto en una determinada posicion"""
        text = fuente.render(texto, 1, color)
        textrect = text.get_rect()
        textrect.center = posicion
        self.pantalla.blit(text, textrect)

    def loadInfo(self):
        """Carga las imagenes y los datos de cada pais"""
        
        # creo todas las listas
        self.listaLugares = []
        self.listaDeptos = []
        self.listaRios = []
        self.listaRutas = []
        self.listaCuchillas = []
        self.lista_estadisticas = []
        # mapas
        self.deptos = None
        self.deptosLineas = None
        self.rios = None
        self.rutas = None
        self.cuchillas = None
        
        path = os.path.join(self.camino_datos, self.directorio + '.py')
        f = None
        try:
            f = load_source(self.directorio, path)
        except (OSError, ImportError, SyntaxError) as err:
            print(_('Cannot open %s') % path, err)

        if f:
            simbolos = {
                0: self.simboloCapitalN,
                1: self.simboloCapitalD,
                2: self.simboloCiudad,
                5: self.simboloCerro,
            }
            for categoria in ('CAPITALS', 'CITIES', 'HILLS'):
                for nombre, x, y, tipo, incx, incy in getattr(f, categoria, []):
                    simbolo = simbolos.get(tipo, self.simboloCiudad)
                    self.listaLugares.append(
                        Punto(nombre, tipo, simbolo, (x, y), (incx, incy)))

            # Datos, lista de destino, imagen visible, mascara de deteccion, tipo.
            zonas = (
                ('STATES', 'listaDeptos', 'deptosLineas', 'deptos', 1),
                ('CUCHILLAS', 'listaCuchillas', 'cuchillas', 'cuchillasDetectar', 4),
                ('RIVERS', 'listaRios', 'rios', 'riosDetectar', 3),
                ('ROUTES', 'listaRutas', 'rutas', 'rutasDetectar', 6),
            )
            for categoria, lista, imagen, mascara, tipo in zonas:
                if hasattr(f, categoria):
                    self._cargar_zonas(getattr(f, categoria), lista,
                                       imagen, mascara, tipo)
            
            if hasattr(f, 'STATS'):
                for e in f.STATS:
                    p1 = e[0]
                    p2 = e[1]
                    self.lista_estadisticas.append((p1, p2))

    def _cargar_zonas(self, datos, lista, imagen, mascara, tipo):
        """Carga las imagenes y crea las zonas de una categoria geografica"""
        setattr(self, imagen, self.cargarImagen(imagen + '.png'))
        mapa = self.cargarImagen(mascara + '.png')
        setattr(self, mascara, mapa)
        setattr(self, lista, [
            Zona(mapa, nombre, clave, tipo, (x, y), rotacion)
            for nombre, clave, x, y, rotacion in datos
        ])

    def cargarListaDirectorios(self):
        """Carga la lista de directorios con los distintos mapas"""
        self.listaDirectorios = []
        self.listaNombreDirectorios = []
        listaTemp = os.listdir(CAMINORECURSOS)
        listaTemp.sort()
        for d in listaTemp:
            if not (d == 'comun'):
                path = os.path.join(CAMINORECURSOS, d, 'datos', d + '.py')
                f = None
                try:
                    f = load_source(d, path)
                except:
                    print(_('Cannot open %s') % d)

                if hasattr(f, 'NAME'):
                    name = f.NAME
                    self.listaNombreDirectorios.append(name)
                    self.listaDirectorios.append(d)

    def loadCommons(self):
        """Carga los recursos en comun"""
        path = os.path.join(CAMINORECURSOS, CAMINOCOMUN, 'datos', 'commons.py')
        data = load_source('commons', path)
        self.activity_name = getattr(data, 'ACTIVITY_NAME', self.activity_name)
        attributes = {
            'listaPrefijos': 'PREFIX',
            'listaSufijos': 'SUFIX',
            'listaCorrecto': 'CORRECT',
            'listaMal': 'WRONG',
            'listaDespedidasB': 'BYE_C',
            'listaDespedidasM': 'BYE_W',
            'listaPresentacion': 'PRESENTATION',
            'listaCreditos': 'CREDITS',
        }
        for attribute, source in attributes.items():
            setattr(self, attribute, list(getattr(data, source, [])))

    def cargarNiveles(self):
        """Carga los niveles del archivo de configuracion"""
        path = os.path.join(self.camino_datos, ARCHIVONIVELES + '.py')
        data = load_source(ARCHIVONIVELES, path)
        templates = {
            2: (2, _('the city of\n%s')),
            7: (1, _('the department of\n%s')),
            8: (1, _('the province of\n%s')),
            9: (1, _('the district of\n%s')),
            10: (1, _('the state of\n%s')),
            11: (1, _('the region of\n%s')),
            12: (1, _('the parish of\n%s')),
            14: (1, _('the taluka of\n%s')),
            6: (1, _('the municipality of\n%s')),
            4: (3, _('the %s')),
            5: (6, _('the %(route)s')),
        }
        self.listaNiveles = []
        for index, name, drawings, labels, questions in data.LEVELS:
            level = Nivel(str(name))
            level.dibujoInicial = [item.strip() for item in drawings]
            level.nombreInicial = [item.strip() for item in labels]
            if index == 1:
                level.preguntas = [
                    (text, kind, str(answer), str(hint))
                    for text, kind, answer, hint in questions
                ]
            else:
                if index not in templates:
                    raise ValueError(f'Unknown level type {index} in {path}')
                kind, template = templates[index]
                level.preguntas = [
                    (template % ({'route': answer} if index == 5 else answer),
                     kind, answer, hint)
                    for answer, hint in questions
                ]
            if not level.preguntas:
                raise ValueError(f'Empty level {name!r} in {path}')
            self.listaNiveles.append(level)

        self.indiceNivelActual = 0

    def cargarExploraciones(self):
        """Carga los niveles de exploracion del archivo de configuracion"""
        path = os.path.join(self.camino_datos, ARCHIVOEXPLORACIONES + '.py')
        data = load_source(ARCHIVOEXPLORACIONES, path)
        self.listaExploraciones = []
        for name, drawings, labels, active in data.EXPLORATIONS:
            level = Nivel(name)
            level.dibujoInicial = [item.strip() for item in drawings]
            level.nombreInicial = [item.strip() for item in labels]
            level.elementosActivos = [item.strip() for item in active]
            self.listaExploraciones.append(level)

    def _process_gtk_events(self):
        """Procesa los eventos de Sugar cuando GTK esta disponible"""
        if gtk_present:
            while Gtk.events_pending():
                Gtk.main_iteration()

    def _get_events(self):
        """Limita los fotogramas y obtiene un lote de eventos en orden"""
        clock.tick(20)
        self._process_gtk_events()
        return pygame.event.get()

    def _play_click(self):
        """Reproduce el sonido de la accion si esta habilitado"""
        if self.sound:
            self.click.play()

    def _close_game(self, close_activity=False):
        """Finaliza la partida y guarda una sola vez antes de cerrar."""
        if not self.running:
            return
        self._finish_game()
        self.running = False
        self._deadline = None
        self.save_stats()
        if close_activity and self.parent is not None:
            self.parent.close(skip_save=True)


    def pantallaAcercaDe(self):
        """Pantalla con los datos del juego, creditos, etc"""
        self.pantalla.fill(COLOR_FONDO)
        self.pantalla.blit(self.terron,
                           posicion(20, 20))
        self.pantalla.blit(self.jp1,
                           posicion(925, 468))
        self.mostrarTexto(_("About %s") % self.activity_name,
                          self.fuente40,
                          posicion(600, 100),
                          COLOR_ACT_NAME)

        yLinea = coordenada_y(200)
        for linea in self.listaCreditos:
            self.mostrarTexto(linea.strip(),
                              self.fuente32,
                              (coordenada_x(600), yLinea),
                              COLOR_CREDITS)
            yLinea = yLinea + escalar(40)

        self.mostrarTexto(_("Press any key to return"),
                          self.fuente32,
                          posicion(600, 800),
                          COLOR_SKIP)

    def pantallaStats(self):
        """Pantalla con los datos del juego, creditos, etc"""
        self.pantalla.fill(COLOR_FONDO)
        self.pantalla.blit(self.jp1,
                           posicion(925, 468))
        msg = _("Stats of %s") % self.activity_name
        self.mostrarTexto(msg,
                          self.fuente40,
                          posicion(600, 100),
                          COLOR_ACT_NAME)
        minutos = int((time.monotonic() - self._init_time) / 60) + self._time
        estadisticas = (
            (_('Total score: %s'), self._score),
            (_('Game average score: %s'), self._average),
            (_('Times using Explore Mode: %s'), self._explore_times),
            (_('Places Explored: %s'), self._explore_places),
            (_('Times using Game Mode: %s'), self._game_times),
            (_('Total time: %s minutes'), minutos),
        )
        for indice, (texto, valor) in enumerate(estadisticas):
            self.mostrarTexto(texto % valor, self.fuente32,
                              posicion(400, 300 + indice * 50), COLOR_STAT_N)

        self.mostrarTexto(_("Press any key to return"),
                          self.fuente32,
                          posicion(600, 800),
                          COLOR_SKIP)

    def _draw_footer(self, last_label):
        rectangles = []
        for x, label in zip((20, 420, 820),
                            (_("About this game"), _("Stats"), last_label)):
            rect = rectangulo(x, 801, 370, 48)
            self.pantalla.fill(COLOR_BUTTON_B, rect)
            self.mostrarTexto(label, self.fuente40, rect.center, COLOR_BUTTON_T)
            rectangles.append(rect)
        return rectangles
        
    def _draw_menu_option(self, texto, x, y, color):
        """Dibuja una opcion y devuelve su zona clicable"""
        rect = pygame.Rect(coordenada_x(x), y-escalar(24),
                           escalar(590), escalar(48))
        self.pantalla.fill(COLOR_OPTION_B, rect)
        self.mostrarTexto(texto, self.fuente40,
                          (coordenada_x(x+290), y), color)
        return rect

    def pantallaInicial(self):
        """Pantalla con el menu principal del juego"""
        self.pantalla.fill(COLOR_FONDO)
        self.mostrarTexto(self.activity_name,
                          self.fuente60,
                          posicion(600, 80),
                          COLOR_ACT_NAME)
        self.mostrarTexto(_("You have chosen the map ") +
                          self.listaNombreDirectorios
                          [self.indiceDirectorioActual],
                          self.fuente40,
                          posicion(600, 140),
                          COLOR_OPTION_T)
        self.mostrarTexto(_("Play"),
                          self.fuente60,
                          posicion(300, 220),
                          COLOR_OPTION_T)

        self.niveles_rect = []
        yLista = coordenada_y(300)
        for n in self.listaNiveles:
            self.niveles_rect.append(self._draw_menu_option(
                n.nombre, 10, yLista, COLOR_OPTION_T))
            yLista += escalar(50)
            
        self.mostrarTexto(_("Explore"),
                          self.fuente60,
                          posicion(900, 220),
                          COLOR_NEXT)

        self.exploraciones_rect = []
        yLista = coordenada_y(300)
        for n in self.listaExploraciones:
            self.exploraciones_rect.append(self._draw_menu_option(
                n.nombre, 610, yLista, COLOR_NEXT))
            yLista += escalar(50)

        # buttons
        self.footer_rects = self._draw_footer(_("Return"))

    def pantallaDirectorios(self):
        """Pantalla con el menu de directorios"""
        self.pantalla.fill(COLOR_FONDO)
        self.mostrarTexto(self.activity_name,
                          self.fuente60,
                          posicion(600, 80),
                          COLOR_ACT_NAME)
        self.mostrarTexto(_("Choose the map to use"),
                          self.fuente40,
                          posicion(600, 140),
                          COLOR_OPTION_T)
        nDirectorios = len(self.listaNombreDirectorios)
        paginaDirectorios = self.paginaDir
        yLista = coordenada_y(200)
        self.pantalla.fill(COLOR_FONDO,
                           (int(shift_x), yLista-escalar(24),
                            escalar(1200), escalar(600)))

        self.opciones = []

        # Página anterior
        if paginaDirectorios > 0:
            rect = self._draw_menu_option(
                "<<< " + _("Previous page"),
                10, yLista, COLOR_NEXT
            )
            self.opciones.append((rect, "anterior", None))

        # Países de la página actual
        inicio = paginaDirectorios * 20
        fin = min(inicio + 20, nDirectorios)

        for local, indice in enumerate(range(inicio, fin)):
            columna = local // 10
            fila = local % 10

            x = 10 + columna * 600
            y = coordenada_y(250 + fila * 50)

            rect = self._draw_menu_option(
                self.listaNombreDirectorios[indice],
                x, y, COLOR_OPTION_T
            )

            self.opciones.append((rect, "mapa", indice))

        # Página siguiente
        if fin < nDirectorios:
            rect = self._draw_menu_option(
                _("Next page") + " >>>",
                610,
                coordenada_y(750),
                COLOR_NEXT
            )
            self.opciones.append((rect, "siguiente", None))

        # buttons
        self.footer_rects = self._draw_footer(_("Exit"))

    def cargarImagen(self, nombre):
        """Carga una imagen y la escala de acuerdo a la resolucion"""
        archivo = os.path.join(self.camino_imagenes, nombre)
        if not os.path.exists(archivo):
            return None
        imagen = pygame.image.load(archivo)
        if not xo_resolution:
            imagen = pygame.transform.scale(imagen,
                         (escalar(imagen.get_width()),
                         escalar(imagen.get_height())))
        return imagen

    def __init__(self, parent=None):
        self.parent = parent
        self.running = True
        self._screen = None
        self._screen_revision = 0
        self._deadline = None
        self._next_refresh = 0
        self._game_active = False
        self.paginaDir = 0
        file_activity_info = configparser.ConfigParser()
        activity_info_path = os.path.join(BASE_DIR, 'activity', 'activity.info')
        file_activity_info.read(activity_info_path)
        bundle_id = file_activity_info.get('Activity', 'bundle_id')
        self.activity_name = file_activity_info.get('Activity', 'name')
        path = os.path.join(BASE_DIR, 'locale')
        gettext.bindtextdomain(bundle_id, path)
        gettext.textdomain(bundle_id)
        global _
        _ = gettext.gettext
        # initial time
        self._init_time = time.monotonic()
        # sound
        self.click = None
        self.sound = False
        # stats
        self._score = 0
        self._average = 0
        self._explore_times = 0
        self._explore_places = 0
        self._game_times = 0
        self._time = 0

    def load_stats(self):
        try:
            path = self._get_stats_path()

            with open(path, 'r', encoding='utf-8') as f:
                l = [int(float(line.strip())) for line in f]

        except FileNotFoundError:
            return  # First run.

        except (OSError, ValueError, TypeError) as err:
            print('Cannot load stats', err)
            return

        # Accept both the old and the new format.
        if not self._validate_stats(l):
            print('Invalid stats file')
            return

        # Old format: 7 values, including average at index 1.
        # Remove the average and the old checksum.
        if len(l) == 7:
            l = [l[0], l[2], l[3], l[4], l[5]]

        else:
            # New format: remove the checksum.
            l = l[:-1]

        self._score = l[0]
        self._explore_times = l[1]
        self._explore_places = l[2]
        self._game_times = l[3]
        self._time = l[4]

        # Calculate average instead of reading it from stats.dat
        if self._game_times > 0:
            self._average = self._score / self._game_times

    def _validate_stats(self, values):
        return (
            len(values) in (6, 7)
            and self._calc_sum(values[:-1]) == values[-1]
        )

    def _calc_sum(self, l):
        return sum(l) % 7

    def _get_stats_path(self):
        if self.parent is not None:
            folder = os.path.join(self.parent.get_activity_root(), 'data')
        else:
            base = os.environ.get('XDG_DATA_HOME', '')
            if not os.path.isabs(base):
                base = os.path.expanduser('~/.local/share')

            folder = os.path.join(base, 'iknowamerica')
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, 'stats.dat')

    def _update_play_time(self):
        elapsed = time.monotonic() - self._init_time
        minutes = int(elapsed // 60)

        if minutes > 0:
            self._time += minutes
            self._init_time += minutes * 60

    def save_stats(self):
        try:
            self._update_play_time()
            path = self._get_stats_path()

            values = [self._score, self._explore_times, self._explore_places,
                      self._game_times, self._time]
            values.append(self._calc_sum(values))

            # save
            f = open(path, 'w')
            for val in values:
                f.write(str(val) + '\n')
            f.close()
        except Exception as err:
            print('Error saving stats', err)

    def loadAll(self):
        global scale, shift_x, shift_y, xo_resolution
        self.pantalla = pygame.display.get_surface()
        if not(self.pantalla):
            info = pygame.display.Info()
            self.pantalla = pygame.display.set_mode(
                (info.current_w, info.current_h), pygame.FULLSCREEN)
            pygame.display.set_caption(_(self.activity_name))
        self.anchoPantalla = self.pantalla.get_width()
        self.altoPantalla = self.pantalla.get_height()
        if self.anchoPantalla == 1200 and self.altoPantalla == 900:
            xo_resolution = True
            scale = 1
            shift_x = 0
            shift_y = 0
        else:
            xo_resolution = False
            if self.anchoPantalla/1200.0 < self.altoPantalla/900.0:
                scale = self.anchoPantalla/1200.0
                shift_x = 0
                shift_y = int((self.altoPantalla-scale*900)/2)
            else:
                scale = self.altoPantalla/900.0
                shift_x = int((self.anchoPantalla-scale*1200)/2)
                shift_y = 0
        # cargar imagenes generales
        self.camino_imagenes = os.path.join(CAMINORECURSOS,
                                            CAMINOCOMUN,
                                            CAMINOIMAGENES)
        imagenes = {
            'fondo1': 'fondo1', 'fondo2': 'fondo2',
            'jpp1': 'jpp1', 'jpp2': 'jpp2',
            'globo1': 'globo1', 'globo3': 'globo3', 'jp1': 'jp1',
            'ojos1': 'ojos1', 'ojos2': 'ojos2', 'ojos3': 'ojos3',
            'puerta1': 'puerta01', 'puerta2': 'puerta02',
            'globito': 'globito', 'terron': 'terron',
            'simboloCapitalD': 'capitalD', 'simboloCapitalN': 'capitalN',
            'simboloCiudad': 'ciudad', 'simboloCerro': 'cerro',
        }
        for atributo, archivo in imagenes.items():
            setattr(self, atributo, self.cargarImagen(archivo + '.png'))
        self.globo2 = pygame.transform.flip(self.globo1, True, False)
        # cargar sonidos
        self.camino_sonidos = os.path.join(CAMINORECURSOS,
                                           CAMINOCOMUN,
                                           CAMINOSONIDOS)
        # check sound
        self.sound = True
        try:
            self.click = pygame.mixer.Sound(os.path.join(
                self.camino_sonidos, "junggle_btn117.wav"))
            self.click.set_volume(0.2)
        except:
            self.sound = False
        # cargar directorios
        self.cargarListaDirectorios()
        # cargar fuentes
        fuente = os.path.join(CAMINORECURSOS, CAMINOCOMUN,
                              CAMINOFUENTES, "Share-Regular.ttf")
        for atributo, archivo, tamano in (
                ('fuente60', fuente, 60), ('fuente40', fuente, 34),
                ('fuente9', fuente, 20), ('fuente32', None, 30),
                ('fuente24', None, 24)):
            setattr(self, atributo, pygame.font.Font(archivo, escalar(tamano)))
        # cursor
        datos_cursor = (
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
            "XXX.........................XXXX",
            "XXX..........................XXX",
            "XXX..........................XXX",
            "XXX.........................XXXX",
            "XXX.......XXXXXXXXXXXXXXXXXXXXX ",
            "XXX........XXXXXXXXXXXXXXXXXXX  ",
            "XXX.........XXX                 ",
            "XXX..........XXX                ",
            "XXX...........XXX               ",
            "XXX....X.......XXX              ",
            "XXX....XX.......XXX             ",
            "XXX....XXX.......XXX            ",
            "XXX....XXXX.......XXX           ",
            "XXX....XXXXX.......XXX          ",
            "XXX....XXXXXX.......XXX         ",
            "XXX....XXX XXX.......XXX        ",
            "XXX....XXX  XXX.......XXX       ",
            "XXX....XXX   XXX.......XXX      ",
            "XXX....XXX    XXX.......XXX     ",
            "XXX....XXX     XXX.......XXX    ",
            "XXX....XXX      XXX.......XXX   ",
            "XXX....XXX       XXX.......XXX  ",
            "XXX....XXX        XXX.......XXX ",
            "XXX....XXX         XXX.......XXX",
            "XXX....XXX          XXX......XXX",
            "XXX....XXX           XXX.....XXX",
            "XXX....XXX            XXX...XXXX",
            " XXX..XXX              XXXXXXXX ",
            "  XXXXXX                XXXXXX  ",
            "   XXXX                  XXXX   ")
        self.cursor = pygame.cursors.compile(datos_cursor)
        pygame.mouse.set_cursor((32, 32), (1, 1), *self.cursor)
        datos_cursor_espera = (
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "  XXXXXX     XXXXXX     XXXXXX  ",
            " XXXXXXXX   XXXXXXXX   XXXXXXXX ",
            "XXXX..XXXX XXXX..XXXX XXXX..XXXX",
            "XXX....XXX XXX....XXX XXX....XXX",
            "XXX....XXX XXX....XXX XXX....XXX",
            "XXX....XXX XXX....XXX XXX....XXX",
            "XXXX..XXXX XXXX..XXXX XXXX..XXXX",
            " XXXXXXXX   XXXXXXXX   XXXXXXXX ",
            "  XXXXXX     XXXXXX      XXXXX  ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ")
        self.cursor_espera = pygame.cursors.compile(datos_cursor_espera)

    def cargarDirectorio(self):
        """Carga la informacion especifica de un directorio"""
        self.camino_imagenes = os.path.join(CAMINORECURSOS,
                                            self.directorio,
                                            CAMINOIMAGENES)
        self.camino_sonidos = os.path.join(CAMINORECURSOS,
                                           self.directorio,
                                           CAMINOSONIDOS)
        self.camino_datos = os.path.join(CAMINORECURSOS,
                                         self.directorio,
                                         CAMINODATOS)
        self.fondo = self.cargarImagen("fondo.png")
        self.bandera = self.cargarImagen("bandera.png")

        self.loadInfo()

        self.cargarNiveles()
        self.cargarExploraciones()

    def mostrarGlobito(self, lineas):
        """Muestra texto en el globito"""
        self.pantalla.blit(self.globito,
                           posicion(XMAPAMAX, YGLOBITO))
        yLinea = escalar(YGLOBITO) + shift_y + \
            self.fuente32.get_height()*3
        for l in lineas:
            text = self.fuente32.render(l, 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (coordenada_x(XCENTROPANEL), yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea + self.fuente32.get_height() + escalar(10)

    def borrarGlobito(self):
        """ Borra el globito, lo deja en blanco"""
        self.pantalla.blit(self.globito,
                           posicion(XMAPAMAX, YGLOBITO))

    def correcto(self):
        """Muestra texto en el globito cuando la respuesta es correcta"""
        self.mostrarGlobito([random.choice(self.listaCorrecto)])
        self.esCorrecto = True
        self.puntos += 5 if self.nRespuestasMal >= 1 else 10
        self._deadline = pygame.time.get_ticks() + TIEMPORESPUESTA

    def mal(self):
        """Muestra texto en el globito cuando la respuesta es incorrecta"""
        self.mostrarGlobito([random.choice(self.listaMal)])
        self.esCorrecto = False
        self.nRespuestasMal += 1
        self._deadline = pygame.time.get_ticks() + TIEMPORESPUESTA

    def _categoria(self, nombre):
        """Resuelve los prefijos usados por los archivos de niveles."""
        if nombre.startswith("lineasDepto"):
            return "deptos"
        return next((clave for clave in CATEGORIAS
                     if nombre.startswith(clave)), None)

    def _elementos_categoria(self, categoria):
        """Devuelve los elementos y el estilo de una categoria."""
        lista, fuente, color, tipos, _, _ = CATEGORIAS[categoria]
        elementos = (elemento for elemento in getattr(self, lista)
                     if tipos is None or elemento.tipo in tipos)
        return elementos, getattr(self, fuente), color

    def esCorrecta(self, nivel, pos):
        """Comprueba nombre, categoria y posicion de la respuesta."""
        tipo = nivel.preguntaActual[1]
        respuesta = nivel.preguntaActual[2]
        for categoria, configuracion in CATEGORIAS.items():
            if configuracion[5] != tipo:
                continue
            elementos, fuente, color = self._elementos_categoria(categoria)
            for elemento in elementos:
                if elemento.nombre == respuesta and elemento.estaAca(pos):
                    elemento.mostrarNombre(self.pantalla, fuente, color)
                    return True
        return False

    def mostrarNombres(self, categorias):
        """Dibuja los nombres indicados sin actualizar la pantalla."""
        for nombre in categorias:
            categoria = self._categoria(nombre)
            if categoria is None:
                continue
            elementos, fuente, color = self._elementos_categoria(categoria)
            for elemento in elementos:
                elemento.mostrarNombre(self.pantalla, fuente, color)

    def presentLevel(self):
        for nombre in self.nivelActual.dibujoInicial:
            categoria = self._categoria(nombre)
            if categoria is None:
                continue
            imagen = CATEGORIAS[categoria][4]
            if imagen is not None:
                self.pantalla.blit(getattr(self, imagen), (shift_x, shift_y))
            else:
                elementos, _, _ = self._elementos_categoria(categoria)
                for elemento in elementos:
                    elemento.dibujar(self.pantalla)
        self.mostrarNombres(self.nivelActual.nombreInicial)

    def explorarNombres(self):
        """Juego principal en modo exploro."""
        self._explore_times = self._explore_times + 1
        self.nivelActual = self.listaExploraciones[self.indiceNivelActual]
        # presentar nivel
        self.presentLevel()
        # boton terminar
        self.end_rect = rectangulo(975, 25, 200, 50)
        self.pantalla.fill(COLOR_SHOW_ALL, self.end_rect)
        self.mostrarTexto(_("End"),
                          self.fuente40,
                          posicion(1075, 50),
                          COLOR_SKIP)
        # boton mostrar todo
        self.show_all_rect = rectangulo(975, 90, 200, 50)
        self.pantalla.fill(COLOR_SHOW_ALL, self.show_all_rect)
        self.mostrarTexto(_("Show all"),
                          self.fuente40,
                          posicion(1075, 115),
                          COLOR_SKIP)

    def _draw_progress(self):
        rect = rectangulo(XBARRA_A, YBARRA_A, ABARRA_A, ABARRA_P)
        unit = ABARRA_A / TOTALAVANCE
        fill = rect.copy()
        fill.width = escalar(unit * self.avanceNivel)
        self.pantalla.fill(COLORBARRA_A, fill)
        pygame.draw.rect(self.pantalla, COLORBARRA_C, rect, 3)
        for i in range(1, TOTALAVANCE):
            x = coordenada_x(XBARRA_A + unit * i)
            pygame.draw.line(self.pantalla, COLORBARRA_C,
                             (x, rect.top), (x, rect.bottom), 3)

    def jugarNivel(self):
        """Juego principal de preguntas y respuestas"""
        self._game_times = self._game_times + 1
        self.nivelActual = self.listaNiveles[self.indiceNivelActual]
        self.avanceNivel = 0
        self.nivelActual.prepararPreguntas()
        # presentar nivel
        self.presentLevel()
        self.end_rect = rectangulo(975, 26, 200, 48)
        self.pantalla.fill(COLOR_SHOW_ALL, self.end_rect)
        self.mostrarTexto(_("End"),
                          self.fuente40,
                          posicion(1075, 50),
                          COLOR_SKIP)
        # presentar pregunta inicial
        self.lineasPregunta = self.nivelActual.siguientePregunta(
            self.listaSufijos, self.listaPrefijos)
        self.mostrarGlobito(self.lineasPregunta)
        self.puntos = 0
        self._draw_score()
        self._draw_progress()
        self.nRespuestasMal = 0
        self.estadodespedida = 0
        self.respondiendo = False
        self._game_active = True


    def presentacion(self):
        """Prepara la introduccion; cada plazo muestra un solo cuadro."""
        # Duracion, imagenes (nombre, x, y), dialogo (indice, x, y), aviso.
        self._intro_frames = iter((
            (500, [('fondo1', 75, 75)], None, True),
            (2000, [('globo1', 180, 260)], (0, 384, 330), False),
            (2000, [('globo1', 180, 260)], (1, 384, 315), False),
            (2000, [('globo3', 618, 78)], None, False),
            (500, [('fondo2', 75, 75), ('jpp1', 487, 347)], None, True),
            (1000, [('globo1', 160, 240)], (2, 360, 310), False),
            (1500, [('globo2', 570, 260)], (3, 770, 330), False),
            (500, [('fondo2', 75, 75), ('jpp2', 487, 347)], None, True),
            (2000, [('globo1', 160, 240)], (4, 360, 310), False),
            (2000, [('globo1', 160, 240)], (5, 360, 310), False),
        ))
        self.pantalla.fill(COLOR_FONDO)
        self._advance_intro()

    def _advance_intro(self):
        frame = next(self._intro_frames, None)
        if frame is None:
            self._change_screen('maps')
            return
        duration, images, dialogue, notice = frame
        for name, x, y in images:
            self.pantalla.blit(getattr(self, name), posicion(x, y))
        if notice:
            self.mostrarTexto(_("Press any key to skip"), self.fuente32,
                              posicion(600, 800), COLOR_SKIP)
        if dialogue is not None:
            index, x, y = dialogue
            y_line = coordenada_y(y)
            for line in self.listaPresentacion[index].split("\n"):
                self.mostrarTexto(line.strip(), self.fuente40,
                                  (coordenada_x(x), y_line), COLORPREGUNTAS)
                y_line += self.fuente32.get_height() + escalar(10)
        self._deadline = pygame.time.get_ticks() + duration

    def _finish_game(self):
        """Contabiliza incluso una partida interrumpida, sin duplicarla."""
        if self._game_active:
            self._score += self.puntos
            self._average = self._score / self._game_times
            self._game_active = False

    def _change_screen(self, screen):
        """Cambia de estado y dibuja su pantalla sin esperar eventos."""
        self._finish_game()
        self._deadline = None
        self._screen = screen
        self._screen_revision += 1
        draw = {
            'intro': self.presentacion,
            'maps': self.pantallaDirectorios,
            'menu': self.pantallaInicial,
            'about': self.pantallaAcercaDe,
            'stats': self.pantallaStats,
        }
        if screen in draw:
            draw[screen]()
        else:
            self._draw_map_panel()
            if screen == 'play':
                self.jugarNivel()
            else:
                self.explorarNombres()

    def _draw_map_panel(self):
        self.pantalla.blit(self.fondo, (shift_x, shift_y))
        self.pantalla.fill(COLORPANEL,
                           rectangulo(XMAPAMAX, 0, DXPANEL, 900))
        if self._screen == 'play':
            self.pantalla.blit(self.jp1, posicion(XBICHO, YBICHO))
            self.estadobicho = ESTADONORMAL
            return
        if self.bandera:
            self.pantalla.blit(self.bandera, posicion(XMAPAMAX+47, 155))
        y = coordenada_y(YTEXTO) + self.fuente9.get_height()
        for label, value in self.lista_estadisticas:
            for text, x, color in ((label, XMAPAMAX+10, COLORESTADISTICAS1),
                                   (value, XMAPAMAX+135, COLORESTADISTICAS2)):
                self.pantalla.blit(self.fuente9.render(text, 1, color),
                                   (coordenada_x(x), y))
            y += self.fuente9.get_height() + escalar(5)

    def _back(self):
        if self._screen == 'maps':
            self._close_game(close_activity=True)
        else:
            self._change_screen('maps' if self._screen == 'menu' else 'menu')

    def _handle_event(self, event):
        """Despacha entrada al estado actual; QUIT se resuelve por lote."""
        if event.type not in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            return
        if self._screen == 'intro':
            self._play_click()
            self._change_screen('maps')
        elif self._screen in ('about', 'stats'):
            self._play_click()
            self._change_screen(self._return_screen)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._play_click()
                self._back()
        else:
            self._play_click()
            if self._screen in ('maps', 'menu'):
                self._handle_menu_click(event.pos)
            elif self.end_rect.collidepoint(event.pos):
                self._change_screen('menu')
            elif self._screen == 'explore':
                self._handle_explore_click(event.pos)
            elif rectangulo(0, 0, XMAPAMAX, 900).collidepoint(event.pos):
                self._answer(event.pos)

    def _handle_menu_click(self, pos):
        for rect, action in zip(self.footer_rects, ('about', 'stats', 'back')):
            if rect.collidepoint(pos):
                if action == 'back':
                    self._back()
                else:
                    self._return_screen = self._screen
                    self._change_screen(action)
                return
        if self._screen == 'maps':
            for rect, action, index in self.opciones:
                if not rect.collidepoint(pos):
                    continue
                if action in ('anterior', 'siguiente'):
                    self.paginaDir += -1 if action == 'anterior' else 1
                    self._change_screen('maps')
                else:
                    self.indiceDirectorioActual = index
                    self.directorio = self.listaDirectorios[index]
                    pygame.mouse.set_cursor((32, 32), (1, 1), *self.cursor_espera)
                    try:
                        self.cargarDirectorio()
                    finally:
                        pygame.mouse.set_cursor((32, 32), (1, 1), *self.cursor)
                    self._change_screen('menu')
                return
        else:
            for rects, screen in ((self.niveles_rect, 'play'),
                                  (self.exploraciones_rect, 'explore')):
                for index, rect in enumerate(rects):
                    if rect.collidepoint(pos):
                        self.indiceNivelActual = index
                        self._change_screen(screen)
                        return

    def _handle_explore_click(self, pos):
        if self.show_all_rect.collidepoint(pos):
            self.mostrarNombres(self.nivelActual.elementosActivos)
        elif rectangulo(0, 0, XMAPAMAX, 900).collidepoint(pos):
            for name in self.nivelActual.elementosActivos:
                category = self._categoria(name)
                if category is None:
                    continue
                elements, font, color = self._elementos_categoria(category)
                for element in elements:
                    if element.estaAca(pos):
                        element.mostrarNombre(self.pantalla, font, color)
                        self._explore_places += 1
                        break

    def _answer(self, pos):
        if self.respondiendo or self.avanceNivel >= TOTALAVANCE:
            return
        self.respondiendo = True
        self.borrarGlobito()
        if self.esCorrecta(self.nivelActual, pos):
            self.correcto()
        else:
            self.mal()
        self._draw_score()

    def _draw_score(self):
        self.pantalla.fill(COLORPANEL,
                           rectangulo(XBARRA_P, YBARRA_P-350, ABARRA_P, 390))
        self.pantalla.fill(COLORBARRA_P,
                           rectangulo(XBARRA_P, YBARRA_P-self.puntos*5,
                                      ABARRA_P, self.puntos*5))
        pygame.draw.rect(self.pantalla, COLORBARRA_C,
                         rectangulo(XBARRA_P, YBARRA_P-350, ABARRA_P, 350), 3)
        self.mostrarTexto(str(self.puntos), self.fuente32,
                          posicion(XBARRA_P+ABARRA_P/2, YBARRA_P+15), COLORBARRA_P)

    def _advance_question(self):
        self.respondiendo = False
        if not self.esCorrecto and self.nRespuestasMal == 1:
            self.mostrarGlobito(self.lineasPregunta + self.nivelActual.devolverAyuda())
            return
        self.avanceNivel += 1
        self._draw_progress()
        if self.avanceNivel == TOTALAVANCE:
            messages = (self.listaDespedidasB if self.puntos == TOTALAVANCE * 10
                        else self.listaDespedidasM)
            self.mostrarGlobito(random.choice(messages).split("\n"))
            self.respondiendo = True
            self._deadline = pygame.time.get_ticks() + TIEMPORESPUESTA * 2
        else:
            self.nRespuestasMal = 0
            self.lineasPregunta = self.nivelActual.siguientePregunta(
                self.listaSufijos, self.listaPrefijos)
            self.mostrarGlobito(self.lineasPregunta)

    def _advance_departure(self):
        self.estadobicho = ESTADODESPEGUE
        if self.estadodespedida == 3:
            self._change_screen('menu')
            return
        self.pantalla.fill(COLORPANEL, rectangulo(XMAPAMAX, 76, DXPANEL, 824))
        door = self.puerta2 if self.estadodespedida == 1 else self.puerta1
        self.pantalla.blit(door, posicion(XPUERTA, YPUERTA))
        if self.estadodespedida < 2:
            self.pantalla.blit(self.jp1, posicion(XBICHO, YBICHO))
        self.estadodespedida += 1
        self._deadline = pygame.time.get_ticks() + 1000

    def _animate_character(self):
        eyes = None
        if self.estadobicho == ESTADONORMAL:
            if random.randint(1, 15) == 1:
                self.estadobicho, eyes = ESTADOPESTANAS, self.ojos3
            elif random.randint(1, 20) == 1:
                self.estadobicho, eyes = ESTADOFRENTE, self.ojos2
        elif (self.estadobicho == ESTADOPESTANAS or
              (self.estadobicho == ESTADOFRENTE and random.randint(1, 10) == 1)):
            self.estadobicho, eyes = ESTADONORMAL, self.ojos1
        if eyes is not None:
            self.pantalla.blit(eyes, posicion(1020, 547))

    def _update(self, now):
        """Avanza animaciones y respuestas sin temporizadores en la cola."""
        if self._deadline is not None and now >= self._deadline:
            self._deadline = None
            if self._screen == 'intro':
                self._advance_intro()
            elif self._screen == 'play':
                if self.avanceNivel == TOTALAVANCE:
                    self._advance_departure()
                else:
                    self._advance_question()
        if now >= self._next_refresh:
            self._next_refresh = now + TIEMPOREFRESCO
            if self._screen == 'play':
                self._animate_character()

    def _process_events(self, events):
        # Un cambio de pantalla descarta entrada residual, pero nunca QUIT.
        if any(event.type == pygame.QUIT for event in events):
            self._close_game(close_activity=True)
            return
        revision = self._screen_revision
        for event in events:
            self._handle_event(event)
            if not self.running or self._screen_revision != revision:
                break

    def run(self):
        """Unico bucle de eventos para todas las pantallas y animaciones."""
        self.loadAll()
        self.loadCommons()
        self.load_stats()
        self._change_screen('intro')
        try:
            while self.running:
                self._process_events(self._get_events())
                if self.running:
                    self._update(pygame.time.get_ticks())
                    pygame.display.flip()
        finally:
            self._close_game()


def main():
    juego = Conozco()
    juego.run()

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    main()
