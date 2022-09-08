-- SCHEMA BUILDING

create table if not exists transactions (date date, order_id int, client_id int, prop_id int, prod_price float, prod_qty int);
create table if not exists product_nomenclature (product_id int, product_type text, product_name text);

insert into transactions values ('2020/01/02', 1234, 999, 490756, 50, 1);
insert into transactions values ('2020/01/03', 1234, 999, 389728, 3.56, 4);
insert into transactions values ('2020/01/02', 3456, 845, 490756, 50, 2);
insert into transactions values ('2020/01/03', 3456, 845, 549380, 300, 1);
insert into transactions values ('2020/01/02', 3456, 845, 490756, 10, 6);

insert into product_nomenclature values (490756, 'MEUBLE', 'Chaise');
insert into product_nomenclature values (389728, 'DECO', 'Boule de Noël');
insert into product_nomenclature values (549380, 'MEUBLE', 'Canapé');
insert into product_nomenclature values (293718, 'DECO', 'Mug');

-- PART ONE

select date, sum (prod_qty * prod_price) as chiffre_affaires
from (select distinct * from transactions)
where date >= '01/01/19' and date <= '31/12/19'
group by date
order by date desc

-- PART TWO

select client_id,
       sum(case when product_type = 'MEUBLE' then (prod_price * prod_qty) end) as ventes_meuble,
       sum(case when product_type = 'DECO' then (prod_price * prod_qty) end) as ventes_deco
from (select distinct *
      from transactions as t
      join (select distinct * from products) as p
      on t.prop_id = p.product_id)
where date >= '01/01/19' and date <= '31/12/19'
group by client_id