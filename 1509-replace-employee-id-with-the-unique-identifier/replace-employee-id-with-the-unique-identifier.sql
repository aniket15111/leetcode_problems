# Write your MySQL query statement below
select 
    et.unique_id,
    e.name

from Employees as e
left join EmployeeUNI as et
on e.id =et.id