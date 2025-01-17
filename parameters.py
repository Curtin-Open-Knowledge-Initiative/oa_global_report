# COKI CURTIN RESEARCH QUALITITES REPORT
#
# Copyright 2021 ######
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: COKI Team

# Utility functions
from pathlib import Path

# which data year to run. The final year is *not* included so for eg 2010 to 2019 use (2010, 2020)

REPORT_YEAR = 2021
CENSUS_YEAR = REPORT_YEAR -1
YEARS = range(2010, REPORT_YEAR + 1 )

# oa types
OA_TYPES = [
    'open',
    'closed',
    'publisher',
    'other_platform',
    'both',
    'other_platform_only',
    'publisher_only'
]
# measures of central location
C_LOCS = ['mean', 'median']

# Table Locations
RERUN = True
VERBOSE = True
PROJECT_ID = 'coki-scratch-space'
DOI_TABLE = 'academic-observatory.observatory.doi20211211'
UNPAYWALL_TABLE = 'academic-observatory.our_research.unpaywall'

DESTINATION_TABLES = {
}

# File Locations
DATA_FOLDER = Path('tempdata')
DAG_FILENAME = 'dag.pkl'
DAG_FILEPATH = DATA_FOLDER / DAG_FILENAME
REPORT_DATA_FILENAME = 'report_numbers.json'
REPORT_DATA_FILEPATH = DATA_FOLDER / REPORT_DATA_FILENAME
REPORT_ARCHIVES_DIR = Path('reports')

SQL_TEMPLATE_PARAMETERS = dict(
    years=YEARS,
    start_year=YEARS[0],
    end_year=YEARS[-1],
    doi_table=DOI_TABLE,
    unpaywall=UNPAYWALL_TABLE
)

# color mapping when comparing regions
COLOR_MAP_REGIONS = {
    "Asia": 'orange',
    "Europe": 'limegreen',
    "Americas": 'brown',
    "Oceania": 'red',
    "Africa": 'magenta'
}

# display order when comparing regions
ORDER_REGIONS = ["Asia", "Europe", "Americas", "Oceania", "Africa"]

# color mapping when comparing subregions
COLOR_MAP_SUBREGIONS = {
    "Eastern Asia": 'orange',
    "Southern Asia": 'orange',
    "Western Asia": 'orange',
    "South-eastern Asia": 'orange',
    "Central Asia": 'orange',
    "Southern Europe": 'limegreen',
    "Eastern Europe": 'limegreen',
    "Western Europe": 'limegreen',
    "Northern Europe": 'limegreen',
    "Latin America and the Caribbean": 'brown',
    "Northern America": 'dodgerblue',
    "Australia and New Zealand": 'red',
    "Melanesia": 'red',
    "Polynesia": 'red',
    "Micronesia": 'red',
    "Northern Africa": 'magenta',
    "Sub-Saharan Africa": 'magenta'
}

# line type mapping when comparing subregions
DASH_MAP_SUBREGIONS = {
    "Eastern Asia": 'solid',
    "Southern Asia": 'longdash',
    "Western Asia": 'dash',
    "South-eastern Asia": 'dashdot',
    "Central Asia": 'dot',
    "Southern Europe": 'solid',
    "Eastern Europe": 'dash',
    "Western Europe": 'dashdot',
    "Northern Europe": 'dot',
    "Latin America and the Caribbean": 'solid',
    "Northern America": 'solid',
    "Australia and New Zealand": 'solid',
    "Melanesia": 'dash',
    "Polynesia": 'dashdot',
    "Micronesia": 'dot',
    "Northern Africa": 'solid',
    "Sub-Saharan Africa": 'dash'
}

# display order when comparing subregions
ORDER_SUBREGIONS = [
    "Eastern Asia", "Southern Asia", "Western Asia", "South-eastern Asia", "Central Asia",
    "Southern Europe", "Eastern Europe", "Western Europe", "Northern Europe",
    "Latin America and the Caribbean", "Northern America", "Australia and New Zealand", "Melanesia",
    "Polynesia", "Micronesia", "Northern Africa", "Sub-Saharan Africa"
]

# plotly figure sizes
FIG_SCALE = 1
FIG_WIDTH = 1000
FIG_HEIGHT = 600
