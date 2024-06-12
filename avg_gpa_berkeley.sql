### GPA data at UC Berkeley

# we can view the overall data like this
SELECT *
FROM ucb_gpa;

# lets look at average gpa for 2022-2023 by department
SELECT Department, "Average GPA", "Academic Year"
FROM ucb_gpa
WHERE "Academic Year" LIKE '2022%'
ORDER BY "Average GPA" DESC;
# it looks like humanities majors had the highest GPAs in 2022-2023

# average gpas by program of study (BS or BA)
SELECT ROUND(AVG("Average GPA"), 3) AS avg_gpa, Degree
FROM ucb_gpa
WHERE "Academic Year" LIKE '2022%'
GROUP BY Degree
ORDER BY AVG("Average GPA") DESC;
# BA degrees had slightly higher GPAs

# lets look at the most 10 most popular majors in 2022 - 2023 as measured by headcount
SELECT Major, "Academic Year", Headcount
FROM ucb_gpa
WHERE "Academic Year" LIKE '2022%'
ORDER BY Headcount DESC
LIMIT 10;

# we can see the sum of those majors by doing
SELECT SUM(Headcount) FROM
(SELECT Major, "Academic Year", Headcount
FROM ucb_gpa
WHERE "Academic Year" LIKE '2022%'
ORDER BY Headcount DESC
LIMIT 10) AS total_headcount;
# so there are 5536 students in the 10 most popular majors

# this database has 10525 students and 84 majors for the 2022-2023 year
SELECT COUNT(Major) as N, SUM(Headcount)
FROM ucb_gpa
WHERE "Academic Year" LIKE '2022%';

# so over half of the students were concentrated in just 10 majors

# we can see the mean GPA by year
SELECT ROUND(AVG("Average GPA"), 2) as avg_gpa, "Academic Year"
FROM ucb_gpa
GROUP BY "Academic Year";
# average GPAs were almost .2 points higher in 2022-23 compared to 2013-14

# Computer science and econ have grown a lot
# Their GPAs have grown a lot too 
SELECT Major, Headcount, "Academic Year", "Average GPA"
FROM ucb_gpa
WHERE Major LIKE '%Computer%' OR "Major" LIKE '%Economics%';
