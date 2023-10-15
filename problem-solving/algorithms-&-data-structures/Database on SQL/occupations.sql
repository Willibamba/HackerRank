/*
Pivots the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Prints NULL when there are no more names corresponding to an occupation.

Enter your query here.
*/

Select MAX(CASE WHEN Occupation = "Doctor" THEN Name END),
       MAX(CASE WHEN Occupation = "Professor" THEN Name END),
       MAX(CASE WHEN Occupation = "Singer" THEN Name END),
       MAX(CASE WHEN Occupation = "Actor" THEN Name END)
From (Select Occupation, Name, RANK() OVER(PARTITION BY Occupation ORDER BY Name) AS r_n
FROM OCCUPATIONS) AS subquery GROUP BY r_n ORDER BY r_n;

/*
Input Sample:
                    OCCUPATIONS table
            _________________________________________
           |    Name            |   Occuaption       |
           |____________________|____________________|
           | Samantha           | Doctor             |
           | Julia              | Actor              |
           | Maria              | Actor              |
           | Meera              | Singer             |
           | Ashley             | Professor          |
           | Ketty              | Professor          |
           | Christeen          | Professor          |
           | Jane               | Actor              |
           | Jenny              | Doctor             |
           | Priya              | Singer             |
           |____________________|____________________|
           
Output Sample:
              ____________________________________________
             | Doctor    |Professor  |Singer     |Actor   |
             |___________|___________|___________|________|
             | Jenny     |Ashley     |Meera      |Jane    |
             | Samantha  |Christeen  |Priya      |Julia   |
             | NULL      |Ketty      |NULL       |Maria   |
             |___________|___________|___________|________|
*/