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

# DB restarten
/etc / init.d / mysqld restart

# Datenbank erstellen
create database Enterprise
use Enterprise

# Alles in einer Tabelle mysql
create table enterprise(
    id int primary key auto_increment, film varchar(50), year int, captain varchar(20), ship varchar(40));

# Alles in einer Tabelle sqlite
create table enterprise(
    id integer primary key autoincrement, film TEXT, year int, captain TEXT, ship TEXT);


```sql
INSERT INTO enterprise (film, year, captain, ship) VALUES
('Star Trek: Der Film', 1979, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek II: Der Zorn des Khan', 1982, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek III: Auf der Suche nach Mr. Spock', 1984, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek IV: Zurück in die Gegenwart', 1986, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek V: Am Rande des Universums', 1989, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek VI: Das unentdeckte Land', 1991, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek: Treffen der Generationen', 1994, 'Jean-Luc Picard', 'USS Enterprise (NCC-1701-D)'),
('Star Trek: Der erste Kontakt', 1996, 'Jean-Luc Picard', 'USS Enterprise (NCC-1701-D)'),
('Star Trek: Der Aufstand', 1998, 'Jean-Luc Picard', 'USS Enterprise (NCC-1701-D)'),
('Star Trek: Nemesis', 2002, 'Jean-Luc Picard', 'USS Enterprise (NCC-1701-E)'),
('Star Trek', 2009, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek Into Darkness', 2013, 'James T. Kirk', 'USS Enterprise (NCC-1701)'),
('Star Trek Beyond', 2016, 'James T. Kirk', 'USS Enterprise (NCC-1701)');
```

# Tabellen erstellen
drop table if exists person
create table person(
    id int primary key auto_increment,
    vorname varchar(20),
    nachname varchar(20),
    schiff_id int)

insert into person values(NULL, 'James T.', 'Kirk', 1);
insert into person values(NULL, 'Willard', 'Decker', 1);
insert into person values(NULL, 'Jean-Luc', 'Picard', 2);
insert into person values(NULL, 'Han', 'Solo', 3);
insert into person values(NULL, 'Wilhuff', 'Tarkin', 4);
insert into person values(NULL, 'Mal', 'Reynolds', 5);

drop table if exists film
create table film(
    id int primary key auto_increment,
    titel varchar(40),
    jahr int,
    budget int);

insert into film values(NULL, 'Star Trek', 1979, 46);
insert into film values(NULL, 'Star Trek: Generations', 1994, 35);
insert into film values(NULL, 'Star Wars 4', 1977, 11);
insert into film values(NULL, 'Star Wars 5', 1980, 33);
insert into film values(NULL, 'Serenity', 2005, 39);

drop table if exists schiff
create table schiff(
    id int primary key auto_increment,
    name varchar(20));

insert into schiff values(NULL, 'USS Enterprise');
insert into schiff values(NULL, 'USS Enterprise');
insert into schiff values(NULL, 'Millennium Falcon');
insert into schiff values(NULL, 'Death Star');
insert into schiff values(NULL, 'Serenity');

drop table if exists personfilm
create table personfilm(
    id int primary key auto_increment,
    person_id int,
    film_id int)

insert into personfilm values(NULL, 1, 1);
insert into personfilm values(NULL, 1, 2);
insert into personfilm values(NULL, 2, 1);
insert into personfilm values(NULL, 3, 2);
insert into personfilm values(NULL, 4, 3);
insert into personfilm values(NULL, 4, 4);
insert into personfilm values(NULL, 5, 3);
insert into personfilm values(NULL, 6, 5);

# select-Statements
select * from person
select a.vorname, a.nachname, s.name as Schiff from person as a, schiff as s where a.schiff_id = s.id
