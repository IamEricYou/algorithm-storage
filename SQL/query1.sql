-- To see if there are any ducplicates in a certain field
SELECT payment_method, COUNT(*) FROM flanb_point_of_interest WHERE status='JHR' GROUP BY payment_method HAVING count(*) > 1;

-- Basic templates

SELECT price_range FROM flanb_point_of_interest LIMIT 20;
SELECT meta FROM flanb_point_of_interest WHERE status='JHR' LIMIT 40;
SELECT vendor_uid From flanb_point_of_interest LIMIT 30;
SELECT create_dt, update_dt FROM flanb_point_of_interest WHERE status='JHR' LIMIT 40;
SELECT * FROM flanb_point_of_interest WHERE status='JHR' AND images IS NOT NULL LIMIT 40;
SELECT count(*) FROM flanb_point_of_interest WHERE status='JHR';
SELECT count(*) FROM flanb_point_of_interest;
SELECT count(*) FROM flanb_point_of_interest WHERE status='JHR' and flan is NULL;
SELECT position, metaFROM flanb_point_of_interest WHERE status='JHR' LIMIT 50;
SELECT * FROM flanb_point_of_interest WHERE status='JHR' LIMIT 50;
SELECT payment_method, COUNT(*) FROM flanb_point_of_interest WHERE status='JHR' GROUP BY payment_method HAVING count(*) > 1;

-- Query with times

SELECT count(*) FROM flanb_point_of_interest WHERE status='JHR';
SELECT meta FROM flanb_point_of_interest WHERE status='JHR' LIMIT 10;
SELECT * FROM flanb_point_of_interest WHERE status='JHR' and create_dt > '2020-5-20 14:00:00' LIMIT 50;

-- Query to see if a word mathces a certain word in a column

SELECT count(*) FROM flanb_point_of_interest WHERE status='JHR' and vendor_link like '%kaohsiung%';

-- Search for empty sting for columns
select count(*) from flanb_point_of_interest where (vendor_link = '') IS FALSE;
select count(*) from flanb_point_of_interest where (vendor_link = '') IS TRUE;

-- Search item in json

select * from flanb_point_of_interest fpoi where meta->'meta' is null and status in ('YNC', 'YNC2', 'JHR');

-- update query

update flanb_point_of_interest set city_id=183694 where vendor_link like 'https://tw.openrice.com/en/kaohsiung-pingtung/%';

-- left join

select fpoi.vendor_link, flanb_poi.code from flanb_point_of_interest fpoi left join flanb_poi on fpoi.city_id = flanb_poi.id where (fpoi.vendor_link = '') is FALSE