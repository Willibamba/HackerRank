/*
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.

Consider P1(a, b) and P2(c, d) to be two points on a 2D plane.

  - a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
  - b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
  - c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
  - d happens to equal the maximum value in Western Longitude (LONG_W in STATION). 

Enter your query here.
*/

SELECT ROUND((MAX(LAT_N) - MIN(LAT_N)) + (MAX(LONG_W) - MIN(LONG_W)), 4) FROM STATION;

/* 
Sample Input:
        The STATION table description below:
        ----------------------------------
       | Field          | Type            |
       | ---------------|-----------------|
       | ID             | NUMBER          |
       | CITY           | VARCHAR2(21)    |
       | STATE          | VARCHAR2(2)     |
       | LAT_N          | NUMBER          |
       | LONG_W         | NUMBER          |
        -----------------------------------
Sample Output:
            259.6859  =  (144.98906270 - 25.07352606) + (164.87604770 -  25.10565434)
*/