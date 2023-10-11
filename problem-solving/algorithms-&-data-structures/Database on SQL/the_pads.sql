/*
Generates the following two result sets:

1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed      by the first letter of each profession as a parenthetical (i.e.: enclosed in                parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and          ASingerName(S).
2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences      in ascending order, and output them in the following format:

   There are a total of [occupation_count] [occupation]s

Enter your query here.
*/

SELECT CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') FROM OCCUPATIONS ORDER BY Name ASC;

SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.') 
FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(Occupation), Occupation;

/*  Sample Input: Table
                OCCUPATIONS
    ____________________________________________
    |       Name        |       Occupation      |
    |___________________|_______________________|
    |   Samantha        |   Doctor              |
    |   Julia           |   Actor               |
    |   Maria           |   Actor               |
    |   Meera           |   Singer              |
    |   Ashley          |   Professor           |
    |   Ketty           |   Professor           |
    |   Christeen       |   Professor           |
    |   Jane            |   Actor               |
    |   Jenny           |   Doctor              |
    |   Priya           |   Singer              |
    |___________________|_______________________|

    Sample Output:

    Ashely(P)
    Christeen(P)
    Jane(A)
    Jenny(D)
    Julia(A)
    Ketty(P)
    Maria(A)
    Meera(S)
    Priya(S)
    Samantha(D)
    There are a total of 2 doctors.
    There are a total of 2 singers.
    There are a total of 3 actors.
    There are a total of 3 professors.
*/
