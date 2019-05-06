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

from tobiiglasses.recordings import Recording
from tobiiglasses.filters.fixations import FilterDT
from tobiiglasses.filters.df import BetweenTimestamps, BetweenLoggedEvents
from tobiiglasses.aoi.models import GaussianMixture

parser = argparse.ArgumentParser()
parser.add_argument('projects_dir', metavar='projects_dir', type=str, nargs='+',
                    help='The path of the directory where projects.ttgp is located')
parser.add_argument('project_id', metavar='project_id', type=str, nargs='+',
                    help='The project_id (or folder name) from where import the recordings')
parser.add_argument('recording_id', metavar='recording_id', type=str, nargs='+',
                    help='The recording_id (or folder name) from where import the segments')
args = parser.parse_args()

rec = Recording(args.projects_dir[0], args.project_id[0], args.recording_id[0])
rec.exportCSV_Fixations(fixation_filter=FilterDT(), aoi_model=GaussianMixture(n_clusters=2), aoi_plot=True)
