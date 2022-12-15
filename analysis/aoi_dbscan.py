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
from tobiiglasses.aoi.clustering import GaussianMixture

import os
import csv
import pandas as pd
import logging
import argparse
from tobiiglasses.gazedata import GazeData
from tobiiglasses.aoi.clustering import GaussianMixture, DBSCAN
from tobiiglasses.filters.df import SingleLoggedEvent


parser = argparse.ArgumentParser()
parser.add_argument('projects_dir', metavar='projects_dir', type=str, nargs='+',
                    help='The path of the directory where projects.ttgp is located')
parser.add_argument('project_id', metavar='project_id', type=str, nargs='+',
                    help='The project_id (or folder name) from where import the recordings')
parser.add_argument('recording_id', metavar='recording_id', type=str, nargs='+',
                    help='The recording_id (or folder name) from where import the segments')
args = parser.parse_args()

rec = Recording(args.projects_dir[0], args.project_id[0], args.recording_id[0])
dbscan = DBSCAN(eps=10.0, min_samples=3)
df = rec.getGazeData().toDataFrame()
f = SingleLoggedEvent("start_recording")
res, trial_start_ts = f.getFilteredData(df, columns=[GazeData.Timestamp, GazeData.LoggedEvents])
rec.saveVideoSnapshot(os.path.join(".", "snapshot.png"), ts=trial_start_ts[0], segment_id=1)
fixations = rec.getFixations(segment_id=1, fixation_filter=FilterDT(), aoi_model=dbscan)
dbscan.savePlot(filename=os.path.join(".", ",mutual.pdf"), background_image=os.path.join(".", "snapshot.png"))
