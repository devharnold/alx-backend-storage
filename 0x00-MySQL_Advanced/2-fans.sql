-- sql cript that ranks country origin brand
-- order by non-unique fans
SELECT origin, SUM(fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
