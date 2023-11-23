/*
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

Enter your query here.
*/

SELECT ROUND(AVG(LAT_N), 4) 
    FROM (SELECT RANK() OVER(ORDER BY LAT_N) AS rn, LAT_N FROM STATION) AS subquerry         WHERE rn = (SELECT CEIL(COUNT(rn)/2) FROM STATION);

/* 
Sample Input:
        The STATION table description below
        ----------------------------------
       | Field          | Type            |
       | ---------------|-----------------|
       | ID             | NUMBER          |
       | CITY           | VARCHAR2(21)    |
       | STATE          | VARCHAR2(2)     |
       | LAT_N          | NUMBER          |
       | LONG_W         | NUMBER          |
        -----------------------------------
    where LAT_N is the northern latitude and LONG_W is the western longitude.
    
Sample Output:
                83.8913 
*/