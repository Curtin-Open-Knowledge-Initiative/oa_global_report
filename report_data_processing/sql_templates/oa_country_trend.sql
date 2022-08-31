SELECT
  name,
  time_period AS year,
  oa_coki.open.total AS open,
  oa_coki.closed.total AS closed,
  oa_coki.publisher.total AS publisher,
  oa_coki.other_platform.total AS other_platform,
  oa_coki.publisher_only.total AS publisher_only,
  oa_coki.both.total AS both,
  oa_coki.other_platform_only.total AS other_platform_only
FROM `academic-observatory.observatory.country20220827`
WHERE time_period>1999 AND time_period<2022
