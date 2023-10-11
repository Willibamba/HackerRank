/*
A query to print the company_code, founder name, total number of lead managers, total number of senior managers, 
total number of managers, and total number of employees. Order your output by ascending company_code.

Enter your query here.
*/

SELECT Employee.company_code, Company.founder, COUNT(DISTINCT Employee.lead_manager_code), 
COUNT(DISTINCT Employee.senior_manager_code), COUNT(DISTINCT Employee.manager_code), COUNT(DISTINCT Employee.employee_code)
FROM Employee
INNER JOIN Company ON Employee.company_code = Company.company_code
GROUP BY Employee.company_code, Company.founder
ORDER BY Employee.company_code ASC;

/*  Sample Input: Tables
      Company                             Lead Manager                      
     _________________________       _________________________________
    |company_code  | founder  |     | lead_manager_code | company_code|
    |______________|__________|     |___________________|_____________|
    |   C1         | Monika   |     |   LM1             |   C1        |
    |   C2         | Samantha |     |   LM2             |   C2        |
    |______________|__________|     |___________________|_____________|

                Senior Manager
     ________________________________________________________
    | senior_manager_code | lead_manager_code | company_code |
    |_____________________|___________________|______________|
    |   SM1               |   LM1             |  C1          |
    |   SM2               |   LM1             |  C1          |
    |   SM3               |   LM2             |  C2          |
    |_____________________|___________________|______________|

                    Manager 
     _______________________________________________________________________
    | manager_code | senior_manager_code | lead_manager_code | company_code |
    |______________|_____________________|___________________|______________|
    |   M1         |    SM1              |    LM1            |   C1         |
    |   M2         |    SM3              |    LM2            |   C2         |
    |   M3         |    SM3              |    LM2            |   C2         |
    |______________|_____________________|___________________|______________|

                    Employee
     ______________________________________________________________________________________
    | employee_code | manager_code | senior_amanger_code | lead_manager_code | company_code|
    |_______________|______________|_____________________|___________________|_____________|
    |  E1           |   M1         |     SM1             |    LM1            |   C1        |
    |  E2           |   M1         |     SM1             |    LM1            |   C1        |
    |  E3           |   M2         |     SM3             |    LM2            |   C2        |
    |  E4           |   M3         |     SM3             |    LM2            |   C2        |
    |_______________|______________|_____________________|___________________|_____________|

    Sample Output:

        C1 Monika 1 2 1 2
        C2 Samantha 1 1 2 2
    */
    