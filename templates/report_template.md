{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

{% set report_numbers = load_json(report_numbers.files["report_numbers.json"].cache_filepath) %}
{% set git_status = load_json(git_status.fules["git_status.json"].cache_filepath) %}

<!-- Title Page -->
<pdf:nexttemplate name="titlepage">
<pdf:nextpage>

<p class="subtitle">THE GLOBAL STATE OF OA {{ report_numbers.report_year }}</p>
<p class="titlemeta"><br>REPORT DATE: {{ helper.created_at()|upper }}</p>
<p class="titlemeta"><br>CENSUS PERIOD: {{ report_numbers.census_year.year }}</p>


<!-- switch page templates -->
<pdf:nexttemplate name="report">

<pdf:nextpage>

# Summary

At the end of {{ report_numbers.report_year }} the global open access level for research published in 
{{ report_numbers.census_year.year }} reached {{ report_numbers.census_year.pc_open }}% with an increase of 
{{ report_numbers.census_year.pc_open_increase }}% to {{ report_numbers.census_year.pc_open }} compared to 
outputs published in {{ report_numbers.comparison_year.year }}. Access provided through publisher websites
increased by {{ report_numbers.census_year.pc_publisher_open_increase }}% to 
{{ report_numbers.census_year.pc_publisher }}% for {{ report_numbers.comparison_year.year }} publications.

![]({{ fig_oa_global_trend.files["oa_global_trend.png"].cache_filepath }})

Access through other platforms has not grown to the same extent although embargoes appear to continue to 
have a substantial depression on access through repositories for recent years of publication. As Unpaywall 
commenced recording first availability dates in {{ report_numbers.comparison_year.year }} we cannot compare 
the year on year change. Zero-embargo access through non-publisher platforms for {{ report_numbers.census_year.year }} 
was {{ report_numbers.census_year.pc_other_platform_zero_embargo }}% of all outputs available through other platforms. 
Future reports will track the evolution of immediate other platform open access over time.

# Leading Nations

The countries with the highest levels of open access continue to be countries will small publication output numbers, 
with Indonesia and Brazil dominating amongst countries with more than 10,000 outputs in 
{{ report_numbers.census_year.year }}. A set of European countries, along with South Africa and Mexico follow. 
European countries tend to show higher levels of open access through other platforms, compared to other countries
with high levels of accessibility.

![]({{ fig_oa_country_compare.files["oa_country_compare.png"].cache_filepath }})

<pdf:nextpage>

# Methodology

This report was generated automatically from the source data and the relevant code and state of the repository
is available at {{ git_status.remote_url }} with the commit hash {{ git_status.sha }} on branch {{ git_status.branch }}.

The primary data table used was the final DOI table in the Academic Observatory for 
{{ report_numbers.census_year.year }}, {{ parameters.doi_table }}. Open Access types and the means for
detecting them are as described on the [COKI Open Access Dashboard](https://open.coki.ac/how/).



