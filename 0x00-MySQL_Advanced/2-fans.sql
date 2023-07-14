-- sn aql script that ranks country origin of bands 
-- ordered bu the nu,ber of non-unique fan

SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
