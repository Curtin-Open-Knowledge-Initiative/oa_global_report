# Open Access Global Reports

This repository provides the code and framework for creating the COKI annual Global State of Open Access reports.
The final reports for each year, starting from 2021 are available at Zenodo as follows:

* 2021 Report: https://doi.org/####

The reporting framework uses an automated documentation engine to pull data from the academic observatory data
system to generate a summary report, which is then modified for each release. Our goal is to release an annual
report close to the beginning of the year following the report date.

## Running the report

To replicate the result graphs and the data analysis in full requires access to the academic-observatory tables. The
repository is pushed to github following a run, with the summary data resulting from the main queries provided. If
the `RERUN` parameter in `parameters.py` is set to `False` the report can be run using that local data.

Running the full report requires the libraries listed in `requirements.txt` as well as pandoc being available from
the local command line. 
