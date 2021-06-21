-- Male COVID19 vaccine recipients, 50 years old, in the state of Ohio, who were hospitalized.

.header on
.mode column

SELECT D.[STATE], D.CAGE_YR, D.SEX, D.HOSPITAL, D.HOSPDAYS, D.VAX_DATE, V.VAX_TYPE, V.VAX_MANU, V.VAX_LOT
FROM VData AS D
	INNER JOIN Vaccines AS V ON V.VAERS_ID = D.VAERS_ID
WHERE D.SEX = 'M' AND D.HOSPITAL = 'Y' AND D.CAGE_YR = 50 AND D.[State] = 'OH' AND V.VAX_TYPE = 'COVID19'
ORDER BY D.VAX_DATE;