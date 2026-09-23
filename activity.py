#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gettext import gettext as _

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton

import pygame
import sugargame.canvas
import conozco


class ConzocoActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1
        self.sound_enable = True
        self.build_toolbar()
        self.game = conozco.Conozco(self)
        self.game.canvas = sugargame.canvas.PygameCanvas(
            self, main=self.game.run, modules=[
                pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def build_toolbar(self):
        toolbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbox.toolbar.insert(activity_button, 0)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = True
        toolbox.toolbar.insert(separator, -1)
        separator.show()

        sound_button = ToolButton('speaker-muted-100')
        sound_button.set_tooltip(_('Sound'))
        sound_button.connect('clicked', self.sound_control)
        toolbox.toolbar.insert(sound_button, -1)
        sound_button.show()

        separator2 = Gtk.SeparatorToolItem()
        separator2.props.draw = False
        separator2.set_expand(True)
        toolbox.toolbar.insert(separator2, -1)
        separator2.show()

        stop_button = StopButton(self)
        stop_button.props.accelerator = _('<Ctrl>Q')
        toolbox.toolbar.insert(stop_button, -1)
        stop_button.show()

        toolbox.show()
        self.set_toolbar_box(toolbox)
        self.show_all()

    def sound_control(self, button):
        self.sound_enable = not self.sound_enable
        self.sound_enable = self.game.change_sound(self.sound_enable)
        if not self.sound_enable:
            button.set_icon_name('speaker-muted-000')
            button.set_tooltip(_('No sound'))
        else:
            button.set_icon_name('speaker-muted-100')
            button.set_tooltip(_('Sound'))
