#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Team:
#   J Phani Mahesh <phanimahesh@gmail.com>
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com>
#   Amith KK <amithkumaran@gmail.com>
#   Georgi Karavasilev <motorslav@gmail.com>
#   Sam Tran <samvtran@gmail.com>
#   Sam Hewitt <hewittsamuel@gmail.com>
#   Angel Araya <al.arayaq@gmail.com>
#
# Description:
#   A One-stop configuration tool for Unity.
#
# Legal Stuff:
#
# This file is a part of Unity Tweak Tool
#
# Unity Tweak Tool is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Unity Tweak Tool is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import sys,os
from gi.repository import Gio,  Gdk,Gtk
import UnityTweakTool.config.data as data
import UnityTweakTool.section.dynamic as dynamic


def test_schema(schema):
    if schema in Gio.Settings.list_relocatable_schemas():
        pass
    elif schema not in Gio.Settings.list_schemas():
        print(f"Error: schema {schema} not installed")
        builder=Gtk.Builder()
        builder.set_translation_domain('unity-tweak-tool')
        ui = os.path.join(data.get_data_path(),'errordialog.ui')
        builder.add_from_file(ui)
        dialog = builder.get_object('errordialog')
        message = schema + "\n\nIn order to work properly, Unity Tweak Tool recommends you install the necessary packages"
        dialog.format_secondary_text(message)
        dialog.run()
        sys.exit()

def test_key(schema, key):
    return key in schema.list_keys()

def plugin(plugin):
    schema = f'org.compiz.{plugin}'
    path = f'/org/compiz/profiles/unity/plugins/{plugin}/'
    test_schema(schema)
    return Gio.Settings(schema = schema,  path = path)

def unity(child = None):
    schema = 'com.canonical.Unity'
    schema = f'{schema}.{child}' if child else schema
    test_schema(schema)
    return Gio.Settings(schema)

def canonical(child):
    schema = f'com.canonical.{child}'
    test_schema(schema)
    return Gio.Settings(schema)

def compiz(child):
    schema = f'org.compiz.{child}'
    test_schema(schema)
    return Gio.Settings(schema)

def gnome(child):
    schema = f'org.gnome.{child}'
    test_schema(schema)
    return Gio.Settings(schema)

def color_to_hash(c,alpha=1):
    """Convert a Gdk.Color or Gdk.RGBA object to hex representation, overriding the alpha if asked"""
    if isinstance(c, Gdk.Color):
        return "#{:02x}{:02x}{:02x}{:02x}".format(*[round(x*255) for x in [c.red_float, c.green_float, c.blue_float,alpha]])
    if isinstance(x, Gdk.RGBA):
        return "#{:02x}{:02x}{:02x}{:02x}".format(*[round(x*255) for x in [c.red, c.green, c.blue, alpha]])
    # If it is neither a Gdk.Color object nor a Gdk.RGBA object,
    raise NotImplementedError

# GSettings objects go here

# Sorted by function type and alphabetical order

bluetooth = canonical('indicator.bluetooth')
datetime = canonical('indicator.datetime')
hud = canonical('indicator.appmenu.hud')
power = canonical('indicator.power')
notifyosd = canonical('notify-osd')
session = canonical('indicator.session')
sound = canonical('indicator.sound')

antialiasing = gnome('settings-daemon.plugins.xsettings')
background = gnome('desktop.background')
desktop = gnome('nautilus.desktop')
interface = gnome('desktop.interface')
lockdown = gnome('desktop.lockdown')
wm = gnome('desktop.wm.preferences')
touch = gnome(f'{dynamic.touchpad_schema}.peripherals.touchpad')

animation = plugin('animation')
core = plugin('core')
expo = plugin('expo')
grid = plugin('grid')
move = plugin('move')
opengl = plugin('opengl')
resize = plugin('resize')
scale = plugin('scale')
unityshell = plugin('unityshell')
zoom = plugin('ezoom')

launcher = unity('Launcher')
lenses = unity('Lenses')
lens_apps = unity('ApplicationsLens')
lens_files = unity('FilesLens')
runner = unity('Runner')
