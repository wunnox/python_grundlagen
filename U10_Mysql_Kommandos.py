#############################################
#
# Name: U10_Mysql_Kommandos
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Einrichten einer MySQL DB
#
##############################################


# DB starten
/etc / init.d / mysqld start

# Berechtigungen setzen
insert into user values('*', 'kurs0', password('kurs'), 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', '', '', '', 0, 0, 0, 0)
insert into user values('localhost', 'kurs0', password('kurs'), 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', '', '', '', 0, 0, 0, 0)

# DB restarten
/etc / init.d / mysqld restart

# Datenbank erstellen
create database Enterprise
use Enterprise

# Tabellen erstellen
drop table if exists person
create table person(
    id int primary key auto_increment,
    vorname varchar(20),
    nachname varchar(20),
    schiff_id int)

insert into person values(NULL, 'James T.', 'Kirk', 1)
insert into person values(NULL, 'Willard', 'Decker', 1)
insert into person values(NULL, 'Jean-Luc', 'Picard', 2)
insert into person values(NULL, 'Han', 'Solo', 3)
insert into person values(NULL, 'Wilhuff', 'Tarkin', 4)
insert into person values(NULL, 'Mal', 'Reynolds', 5)

drop table if exists film
create table film(
    id int primary key auto_increment,
    titel varchar(40),
    jahr int,
    budget int)

insert into film values(NULL, 'Star Trek', 1979, 46)
insert into film values(NULL, 'Star Trek: Generations', 1994, 35)
insert into film values(NULL, 'Star Wars 4', 1977, 11)
insert into film values(NULL, 'Star Wars 5', 1980, 33)
insert into film values(NULL, 'Serenity', 2005, 39)

drop table if exists schiff
create table schiff(
    id int primary key auto_increment,
    name varchar(20))

insert into schiff values(NULL, 'USS Enterprise')
insert into schiff values(NULL, 'USS Enterprise')
insert into schiff values(NULL, 'Millennium Falcon')
insert into schiff values(NULL, 'Death Star')
insert into schiff values(NULL, 'Serenity')

drop table if exists personfilm
create table personfilm(
    id int primary key auto_increment,
    person_id int,
    film_id int)

insert into personfilm values(NULL, 1, 1)
insert into personfilm values(NULL, 1, 2)
insert into personfilm values(NULL, 2, 1)
insert into personfilm values(NULL, 3, 2)
insert into personfilm values(NULL, 4, 3)
insert into personfilm values(NULL, 4, 4)
insert into personfilm values(NULL, 5, 3)
insert into personfilm values(NULL, 6, 5)

# select-Statements
select * from person
select a.vorname, a.nachname, s.name as Schiff from person as a, schiff as s where a.schiff_id = s.id
