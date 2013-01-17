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

''' Definitions for Checkbox element. '''
from UnityTweakTool.backends import gsettings

import logging
logger=logging.getLogger('UnityTweakTool.elements.checkbox')

class CheckBox:
    def __init__(self,controlObj):
        self.id         = controlObj['id']
        self.ui         = controlObj['builder'].get_obj(controlObj['id'])
        self.schema     = controlObj['schema']
        self.path       = controlObj['path']
        self.key        = controlObj['key']
        self.type       = controlObj['type']
        self.map        = controlObj['map']
        self.invmap     = dict([ (v,k) for (k,v) in self.map.items() ])
        self.dependants = controlObj['dependants']
        assert gsettings.is_valid(
            schema=self.schema,
            path=self.path,
            key=self.key
            )

    def refresh(self):
        self.ui.set_active(
            self.map[
                gsettings.get(
                    schema=self.schema,
                    path  =self.path,
                    key   =self.key,
                    type  =self.type
                    )
                ]
            )
    
    def handle(self,*args,**kwargs):
        gsettings.set(
            schema=self.schema,
            path=self.path,
            key=self.key,
            type=self.type,
            value=self.invmap[self.ui.get_active()]
            )
