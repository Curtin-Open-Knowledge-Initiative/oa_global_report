WITH embargos AS (
    SELECT
        (SELECT oa_locations.oa_date FROM UNNEST(oa_locations) WHERE oa_locations.type = "repository")
    FROM `{unpaywall}`
    WHERE year = {census_year}
)
SELECT
    DATE(published_date)
