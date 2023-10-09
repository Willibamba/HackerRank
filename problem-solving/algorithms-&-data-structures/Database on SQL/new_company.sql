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
