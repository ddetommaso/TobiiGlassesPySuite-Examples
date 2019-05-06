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

import tobiiglasses.entities
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('projects_dir', metavar='projects_dir', type=str, nargs='+',
                    help='The path of the directory where projects.ttgp is located')
parser.add_argument('project_id', metavar='project_id', type=str, nargs='+',
                    help='The project_id (or folder name) from where import the recordings')
args = parser.parse_args()

recordings = tobiiglasses.entities.get_all_recordings(args.projects_dir[0], args.project_id[0])


print('{0:<8s} {1:<30s} {2:<30s} {3:<30s} {4:<20s} {5:<3s}'.format('Rec Id', 'Rec Name', 'Creation Date', 'Participant Name', 'Valid Samples (%)', 'Segments nr'))
for r in recordings:
    if float(r.getEtSamples()) == 0:
        validity = 0
    else:
        validity = int(100*(r.getEtValidSamples()/float(r.getEtSamples())))
    print('{0:<8s} {1:<30s} {2:<30s} {3:<30s} {4:<20s} {5:<3s}'.format(
                    r.getId(), r.getName(), str(r.getCreationDate()),
                    r.getParticipant().getName(),
                    str(validity),
                    str(r.getSegmentsN()) ) )
