{% import "report_macros.md" as helper with context %}
{% include "report_css.html" %}

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
{{ report_numbers.census_year.year }} reached {{ report_numbers.census_year.pc_oa }}% with an increase of 
{{ report_numbers.census_year.pc_open_increase }}% to {{ report_numbers.census_year.pc_open }} compared to 
outputs published in {{ report_numbers.comparison_year.year }}. Access provided through publisher websites
increased by {{ report_numbers.census_year.pc_publisher_open_increase }}% to 
{{ report_numbers.census_year.pc_publisher_open }}% for {{ report_numbers.comparison_year.year }} publications.

Access through other platforms has not grown to the same extent although embargoes appear to continue to 
have a substantial depression on access through repositories for recent years of publication. As Unpaywall 
commenced recording first availability dates in {{ report_numbers.comparison_year.year }} we cannot compare 
the year on year change. Zero-embargo access through non-publisher platforms for {{ report_numbers.census_year.year }} 
was {{ report_numbers.census_year.pc_other_platform_zero_embargo }}% of all outputs available through other platforms. 
Future reports will track the evolution of immediate other platform open access over time.

# Leading Nations and Biggest Movers

The countries with the highest levels of open access continue to be countries will small publication output numbers, 
with Indonesia and Brazil dominating amongst countries with more than 10,000 outputs in 
{{ report_numbers.census_year.year }}. A set of European countries, along with South Africa and Mexico follow. 
European countries tend to show higher levels of open access through other platforms, compared to other countries
with high levels of accessibility.



