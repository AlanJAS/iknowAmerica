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
import pygame
import time
import importlib
import importlib.util
import importlib.machinery
import gettext
import configparser
from gettext import gettext as _
try:
    from sugar3.graphics.style import GRID_CELL_SIZE
except ImportError:
    GRID_CELL_SIZE = 0
gtk_present = True
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except (ImportError, ValueError):
    gtk_present = False

# constantes
RADIO = 10
RADIO2 = RADIO**2
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
EVENTORESPUESTA = pygame.USEREVENT+1
TIEMPORESPUESTA = 2300
EVENTODESPEGUE = EVENTORESPUESTA+1
EVENTOREFRESCO = EVENTODESPEGUE+1
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

# variables globales para adaptar la pantalla a distintas resoluciones
scale = 1
shift_x = 0
shift_y = 0
xo_resolution = True

clock = pygame.time.Clock()

def load_source(modname, filename):
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    # The module is always executed and not cached in sys.modules.
    # Uncomment the following line to cache the module.
    # sys.modules[module.__name__] = module
    loader.exec_module(module)
    return module


class Punto():
    """Clase para objetos geograficos que se pueden definir como un punto.

    La posicion esta dada por un par de coordenadas (x,y) medida en pixels
    dentro del mapa.
    """

    def __init__(self, nombre, tipo, simbolo, posicion, postexto):
        self.nombre = nombre
        self.tipo = int(tipo)
        self.posicion = (int(int(posicion[0])*scale+shift_x),
                         int(int(posicion[1])*scale+shift_y))
        self.postexto = (int(int(postexto[0])*scale)+self.posicion[0],
                         int(int(postexto[1])*scale)+self.posicion[1])
        self.simbolo = simbolo

    def estaAca(self, pos):
        """Devuelve un booleano indicando si esta en la coordenada pos,
        la precision viene dada por la constante global RADIO"""
        radio = RADIO * scale
        dx = pos[0] - self.posicion[0]
        dy = pos[1] - self.posicion[1]

        return dx * dx + dy * dy < radio * radio

    def dibujar(self, pantalla, flipAhora):
        """Dibuja un punto en su posicion"""
        rect = self.simbolo.get_rect(center=self.posicion)
        pantalla.blit(self.simbolo, rect)
        if flipAhora:
            pygame.display.flip()

    def mostrarNombre(self, pantalla, fuente, color, flipAhora):
        """Escribe el nombre del punto en su posicion"""
        text = fuente.render(self.nombre, 1, color)
        textrect = text.get_rect()
        textrect.center = (self.postexto[0], self.postexto[1])
        pantalla.blit(text, textrect)
        if flipAhora:
            pygame.display.flip()


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
        self.posicion = (int(int(posicion[0])*scale+shift_x),
                         int(int(posicion[1])*scale+shift_y))
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

    def mostrarNombre(self, pantalla, fuente, color, flipAhora):
        """Escribe el nombre de la zona en su posicion"""
        text = fuente.render(self.nombre, 1, color)
        textrot = pygame.transform.rotate(text, self.rotacion)
        textrect = textrot.get_rect()
        textrect.center = (self.posicion[0], self.posicion[1])
        pantalla.blit(textrot, textrect)
        if flipAhora:
            pygame.display.flip()


