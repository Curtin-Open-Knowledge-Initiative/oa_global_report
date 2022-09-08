{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

{% set report_numbers = load_json(report_numbers.files["report_numbers.json"].cache_filepath) %}
{% set git_status = load_json(git_status.files["git_status.json"].cache_filepath) %}

<pdf:nextpage>

# TT

<!-- Title Page -->

<pdf:nexttemplate name="titlepage">

<pdf:nextpage>

<p class="subtitle">THE GLOBAL STATE OF OPEN ACCESS {{ report_numbers.report_year }}</p>
<p class="titlemeta"><br>REPORT DATE: {{ helper.created_at()|upper }}</p>
<p class="titlemeta"><br>CENSUS PERIOD: {{ report_numbers.census_year.year }}</p>


<!-- switch page templates -->

<pdf:nexttemplate name="report">

<pdf:nextpage>

# Summary

At the end of {{ report_numbers.report_year }} the global open access level for research published in 
{{ report_numbers.census_year.year }} reached {{ report_numbers.census_year.pc_open }}% with an increase of 
{{ report_numbers.census_year.pc_open_increase }}% compared to 
outputs published in {{ report_numbers.comparison_year.year }}. Access provided through publisher websites
increased by {{ report_numbers.census_year.pc_publisher_increase }}% to 
{{ report_numbers.census_year.pc_publisher }}% for {{ report_numbers.comparison_year.year }} publications.

![]({{ fig_oa_global_trend.files["oa_global_trend.png"].cache_filepath }})

Access through other platforms was {{ report_numbers.census_year.pc_other_platform }}% in 
{{ report_numbers.census_year.year }} with no growth compared to {{ report_numbers.comparison_year.year }} publications. 
This may be the result of embargos depressing rates of access through repositories for the most recent years of 
publication. Zero-embargo access through non-publisher platforms for {{ report_numbers.census_year.year }} 
was {{ report_numbers.census_year.pc_other_platform_zero_embargo }}% of all outputs available through other platforms.
Future reports will track the evolution of immediate other platform open access over time.

<pdf:nextpage>

# Open Access by Country

The countries with the highest levels of open access continue to be countries will small publication output numbers, 
with Indonesia and Brazil dominating amongst countries with more than 10,000 outputs in 
{{ report_numbers.census_year.year }} with a set of European countries following. 
European countries tend to show higher levels of open access through other platforms, compared to other countries
with high levels of accessibility and this is in part due to generally shorter embargos, particularly in north-western
Europe.

![]({{ fig_oa_country_compare.files["oa_country_compare.png"].cache_filepath }})

<pdf:nextpage>

# Methodology

The primary data table used was the final DOI table in the Academic Observatory for 
{{ report_numbers.report_year }}, bigquery://academic-observatory.observatory.doi20211211. Open Access types and 
the analysis for categorising them from Unpaywall are as described on the 
[COKI Open Access Dashboard](https://open.coki.ac/how/).

This report was generated automatically from the source data on {{ helper.created_at() }} and the relevant code and 
state of the repository is available [on github]({{ git_status.remote_url }}):

* Commit hash: `{{ git_status.sha }}`
* Branch: `{{ git_status.branch }}`

<pdf:nexttemplate name="lastpage">
<pdf:nextpage>


