--
-- CREATE VIEW slug_author, requests and errors
--

create view slug_author as 
select slug, name from articles join authors 
on articles.author = authors.id;

create view requests as
select date(time), count(*) as total 
from log
group by date(time);

create view errors as 
select date(time), count(status) as num, status 
from log 
where status != '200 OK' 
group by date(time), status 
order by date(time);