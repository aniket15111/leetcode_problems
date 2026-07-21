# Write your MySQL query statement below
select 
    pt.product_name,
    st.year,
    st.price
from Sales as st
left join Product as pt
on st.product_id=pt.product_id