/*
A query identifying the type of each record in the TRIANGLES table using its three side lengths. Outputs one of the following statements for each record in the table:

    Equilateral: It's a triangle with  sides of equal length.
    Isosceles: It's a triangle with  sides of equal length.
    Scalene: It's a triangle with  sides of differing lengths.
    Not A Triangle: The given values of A, B, and C don't form a triangle.
    
Enter your query here.
*/

SELECT CASE
        WHEN (A = B AND B = C) AND (A + B > C) THEN "Equilateral"
        WHEN (A = B OR B = C OR A = C) AND (A + B > C) THEN "Isosceles"
        WHEN (A <> B AND B <> C AND A <> C) AND (A + B > C) THEN "Scalene"
        ELSE "Not A Triangle" 
    END AS result FROM TRIANGLES;
    
/*
Input Sample:
                TRIANGLES table
         __________________________________
        |    A      |   B      |    C      |
        |----------------------------------|
        | 20        | 20       | 23        |
        | 20        | 20       | 20        |
        | 20        | 21       | 22        |
        | 13        | 14       | 30        |
         ----------------------------------

Sample Output:
        Isosceles
        Equilateral
        Scalene
        Not A Triangle
*/
