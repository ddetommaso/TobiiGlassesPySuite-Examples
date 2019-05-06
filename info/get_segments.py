#   Copyright (C) 2019  Davide De Tommaso
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>

import os
import argparse
import tobiiglasses.entities

parser = argparse.ArgumentParser()
parser.add_argument('projects_dir', metavar='projects_dir', type=str, nargs='+',
                    help='The path of the directory where projects.ttgp is located')
parser.add_argument('project_id', metavar='project_id', type=str, nargs='+',
                    help='The project_id (or folder name) from where import the recordings')
parser.add_argument('recording_id', metavar='recording_id', type=str, nargs='+',
                    help='The recording_id (or folder name) from where import the segments')
args = parser.parse_args()

recordings_path = tobiiglasses.entities.get_recordings_path(args.projects_dir[0], args.project_id[0])
segments = tobiiglasses.entities.get_all_segments(recordings_path, args.recording_id[0])


print('{0:<8s} {1:<20s} {2:<20s}'.format('id', 'calibrated', 'length (us)') )
for s in segments:
    print('{0:<8s} {1:<20s} {2:<20s}'.format(
                    s.getId(), str(s.isCalibrated()), str(s.getLengthUs()) ) )
