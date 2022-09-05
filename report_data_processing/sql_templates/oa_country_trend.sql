SELECT
  crossref.published_year AS year,
  c.name as name,
  COUNT(doi) AS total,
  COUNTIF(unpaywall.is_oa IS true) AS open,
  COUNTIF(unpaywall.is_oa IS false) AS closed,
  COUNTIF((unpaywall.gold IS true) OR (unpaywall.bronze IS TRUE)) AS publisher,
  COUNTIF(unpaywall.green IS true) AS other_platform,
  COUNTIF(((unpaywall.gold IS true) OR (unpaywall.bronze IS TRUE))
              AND (unpaywall.green IS FALSE)) AS publisher_only,
  COUNTIF(((unpaywall.gold IS true) OR (unpaywall.bronze IS TRUE))
              AND (unpaywall.green IS TRUE)) AS both,
  COUNTIF(unpaywall.green_only_ignoring_bronze IS true) AS other_platform_only
FROM `{doi_table}`, UNNEST(affiliations.countries) as c
WHERE crossref.published_year>1999 AND crossref.published_year<2022 AND unpaywall.is_oa IS NOT NULL
GROUP BY name, year
ORDER BY year DESC, name ASC