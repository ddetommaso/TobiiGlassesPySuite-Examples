# live_scene_and_gaze.py : A demo for video streaming and synchronized gaze
#
# Copyright (C) 2018  Davide De Tommaso
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import numpy as np

if hasattr(__builtins__, 'raw_input'):
      input=raw_input

import sys
sys.path.append("../..")
import threading

import os
import tobiiglasses.entities as entities
from tobiiglasses.recordings import Recording

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('projects_dir', metavar='projects_dir', type=str, nargs='+',
                    help='The path of the directory where projects.ttgp is located')
parser.add_argument('project_id', metavar='project_id', type=str, nargs='+',
                    help='The project_id (or folder name) from where import the recordings')
parser.add_argument('recording_id', metavar='recording_id', type=str, nargs='+',
                    help='The recording_id (or folder name) from where import the segments')
args = parser.parse_args()

rec = Recording(args.projects_dir[0], args.project_id[0], args.recording_id[0])
rec.play(segment_id=1)
