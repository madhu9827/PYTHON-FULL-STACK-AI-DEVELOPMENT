mysql -uroot -proot 

show databases;

create database dbtwo;
use dbtwo;

create table employees(
eid int,
ename varchar(32),
esal float,
primary key(eid)
);