class Nivel():
    """Clase para definir los niveles del juego.

    Cada nivel tiene un dibujo inicial, los elementos pueden estar
    etiquetados con el nombre o no, y un conjunto de preguntas.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.dibujoInicial = list()
        self.nombreInicial = list()
        self.preguntas = list()
        self.indicePreguntaActual = 0
        self.elementosActivos = list()

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
            lugares = []
            if hasattr(f, 'CAPITALS'):
                lugares = lugares + f.CAPITALS
            if hasattr(f, 'CITIES'):
                lugares = lugares + f.CITIES
            if hasattr(f, 'HILLS'):
                lugares = lugares + f.HILLS
            
            for c in lugares:
                nombreLugar = c[0]
                posx = c[1]
                posy = c[2]
                tipo = c[3]
                incx = c[4]
                incy = c[5]
                if tipo == 0:
                    simbolo = self.simboloCapitalN
                elif tipo == 1:
                    simbolo = self.simboloCapitalD
                elif tipo == 2:
                    simbolo = self.simboloCiudad
                elif tipo == 5:
                    simbolo = self.simboloCerro
                else:
                    simbolo = self.simboloCiudad

                nuevoLugar = Punto(nombreLugar, tipo, simbolo,
                                   (posx, posy), (incx, incy))
                self.listaLugares.append(nuevoLugar)

            if hasattr(f, 'STATES'):
                self.deptos = self.cargarImagen("deptos.png")
                self.deptosLineas = self.cargarImagen("deptosLineas.png")
                
                for d in f.STATES:
                    nombreDepto = d[0]
                    claveColor = d[1]
                    posx = d[2]
                    posy = d[3]
                    rotacion = d[4]
                    nuevoDepto = Zona(self.deptos, nombreDepto,
                                      claveColor, 1, (posx, posy), rotacion)
                    self.listaDeptos.append(nuevoDepto)

            if hasattr(f, 'CUCHILLAS'):
                self.cuchillas = self.cargarImagen("cuchillas.png")
                self.cuchillasDetectar = self.cargarImagen(
                    "cuchillasDetectar.png")
                
                for c in f.CUCHILLAS:
                    nombreCuchilla = c[0]
                    claveColor = c[1]
                    posx = c[2]
                    posy = c[3]
                    rotacion = c[4]
                    nuevaCuchilla = Zona(self.cuchillasDetectar, nombreCuchilla,
                                         claveColor, 4, (posx, posy), rotacion)
                    self.listaCuchillas.append(nuevaCuchilla)

            if hasattr(f, 'RIVERS'):
                self.rios = self.cargarImagen("rios.png")
                self.riosDetectar = self.cargarImagen("riosDetectar.png")
                
                for r in f.RIVERS:
                    nombreRio = r[0]
                    claveColor = r[1]
                    posx = r[2]
                    posy = r[3]
                    rotacion = r[4]
                    nuevoRio = Zona(self.riosDetectar, nombreRio,
                                    claveColor, 3, (posx, posy), rotacion)
                    self.listaRios.append(nuevoRio)

            if hasattr(f, 'ROUTES'):
                self.rutas = self.cargarImagen("rutas.png")
                self.rutasDetectar = self.cargarImagen("rutasDetectar.png")
                
                for r in f.ROUTES:
                    nombreRuta = r[0]
                    claveColor = r[1]
                    posx = r[2]
                    posy = r[3]
                    rotacion = r[4]
                    nuevaRuta = Zona(self.rutasDetectar, nombreRuta,
                                     claveColor, 6, (posx, posy), rotacion)
                    self.listaRutas.append(nuevaRuta)
            
            if hasattr(f, 'STATS'):
                for e in f.STATS:
                    p1 = e[0]
                    p2 = e[1]
                    self.lista_estadisticas.append((p1, p2))

    def cargarListaDirectorios(self):
        """Carga la lista de directorios con los distintos mapas"""
        self.listaDirectorios = list()
        self.listaNombreDirectorios = list()
        listaTemp = os.listdir(CAMINORECURSOS)
        listaTemp.sort()
        for d in listaTemp:
            if not (d == 'comun'):
                r_path = os.path.join(CAMINORECURSOS, d, 'datos', d + '.py')
                a_path = os.path.abspath(r_path)
                f = None
                try:
                    f = load_source(d, a_path)
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
        """Carga los niveles de exploracion del archivo de configuracion."""
        path = os.path.join(self.camino_datos, ARCHIVOEXPLORACIONES + '.py')
        data = load_source(ARCHIVOEXPLORACIONES, path)
        self.listaExploraciones = []
        for name, drawings, labels, active in data.EXPLORATIONS:
            level = Nivel(name)
            level.dibujoInicial = [item.strip() for item in drawings]
            level.nombreInicial = [item.strip() for item in labels]
            level.elementosActivos = [item.strip() for item in active]
            self.listaExploraciones.append(level)

    def pantallaAcercaDe(self):
        """Pantalla con los datos del juego, creditos, etc"""
        self.pantallaTemp = pygame.Surface(
            (self.anchoPantalla, self.altoPantalla))
        self.pantallaTemp.blit(self.pantalla, (0, 0))
        self.pantalla.fill(COLOR_FONDO)
        self.pantalla.blit(self.terron,
                           (int(20*scale+shift_x),
                            int(20*scale+shift_y)))
        self.pantalla.blit(self.jp1,
                           (int(925*scale+shift_x),
                            int(468*scale+shift_y)))
        self.mostrarTexto(_("About %s") % self.activity_name,
                          self.fuente40,
                          (int(600*scale+shift_x),
                           int(100*scale+shift_y)),
                          COLOR_ACT_NAME)

        yLinea = int(200*scale+shift_y)
        for linea in self.listaCreditos:
            self.mostrarTexto(linea.strip(),
                              self.fuente32,
                              (int(600*scale+shift_x), yLinea),
                              COLOR_CREDITS)
            yLinea = yLinea + int(40*scale)

        self.mostrarTexto(_("Press any key to return"),
                          self.fuente32,
                          (int(600*scale+shift_x),
                           int(800*scale+shift_y)),
                          COLOR_SKIP)
        pygame.display.flip()
        while 1:
            clock.tick(20)
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound:
                        self.click.play()
                    self.pantalla.blit(self.pantallaTemp, (0, 0))
                    pygame.display.flip()
                    return
                elif event.type == pygame.QUIT:
                    if self.sound:
                        self.click.play()
                    self.save_stats()
                    return 1
                elif event.type == EVENTOREFRESCO:
                    pygame.display.flip()

    def pantallaStats(self):
        """Pantalla con los datos del juego, creditos, etc"""
        self.pantallaTemp = pygame.Surface(
            (self.anchoPantalla, self.altoPantalla))
        self.pantallaTemp.blit(self.pantalla, (0, 0))
        self.pantalla.fill(COLOR_FONDO)
        self.pantalla.blit(self.jp1,
                           (int(925*scale+shift_x),
                            int(468*scale+shift_y)))
        msg = _("Stats of %s") % self.activity_name
        self.mostrarTexto(msg,
                          self.fuente40,
                          (int(600*scale+shift_x),
                           int(100*scale+shift_y)),
                          COLOR_ACT_NAME)
        msg = _('Total score: %s') % self._score
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(300*scale+shift_y)),
                          COLOR_STAT_N)
        msg = _('Game average score: %s') % self._average
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(350*scale+shift_y)),
                          COLOR_STAT_N)
        msg = _('Times using Explore Mode: %s') % self._explore_times
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(400*scale+shift_y)),
                          COLOR_STAT_N)
        msg = _('Places Explored: %s') % self._explore_places
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(450*scale+shift_y)),
                          COLOR_STAT_N)
        msg = _('Times using Game Mode: %s') % self._game_times
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(500*scale+shift_y)),
                          COLOR_STAT_N)
        t = int((time.monotonic() - self._init_time) / 60)
        t = t + self._time
        msg = _('Total time: %s minutes') % t
        self.mostrarTexto(msg,
                          self.fuente32,
                          (int(400*scale+shift_x),
                           int(550*scale+shift_y)),
                          COLOR_STAT_N)

        self.mostrarTexto(_("Press any key to return"),
                          self.fuente32,
                          (int(600*scale+shift_x),
                           int(800*scale+shift_y)),
                          COLOR_SKIP)

        pygame.display.flip()
        while 1:
            clock.tick(20)
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound:
                        self.click.play()
                    self.pantalla.blit(self.pantallaTemp, (0, 0))
                    pygame.display.flip()
                    return
                elif event.type == pygame.QUIT:
                    if self.sound:
                        self.click.play()
                    self.save_stats()
                    return 1
                elif event.type == EVENTOREFRESCO:
                    pygame.display.flip()

    def _draw_footer(self, last_label):
        rectangles = []
        for x, label in zip((20, 420, 820),
                            (_("About this game"), _("Stats"), last_label)):
            rect = pygame.Rect(int(x * scale + shift_x),
                               int(801 * scale + shift_y),
                               int(370 * scale), int(48 * scale))
            self.pantalla.fill(COLOR_BUTTON_B, rect)
            self.mostrarTexto(label, self.fuente40, rect.center, COLOR_BUTTON_T)
            rectangles.append(rect)
        return rectangles
        
    def _draw_menu_option(self, texto, x, y, color):
        """Dibuja una opcion y devuelve su zona clicable"""
        rect = pygame.Rect(int(x*scale+shift_x), y-int(24*scale),
                           int(590*scale), int(48*scale))
        self.pantalla.fill(COLOR_OPTION_B, rect)
        self.mostrarTexto(texto, self.fuente40,
                          (int((x+290)*scale+shift_x), y), color)
        return rect

    def pantallaInicial(self):
        """Pantalla con el menu principal del juego"""
        self.pantalla.fill(COLOR_FONDO)
        self.mostrarTexto(self.activity_name,
                          self.fuente60,
                          (int(600*scale+shift_x),
                           int(80*scale+shift_y)),
                          COLOR_ACT_NAME)
        self.mostrarTexto(_("You have chosen the map ") +
                          self.listaNombreDirectorios
                          [self.indiceDirectorioActual],
                          self.fuente40,
                          (int(600*scale+shift_x), int(140*scale+shift_y)),
                          COLOR_OPTION_T)
        self.mostrarTexto(_("Play"),
                          self.fuente60,
                          (int(300*scale+shift_x), int(220*scale+shift_y)),
                          COLOR_OPTION_T)

        niveles_rect = []
        yLista = int(300*scale+shift_y)
        for n in self.listaNiveles:
            niveles_rect.append(self._draw_menu_option(
                n.nombre, 10, yLista, COLOR_OPTION_T))
            yLista += int(50*scale)
            
        self.mostrarTexto(_("Explore"),
                          self.fuente60,
                          (int(900*scale+shift_x), int(220*scale+shift_y)),
                          COLOR_NEXT)

        exploraciones_rect = []
        yLista = int(300*scale+shift_y)
        for n in self.listaExploraciones:
            exploraciones_rect.append(self._draw_menu_option(
                n.nombre, 610, yLista, COLOR_NEXT))
            yLista += int(50*scale)

        # buttons
        about_rect, stats_rect, exit_rect = self._draw_footer(_("Return"))
        pygame.display.flip()
        while 1:
            clock.tick(20)
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:  # escape: volver
                        if self.sound:
                            self.click.play()
                        self.elegir_directorio = True
                        return
                elif event.type == pygame.QUIT:
                    if self.sound:
                        self.click.play()
                    self.save_stats()
                    return 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound:
                        self.click.play()

                    pos = event.pos
                    if about_rect.collidepoint(pos):
                        if self.pantallaAcercaDe() == 1:
                            return 1
                    elif stats_rect.collidepoint(pos):
                        if self.pantallaStats() == 1:
                            return 1
                    elif exit_rect.collidepoint(pos):
                        self.elegir_directorio = True
                        return
                    else:
                        for indice, rect in enumerate(niveles_rect):
                            if rect.collidepoint(pos):
                                self.indiceNivelActual = indice
                                self.jugar = True
                                return
                        for indice, rect in enumerate(exploraciones_rect):
                            if rect.collidepoint(pos):
                                self.indiceNivelActual = indice
                                self.jugar = False
                                return

                elif event.type == EVENTOREFRESCO:
                    pygame.display.flip()

    def pantallaDirectorios(self):
        """Pantalla con el menu de directorios"""
        self.pantalla.fill(COLOR_FONDO)
        self.mostrarTexto(self.activity_name,
                          self.fuente60,
                          (int(600*scale+shift_x), int(80*scale+shift_y)),
                          COLOR_ACT_NAME)
        self.mostrarTexto(_("Choose the map to use"),
                          self.fuente40,
                          (int(600*scale+shift_x), int(140*scale+shift_y)),
                          COLOR_OPTION_T)
        nDirectorios = len(self.listaNombreDirectorios)
        paginaDirectorios = self.paginaDir
        while 1:
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()
            yLista = int(200*scale+shift_y)
            self.pantalla.fill(COLOR_FONDO,
                               (int(shift_x), yLista-int(24*scale),
                                int(1200*scale), int(600*scale)))
            
            opciones = []

            # Página anterior
            if paginaDirectorios > 0:
                rect = self._draw_menu_option(
                    "<<< " + _("Previous page"),
                    10, yLista, COLOR_NEXT
                )
                opciones.append((rect, "anterior", None))

            # Países de la página actual
            inicio = paginaDirectorios * 20
            fin = min(inicio + 20, nDirectorios)

            for local, indice in enumerate(range(inicio, fin)):
                columna = local // 10
                fila = local % 10

                x = 10 + columna * 600
                y = int((250 + fila * 50) * scale + shift_y)

                rect = self._draw_menu_option(
                    self.listaNombreDirectorios[indice],
                    x, y, COLOR_OPTION_T
                )

                opciones.append((rect, "mapa", indice))

            # Página siguiente
            if fin < nDirectorios:
                rect = self._draw_menu_option(
                    _("Next page") + " >>>",
                    610,
                    int(750 * scale + shift_y),
                    COLOR_NEXT
                )
                opciones.append((rect, "siguiente", None))

            # buttons
            about_rect, stats_rect, exit_rect = self._draw_footer(_("Exit"))
            pygame.display.flip()
            cambiarPagina = False
            while not cambiarPagina:
                clock.tick(20)
                if gtk_present:
                    while Gtk.events_pending():
                        Gtk.main_iteration()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == 27:  # escape: salir
                            if self.sound:
                                self.click.play()
                            self.save_stats()
                            if self.parent is not None:
                                self.parent.close(skip_save=True)
                            return 1
                    elif event.type == pygame.QUIT:
                        if self.sound:
                            self.click.play()
                        self.save_stats()
                        return 1
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.sound:
                            self.click.play()
                        pos = event.pos
                        # zona de opciones
                        if about_rect.collidepoint(pos):
                            if self.pantallaAcercaDe() == 1:
                                return 1
                        elif stats_rect.collidepoint(pos):
                            if self.pantallaStats() == 1:
                                return 1
                        elif exit_rect.collidepoint(pos):
                            self.save_stats()
                            if self.parent is not None:
                                self.parent.close(skip_save=True)
                            return 1
                        else:
                            for rect, accion, indice in opciones:
                                if not rect.collidepoint(pos):
                                    continue
                                if accion == "anterior":
                                    paginaDirectorios -= 1
                                    cambiarPagina = True
                                elif accion == "siguiente":
                                    paginaDirectorios += 1
                                    cambiarPagina = True
                                else:
                                    self.indiceDirectorioActual = indice
                                    self.paginaDir = paginaDirectorios
                                    return
                                break

                    elif event.type == EVENTOREFRESCO:
                        pygame.display.flip()

    def cargarImagen(self, nombre):
        """Carga una imagen y la escala de acuerdo a la resolucion"""
        archivo = os.path.join(self.camino_imagenes, nombre)
        if not os.path.exists(archivo):
            return None
        imagen = pygame.image.load(archivo)
        if not xo_resolution:
            imagen = pygame.transform.scale(imagen,
                         (int(imagen.get_width() * scale),
                         int(imagen.get_height() * scale)))
        return imagen

    def __init__(self, parent=None):
        self.parent = parent
        self.running = True
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
        l = []
        for i in range(7):
            l.append(0)
        try:
            path = self._get_stats_path()
            f = open(path, 'r')
            for i in range(7):
                val = f.readline()
                val = val.strip('\n')
                if not(val == ''):
                    l[i] = int(float(val))
            f.close()
        except FileNotFoundError:
            return  # First run.
        except (OSError, ValueError) as err:
            print('Cannot load stats', err)
            return
        if self._validate_stats(l):
            self._score = l[0]
            self._average = l[1]
            self._explore_times = l[2]
            self._explore_places = l[3]
            self._game_times = l[4]
            self._time = l[5]

    def _validate_stats(self, l):
        return (self._calc_sum(l) == l[6])

    def _calc_sum(self, l):
        s = 0
        for i in range(6):
            s = s + l[i]
        return s % 7

    def _get_stats_path(self):
        if self.parent is not None:
            folder = os.path.join(self.parent.get_activity_root(), 'data')
        else:
            base = os.environ.get('XDG_DATA_HOME', '')
            if not os.path.isabs(base):
                base = os.path.expanduser('~/.local/share')

            folder = os.path.join(base, 'iknowamerica')
        try:
            os.makedirs(folder, exist_ok=True)
        except:
            return None
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
            # use aux list
            l = []
            for i in range(7):
                l.append(0)
            l[0] = self._score
            l[1] = self._average
            l[2] = self._explore_times
            l[3] = self._explore_places
            l[4] = self._game_times
            l[5] = self._time
            l[6] = self._calc_sum(l)
            # save
            f = open(path, 'w')
            for i in range(7):
                f.write(str(l[i]) + '\n')
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
        pygame.display.flip()
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
        # fondo presentacion
        self.fondo1 = self.cargarImagen("fondo1.png")
        self.fondo2 = self.cargarImagen("fondo2.png")
        # JP presentacion
        self.jpp1 = self.cargarImagen("jpp1.png")
        self.jpp2 = self.cargarImagen("jpp2.png")
        # globo
        self.globo1 = self.cargarImagen("globo1.png")
        self.globo2 = pygame.transform.flip(self.globo1, True, False)
        self.globo3 = self.cargarImagen("globo3.png")
        # JP para el juego
        self.jp1 = self.cargarImagen("jp1.png")
        # Ojos JP
        self.ojos1 = self.cargarImagen("ojos1.png")
        self.ojos2 = self.cargarImagen("ojos2.png")
        self.ojos3 = self.cargarImagen("ojos3.png")
        # Puerta fin
        self.puerta1 = self.cargarImagen("puerta01.png")
        self.puerta2 = self.cargarImagen("puerta02.png")
        # Otros
        self.globito = self.cargarImagen("globito.png")
        self.terron = self.cargarImagen("terron.png")
        self.simboloCapitalD = self.cargarImagen("capitalD.png")
        self.simboloCapitalN = self.cargarImagen("capitalN.png")
        self.simboloCiudad = self.cargarImagen("ciudad.png")
        self.simboloCerro = self.cargarImagen("cerro.png")
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
        self.fuente60 = pygame.font.Font(os.path.join(CAMINORECURSOS,
                                                      CAMINOCOMUN,
                                                      CAMINOFUENTES,
                                                      "Share-Regular.ttf"),
                                         int(60*scale))
        self.fuente40 = pygame.font.Font(os.path.join(CAMINORECURSOS,
                                                      CAMINOCOMUN,
                                                      CAMINOFUENTES,
                                                      "Share-Regular.ttf"),
                                         int(34*scale))
        self.fuente9 = pygame.font.Font(os.path.join(CAMINORECURSOS,
                                                     CAMINOCOMUN,
                                                     CAMINOFUENTES,
                                                     "Share-Regular.ttf"),
                                        int(20*scale))
        self.fuente32 = pygame.font.Font(None, int(30*scale))
        self.fuente24 = pygame.font.Font(None, int(24*scale))
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
                           (int(XMAPAMAX*scale+shift_x),
                            int(YGLOBITO*scale+shift_y)))
        yLinea = int(YGLOBITO*scale) + shift_y + \
            self.fuente32.get_height()*3
        for l in lineas:
            text = self.fuente32.render(l, 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(XCENTROPANEL*scale+shift_x), yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea + self.fuente32.get_height() + int(10*scale)
        pygame.display.flip()

    def borrarGlobito(self):
        """ Borra el globito, lo deja en blanco"""
        self.pantalla.blit(self.globito,
                           (int(XMAPAMAX*scale+shift_x),
                            int(YGLOBITO*scale+shift_y)))

    def correcto(self):
        """Muestra texto en el globito cuando la respuesta es correcta"""
        self.mostrarGlobito([random.choice(self.listaCorrecto)])
        self.esCorrecto = True
        if self.nRespuestasMal >= 1:
            self.puntos = self.puntos + 5
        else:
            self.puntos = self.puntos + 10
        pygame.time.set_timer(EVENTORESPUESTA, TIEMPORESPUESTA)

    def mal(self):
        """Muestra texto en el globito cuando la respuesta es incorrecta"""
        self.mostrarGlobito([random.choice(self.listaMal)])
        self.esCorrecto = False
        self.nRespuestasMal += 1
        pygame.time.set_timer(EVENTORESPUESTA, TIEMPORESPUESTA)

    def esCorrecta(self, nivel, pos):
        """Devuelve True si las coordenadas cliqueadas corresponden a la
        respuesta correcta
        """
        respCorrecta = nivel.preguntaActual[2]
        choices = {
            1: ('listaDeptos', self.fuente32, COLORNOMBREDEPTO),
            2: ('listaLugares', self.fuente24, COLORNOMBRECAPITAL),
            3: ('listaRios', self.fuente24, COLORNOMBRERIO),
            4: ('listaCuchillas', self.fuente24, COLORNOMBREELEVACION),
            5: ('listaLugares', self.fuente24, COLORNOMBREELEVACION),
            6: ('listaRutas', self.fuente24, COLORNOMBRERUTA),
        }
        choice = choices.get(nivel.preguntaActual[1])
        if choice is None:
            return False
        attribute, font, color = choice
        for place in getattr(self, attribute, []):
            if place.nombre == respCorrecta:
                if place.estaAca(pos):
                    place.mostrarNombre(self.pantalla, font, color, True)
                    return True
                else:
                    return False
        return False

    def presentLevel(self):
        for i in self.nivelActual.dibujoInicial:
            if i.startswith("lineasDepto"):
                self.pantalla.blit(self.deptosLineas, (shift_x, shift_y))
            elif i.startswith("rios"):
                self.pantalla.blit(self.rios, (shift_x, shift_y))
            elif i.startswith("rutas"):
                self.pantalla.blit(self.rutas, (shift_x, shift_y))
            elif i.startswith("cuchillas"):
                self.pantalla.blit(self.cuchillas, (shift_x, shift_y))
            elif i.startswith("capitales"):
                for l in self.listaLugares:
                    if ((l.tipo == 0) or (l.tipo == 1)):
                        l.dibujar(self.pantalla, False)
            elif i.startswith("ciudades"):
                for l in self.listaLugares:
                    if l.tipo == 2:
                        l.dibujar(self.pantalla, False)
            elif i.startswith("cerros"):
                for l in self.listaLugares:
                    if l.tipo == 5:
                        l.dibujar(self.pantalla, False)
        for i in self.nivelActual.nombreInicial:
            if i.startswith("deptos"):
                for d in self.listaDeptos:
                    d.mostrarNombre(self.pantalla, self.fuente32,
                                    COLORNOMBREDEPTO, False)
            elif i.startswith("rios"):
                for d in self.listaRios:
                    d.mostrarNombre(self.pantalla, self.fuente24,
                                    COLORNOMBRERIO, False)
            elif i.startswith("rutas"):
                for d in self.listaRutas:
                    d.mostrarNombre(self.pantalla, self.fuente24,
                                    COLORNOMBRERUTA, False)
            elif i.startswith("cuchillas"):
                for d in self.listaCuchillas:
                    d.mostrarNombre(self.pantalla, self.fuente24,
                                    COLORNOMBREELEVACION, False)
            elif i.startswith("capitales"):
                for l in self.listaLugares:
                    if ((l.tipo == 0) or (l.tipo == 1)):
                        l.mostrarNombre(self.pantalla, self.fuente24,
                                        COLORNOMBRECAPITAL, False)
            elif i.startswith("ciudades"):
                for l in self.listaLugares:
                    if l.tipo == 2:
                        l.mostrarNombre(self.pantalla, self.fuente24,
                                        COLORNOMBRECAPITAL, False)
            elif i.startswith("cerros"):
                for l in self.listaLugares:
                    if l.tipo == 5:
                        l.mostrarNombre(self.pantalla, self.fuente24,
                                        COLORNOMBREELEVACION, False)

    def explorarNombres(self):
        """Juego principal en modo exploro."""
        self._explore_times = self._explore_times + 1
        self.nivelActual = self.listaExploraciones[self.indiceNivelActual]
        # presentar nivel
        self.presentLevel()
        # boton terminar
        end_rect = pygame.Rect(int(975*scale+shift_x),
                               int(25*scale+shift_y),
                               int(200*scale), int(50*scale))
        self.pantalla.fill(COLOR_SHOW_ALL, end_rect)
        self.mostrarTexto(_("End"),
                          self.fuente40,
                          (int(1075*scale+shift_x),
                           int(50*scale+shift_y)),
                          COLOR_SKIP)
        pygame.display.flip()
        # boton mostrar todo
        show_all_rect = pygame.Rect(int(975*scale+shift_x),
                                    int(90*scale+shift_y),
                                    int(200*scale), int(50*scale))
        self.pantalla.fill(COLOR_SHOW_ALL, show_all_rect)
        self.mostrarTexto(_("Show all"),
                          self.fuente40,
                          (int(1075*scale+shift_x),
                           int(115*scale+shift_y)),
                          COLOR_SKIP)
        pygame.display.flip()
        # lazo principal de espera por acciones del usuario
        while 1:
            clock.tick(20)
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:  # escape: salir
                        if self.sound:
                            self.click.play()
                        return
                elif event.type == pygame.QUIT:
                    if self.sound:
                        self.click.play()
                    self.save_stats()
                    return 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound:
                        self.click.play()
                    if event.pos[0] < XMAPAMAX*scale+shift_x:  # zona de mapa
                        for i in self.nivelActual.elementosActivos:
                            if i.startswith("capitales"):
                                for l in self.listaLugares:
                                    if ((l.tipo == 0) or (l.tipo == 1)) and l.estaAca(event.pos):
                                        l.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBRECAPITAL,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("ciudades"):
                                for l in self.listaLugares:
                                    if l.tipo == 2 and l.estaAca(event.pos):
                                        l.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBRECAPITAL,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("rios"):
                                for d in self.listaRios:
                                    if d.estaAca(event.pos):
                                        d.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBRERIO,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("rutas"):
                                for d in self.listaRutas:
                                    if d.estaAca(event.pos):
                                        d.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBRERUTA,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("cuchillas"):
                                for d in self.listaCuchillas:
                                    if d.estaAca(event.pos):
                                        d.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBREELEVACION,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("cerros"):
                                for l in self.listaLugares:
                                    if l.tipo == 5 and l.estaAca(event.pos):
                                        l.mostrarNombre(self.pantalla,
                                                        self.fuente24,
                                                        COLORNOMBREELEVACION,
                                                        True)
                                        self._explore_places += 1
                                        break
                            elif i.startswith("deptos"):
                                for d in self.listaDeptos:
                                    if d.estaAca(event.pos):
                                        d.mostrarNombre(self.pantalla,
                                                        self.fuente32,
                                                        COLORNOMBREDEPTO,
                                                        True)
                                        self._explore_places += 1
                                        break
                    elif end_rect.collidepoint(event.pos):
                        return
                    elif show_all_rect.collidepoint(event.pos):
                        for i in self.nivelActual.elementosActivos:
                            if i.startswith("deptos"):
                                for d in self.listaDeptos:
                                    d.mostrarNombre(self.pantalla, self.fuente32,
                                                    COLORNOMBREDEPTO, False)
                            elif i.startswith("rios"):
                                for d in self.listaRios:
                                    d.mostrarNombre(self.pantalla, self.fuente24,
                                                    COLORNOMBRERIO, False)
                            elif i.startswith("rutas"):
                                for d in self.listaRutas:
                                    d.mostrarNombre(self.pantalla, self.fuente24,
                                                    COLORNOMBRERUTA, False)
                            elif i.startswith("cuchillas"):
                                for d in self.listaCuchillas:
                                    d.mostrarNombre(self.pantalla, self.fuente24,
                                                    COLORNOMBREELEVACION, False)
                            elif i.startswith("capitales"):
                                for l in self.listaLugares:
                                    if ((l.tipo == 0) or (l.tipo == 1)):
                                        l.mostrarNombre(self.pantalla, self.fuente24,
                                                        COLORNOMBRECAPITAL, False)
                            elif i.startswith("ciudades"):
                                for l in self.listaLugares:
                                    if l.tipo == 2:
                                        l.mostrarNombre(self.pantalla, self.fuente24,
                                                        COLORNOMBRECAPITAL, False)
                            elif i.startswith("cerros"):
                                for l in self.listaLugares:
                                    if l.tipo == 5:
                                        l.mostrarNombre(self.pantalla, self.fuente24,
                                                        COLORNOMBREELEVACION, False)
                        pygame.display.flip()
                elif event.type == EVENTOREFRESCO:
                    pygame.display.flip()

    def _draw_progress(self):
        rect = pygame.Rect(int(XBARRA_A * scale + shift_x),
                           int(YBARRA_A * scale + shift_y),
                           int(ABARRA_A * scale), int(ABARRA_P * scale))
        unit = ABARRA_A / TOTALAVANCE
        fill = rect.copy()
        fill.width = int(unit * self.avanceNivel * scale)
        self.pantalla.fill(COLORBARRA_A, fill)
        pygame.draw.rect(self.pantalla, COLORBARRA_C, rect, 3)
        for i in range(1, TOTALAVANCE):
            x = int((XBARRA_A + unit * i) * scale + shift_x)
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
        end_rect = pygame.Rect(int(975*scale+shift_x),
                               int(26*scale+shift_y),
                               int(200*scale), int(48*scale))
        self.pantalla.fill(COLOR_SHOW_ALL, end_rect)
        self.mostrarTexto(_("End"),
                          self.fuente40,
                          (int(1075*scale+shift_x),
                           int(50*scale+shift_y)),
                          COLOR_SKIP)
        pygame.display.flip()
        # presentar pregunta inicial
        self.lineasPregunta = self.nivelActual.siguientePregunta(
            self.listaSufijos, self.listaPrefijos)
        self.mostrarGlobito(self.lineasPregunta)
        # barra puntaje
        pygame.draw.rect(self.pantalla, COLORBARRA_C,
                         (int(XBARRA_P*scale+shift_x),
                          int((YBARRA_P-350)*scale+shift_y),
                          int(ABARRA_P*scale),
                          int(350*scale)), 3)
        self.mostrarTexto('0', self.fuente32,
                          (int((XBARRA_P+ABARRA_P/2)*scale+shift_x),
                           int(YBARRA_P+10)*scale+shift_y), COLORBARRA_P)
        # barra avance
        self._draw_progress()
        
        self.nBien = 0
        self.nMal = 0
        self.puntos = 0
        self.nRespuestasMal = 0
        self.otorgado = False
        self.estadodespedida = 0
        self.primera = False
        self.respondiendo = False
        self.avanceNivel = 0
        pygame.time.set_timer(EVENTORESPUESTA, 0)
        # leer eventos y ver si la respuesta es correcta
        while 1:
            clock.tick(20)
            if gtk_present:
                while Gtk.events_pending():
                    Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:  # escape: salir
                        if self.sound:
                            self.click.play()
                        pygame.time.set_timer(EVENTORESPUESTA, 0)
                        pygame.time.set_timer(EVENTODESPEGUE, 0)
                        return
                elif event.type == pygame.QUIT:
                    if self.sound:
                        self.click.play()
                    self.save_stats()
                    return 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound:
                        self.click.play()
                    if end_rect.collidepoint(event.pos):
                        pygame.time.set_timer(EVENTORESPUESTA, 0)
                        pygame.time.set_timer(EVENTODESPEGUE, 0)
                        return
                    if event.pos[0] < XMAPAMAX*scale+shift_x:  # zona mapa
                        if self.avanceNivel < TOTALAVANCE:
                            if not(self.respondiendo):
                                self.respondiendo = True
                                if self.esCorrecta(self.nivelActual, event.pos):
                                    if not(self.otorgado):
                                        self.borrarGlobito()
                                        self.correcto()
                                        self.otorgado = True
                                else:
                                    self.borrarGlobito()
                                    self.mal()
                                if self.puntos < 0:
                                    self.mostrarTexto('0', self.fuente32,
                                                      (int((XBARRA_P+ABARRA_P/2)*scale+shift_x),
                                                       int(YBARRA_P+15)*scale+shift_y),
                                                      COLORBARRA_P)
                                else:
                                    self.pantalla.fill(COLORPANEL, (
                                        int(XBARRA_P*scale+shift_x),
                                        int((YBARRA_P-350)*scale+shift_y),
                                        int(ABARRA_P*scale),
                                        int(390*scale)
                                    )
                                    )
                                    self.pantalla.fill(COLORBARRA_P, (
                                        int(XBARRA_P*scale+shift_x),
                                        int((YBARRA_P-self.puntos*5)
                                            * scale+shift_y),
                                        int(ABARRA_P*scale),
                                        int(self.puntos*5*scale)
                                    )
                                    )
                                    pygame.draw.rect(self.pantalla, COLORBARRA_C,
                                                     (int(XBARRA_P*scale+shift_x),
                                                      int((YBARRA_P-350)
                                                          * scale+shift_y),
                                                         int(ABARRA_P*scale),
                                                         int(350*scale)), 3)
                                    self.mostrarTexto(str(self.puntos), self.fuente32,
                                                      (int((XBARRA_P+ABARRA_P/2)*scale+shift_x),
                                                       int(YBARRA_P+15)*scale+shift_y),
                                                      COLORBARRA_P)

                elif event.type == EVENTORESPUESTA:
                    pygame.time.set_timer(EVENTORESPUESTA, 0)
                    self.respondiendo = False
                    if not(self.esCorrecto):
                        if self.nRespuestasMal == 1:  # ayuda
                            linea = self.lineasPregunta
                            linea2 = self.nivelActual.devolverAyuda()
                            linea3 = linea + linea2
                            self.mostrarGlobito(linea3)
                            pygame.time.set_timer(
                                EVENTORESPUESTA, TIEMPORESPUESTA)
                        elif self.nRespuestasMal > 1:
                            self.lineasPregunta = \
                                self.nivelActual.siguientePregunta(
                                    self.listaSufijos, self.listaPrefijos)
                            self.mostrarGlobito(self.lineasPregunta)
                            self.nRespuestasMal = 0
                            # avanzo
                            self.avanceNivel = self.avanceNivel + 1
                            # barra avance
                            self._draw_progress()
                            # fin barra avance
                        else:  # volver a preguntar
                            self.mostrarGlobito(self.lineasPregunta)
                    else:
                        self.avanceNivel = self.avanceNivel + 1
                        # barra avance
                        self._draw_progress()
                        # fin barra avance
                        if not(self.avanceNivel == TOTALAVANCE):
                            self.lineasPregunta = \
                                self.nivelActual.siguientePregunta(
                                    self.listaSufijos, self.listaPrefijos)
                            self.mostrarGlobito(self.lineasPregunta)
                            self.nRespuestasMal = 0
                            self.otorgado = False
                    if self.avanceNivel == TOTALAVANCE:  # inicia despedida
                        if self.puntos == 70:
                            self.lineasPregunta = random.choice(self.listaDespedidasB)\
                                .split("\n")
                        else:
                            self.lineasPregunta = random.choice(self.listaDespedidasM)\
                                .split("\n")
                        self.mostrarGlobito(self.lineasPregunta)
                        pygame.time.set_timer(EVENTODESPEGUE,
                                              TIEMPORESPUESTA*2)

                elif event.type == EVENTODESPEGUE:
                    self.estadobicho = ESTADODESPEGUE
                    self.pantalla.fill(COLORPANEL,
                                       (int(XMAPAMAX*scale+shift_x), int(76*scale+shift_y),
                                        int(DXPANEL*scale),
                                        int(824*scale)))
                    if self.estadodespedida == 0:
                        self.pantalla.blit(self.puerta1,
                                           (int(XPUERTA*scale+shift_x), YPUERTA*scale+shift_y))
                        self.pantalla.blit(self.jp1,
                                           (int(XBICHO*scale+shift_x),
                                            int(YBICHO*scale+shift_y)))
                    elif self.estadodespedida == 1:
                        self.pantalla.blit(self.puerta2,
                                           (int(XPUERTA*scale+shift_x), YPUERTA*scale+shift_y))
                        self.pantalla.blit(self.jp1,
                                           (int(XBICHO*scale+shift_x),
                                            int(YBICHO*scale+shift_y)))
                    elif self.estadodespedida == 2:
                        self.pantalla.blit(self.puerta1,
                                           (int(XPUERTA*scale+shift_x), YPUERTA*scale+shift_y))
                    elif self.estadodespedida == 3:
                        pygame.time.set_timer(EVENTODESPEGUE, 0)
                        return
                    pygame.display.flip()
                    self.estadodespedida = self.estadodespedida + 1
                    pygame.time.set_timer(EVENTODESPEGUE, 1000)

                elif event.type == EVENTOREFRESCO:
                    if self.estadobicho == ESTADONORMAL:
                        if random.randint(1, 15) == 1:
                            self.estadobicho = ESTADOPESTANAS
                            self.pantalla.blit(self.ojos3,
                                               (int(1020*scale+shift_x),
                                                int(547*scale+shift_y)))
                        elif random.randint(1, 20) == 1:
                            self.estadobicho = ESTADOFRENTE
                            self.pantalla.blit(self.ojos2,
                                               (int(1020*scale+shift_x),
                                                int(547*scale+shift_y)))
                    elif self.estadobicho == ESTADOPESTANAS:
                        self.estadobicho = ESTADONORMAL
                        self.pantalla.blit(self.ojos1,
                                           (int(1020*scale+shift_x),
                                            int(547*scale+shift_y)))
                    elif self.estadobicho == ESTADOFRENTE:
                        if random.randint(1, 10) == 1:
                            self.estadobicho = ESTADONORMAL
                            self.pantalla.blit(self.ojos1,
                                               (int(1020*scale+shift_x),
                                                int(547*scale+shift_y)))
                    elif self.estadobicho == ESTADODESPEGUE:
                        pass
                    pygame.display.flip()

    def _wait_presentation(self, milliseconds):
        """Return True when the presentation is skipped or the window closes."""
        pygame.time.set_timer(EVENTORESPUESTA, milliseconds)
        try:
            while True:
                clock.tick(20)
                if gtk_present:
                    while Gtk.events_pending():
                        Gtk.main_iteration()
                events = pygame.event.get()
                if any(event.type == pygame.QUIT for event in events):
                    return "quit"
                for event in events:
                    if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                        if self.sound:
                            self.click.play()
                        return "skip"
                    if event.type == EVENTORESPUESTA:
                        return "continue"
                    if event.type == EVENTOREFRESCO:
                        pygame.display.flip()
        finally:
            pygame.time.set_timer(EVENTORESPUESTA, 0)
            pygame.event.clear(EVENTORESPUESTA)

    def presentacion(self):

        #***************************** cuadro 1 ******************************
        self.pantalla.fill(COLOR_FONDO)
        self.pantalla.blit(self.fondo1,
                        (int(75*scale+shift_x),int(75*scale+shift_y)))
        self.mostrarTexto(_("Press any key to skip"),
                        self.fuente32,
                        (int(600*scale+shift_x),int(800*scale+shift_y)),
                        COLOR_SKIP)
        pygame.display.flip()
        # esperar o no esperar, esa es la cuestion
        resultado = self._wait_presentation(500)
        if resultado != "continue":
            return resultado

        # comienzo animacion
        self.pantalla.blit(self.globo1,
                        (int(180*scale+shift_x),int(260*scale+shift_y)))
        yLinea = int(330*scale+shift_y)
        # hola amigos
        lineas = self.listaPresentacion[0].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(384*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea+self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()

        #time.sleep(2)
        terminar = False
        resultado = self._wait_presentation(2000)
        if resultado != "continue":
            return resultado

        self.pantalla.blit(self.globo1,
                        (int(180*scale+shift_x),int(260*scale+shift_y)))
        yLinea = int(315*scale+shift_y)
        # mañana tengo...
        lineas = self.listaPresentacion[1].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(384*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea+self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()
        resultado = self._wait_presentation(2000)
        if resultado != "continue":
            return resultado

        #***************************** cuadro 3 ******************************
        self.pantalla.blit(self.globo3,
                        (int(618*scale+shift_x),int(78*scale+shift_y)))
        pygame.display.flip()
        resultado = self._wait_presentation(2000)
        if resultado != "continue":
            return resultado

        #***************************** cuadro 4 ******************************
        # **************************** fondo 2 *******************************
        self.pantalla.blit(self.fondo2,
                        (int(75*scale+shift_x),int(75*scale+shift_y)))
        self.pantalla.blit(self.jpp1,
                        (int(487*scale+shift_x),int(347*scale+shift_y)))
        self.mostrarTexto(_("Press any key to skip"),
                        self.fuente32,
                        (int(600*scale+shift_x),int(800*scale+shift_y)),
                        COLOR_SKIP)
        pygame.display.flip()
        # espero
        resultado = self._wait_presentation(500)
        if resultado != "continue":
            return resultado

        self.pantalla.blit(self.globo1,
                        (int(160*scale+shift_x),int(240*scale+shift_y)))
        yLinea = int(310*scale+shift_y)
        # y no se nada
        lineas = self.listaPresentacion[2].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(360*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea+self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()
        resultado = self._wait_presentation(1000)
        if resultado != "continue":
            return resultado

        #***************************** cuadro 5 ******************************
        self.pantalla.blit(self.globo2,
                        (int(570*scale+shift_x),int(260*scale+shift_y)))
        yLinea = int(330*scale+shift_y)
        # que hago
        lineas = self.listaPresentacion[3].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(770*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea + self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()
        resultado = self._wait_presentation(1500)
        if resultado != "continue":
            return resultado

        #***************************** cuadro 6 ******************************
        self.pantalla.blit(self.fondo2,
                        (int(75*scale+shift_x),int(75*scale+shift_y)))
        self.pantalla.blit(self.jpp2,
                        (int(487*scale+shift_x),int(347*scale+shift_y)))
        self.mostrarTexto(_("Press any key to skip"),
                        self.fuente32,
                        (int(600*scale+shift_x),int(800*scale+shift_y)),
                        COLOR_SKIP)
        pygame.display.flip()
        # espero
        resultado = self._wait_presentation(500)
        if resultado != "continue":
            return resultado

        self.pantalla.blit(self.globo1,
                        (int(160*scale+shift_x),int(240*scale+shift_y)))
        yLinea = int(310*scale+shift_y)
        # te puedo pedir
        lineas = self.listaPresentacion[4].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(360*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea + self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()

        resultado = self._wait_presentation(2000)
        if resultado != "continue":
            return resultado

        self.pantalla.blit(self.globo1,
                        (int(160*scale+shift_x),int(240*scale+shift_y)))
        yLinea = int(310*scale+shift_y)
        # me ayudas
        lineas = self.listaPresentacion[5].split("\n")
        for l in lineas:
            text = self.fuente40.render(l.strip(), 1, COLORPREGUNTAS)
            textrect = text.get_rect()
            textrect.center = (int(360*scale+shift_x),yLinea)
            self.pantalla.blit(text, textrect)
            yLinea = yLinea + self.fuente32.get_height()+int(10*scale)
        pygame.display.flip()
        
        resultado = self._wait_presentation(2000)
        # retorno siempre algo
        return resultado

    def run(self):
        """Este es el loop principal del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(
                    (event.size[0], event.size[1] - GRID_CELL_SIZE),
                    pygame.RESIZABLE)
                break

        pygame.time.set_timer(EVENTOREFRESCO,TIEMPOREFRESCO)

        self.loadAll()

        self.loadCommons()
        
        self.load_stats()

        resultado = self.presentacion()

        if resultado == "quit":
            self.running = False
            self.save_stats()

            if self.parent is not None:
                self.parent.close(skip_save=True)

            return

        # Si terminó normalmente o se salto, continuar con el juego.
        self.paginaDir = 0
        self.running = True

        while self.running:
            if self.pantallaDirectorios() == 1:
                return
            # seleccion de mapa
            pygame.mouse.set_cursor((32, 32), (1, 1), *self.cursor_espera)
            self.directorio = self.listaDirectorios[self.indiceDirectorioActual]
            self.cargarDirectorio()
            pygame.mouse.set_cursor((32, 32), (1, 1), *self.cursor)
            while self.running:
                # pantalla inicial de juego
                self.elegir_directorio = False
                if self.pantallaInicial() == 1:
                    return
                if self.elegir_directorio:  # volver a seleccionar mapa
                    break
                # dibujar fondo y panel
                self.pantalla.blit(self.fondo, (shift_x, shift_y))
                self.pantalla.fill(COLORPANEL,
                                   (int(XMAPAMAX*scale+shift_x), shift_y,
                                    int(DXPANEL*scale), int(900*scale)))
                if self.jugar:
                    self.pantalla.blit(self.jp1,
                                       (int(XBICHO*scale+shift_x),
                                        int(YBICHO*scale+shift_y)))
                    self.estadobicho = ESTADONORMAL
                    pygame.display.flip()
                    if self.jugarNivel() == 1:
                        return
                    self._score = self._score + self.puntos
                    self._average = self._score / self._game_times
                else:
                    if self.bandera:
                        self.pantalla.blit(self.bandera,
                                           (int((XMAPAMAX+47)*scale+shift_x),
                                            int(155*scale+shift_y)))
                    yLinea = int(YTEXTO*scale) + shift_y + \
                        self.fuente9.get_height()
                    for par in self.lista_estadisticas:
                        text1 = self.fuente9.render(
                            par[0], 1, COLORESTADISTICAS1)
                        self.pantalla.blit(text1,
                                           ((XMAPAMAX+10)*scale+shift_x, yLinea))
                        text2 = self.fuente9.render(
                            par[1], 1, COLORESTADISTICAS2)
                        self.pantalla.blit(text2,
                                           ((XMAPAMAX+135)*scale+shift_x, yLinea))
                        yLinea = yLinea+self.fuente9.get_height()+int(5*scale)

                    pygame.display.flip()
                    if self.explorarNombres() == 1:
                        return


def main():
    juego = Conozco()
    juego.run()

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    main()
