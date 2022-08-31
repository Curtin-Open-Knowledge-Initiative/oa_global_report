SELECT
  crossref.published_year AS year,
  COUNT(doi) AS total,
  COUNTIF(coki.oa_coki.open IS true) AS open,
  COUNTIF(coki.oa_coki.closed IS true) AS closed,
  COUNTIF(coki.oa_coki.publisher IS true) AS publisher,
  COUNTIF(coki.oa_coki.other_platform IS true) AS other_platform,
  COUNTIF(coki.oa_coki.publisher_only IS true) AS publisher_only,
  COUNTIF(coki.oa_coki.both IS true) AS both,
  COUNTIF(coki.oa_coki.other_platform_only IS true) AS other_platform_only
FROM `academic-observatory.observatory.doi20220827`
WHERE crossref.published_year>1999 AND crossref.published_year<2022 AND coki.oa_coki IS NOT NULL
GROUP BY year
ORDER BY year