###################################################################
#
# Infos zu sqlite3 Datenbanken:
# sqlite3 ist eine einfache relationale Datenbank, welche lediglich aus einem Client
# und einem File, welches die Tabellen beinhaltet, besteht.
# sqlite3 ist Plattform unabhängig und wird heute im Hintergrund von vielen Applikationen
# verwendet, welche eine Datenverwaltung benötigen.
# Es können die bekannten sql-Kommandos (insert, select, update, delete) verwendet werden.
# sqlite kennt nur 5 Datentypen:
#   - Integer: Steht für int, tinyint, smallint etc.
#   - Text: Steht für varchar, nchar, char clob etc.
#   - Blob: Blob
#   - Real: Steht für Real, Double, Float etc.
#   - Numeric: Steht für Numeric, Decimal, Boolean, Date etc.
#
###################################################################

#### Aufbau der Datenbank im Kurs: ####

create table personen(name TEXT, vorname TEXT, personalnummer INTEGER PRIMARY KEY, gehalt FLOAT, geburtstag TEXT)

insert into personen values('Maier', 'Hans', 6714, 3500, '15.03.1962')
insert into personen values('Muster', 'Hans', 8420, 3400, '16.08.1985')
insert into personen values('Mertens', 'Julia', 2297, 3621.5, '30.12.1959')
insert into personen values('Schmitz', 'Peter', 8133, 3750, '12.04.1958')
insert into personen values('Müller', 'Hans', 9430, 3650, '22.08.1960')

drop table if exists person
create table person(
    id int primary key,
    vorname varchar(20),
    nachname varchar(20),
    schiff_id int)

insert into person values(1, 'James T.', 'Kirk', 1)
insert into person values(2, 'Willard', 'Decker', 1)
insert into person values(3, 'Jean-Luc', 'Picard', 2)
insert into person values(4, 'Han', 'Solo', 3)
insert into person values(5, 'Wilhuff', 'Tarkin', 4)
insert into person values(6, 'Mal', 'Reynolds', 5)

drop table if exists film
create table film(
    id int primary key,
    titel varchar(40),
    jahr int,
    budget int)

insert into film values(1, 'Star Trek', 1979, 46)
insert into film values(2, 'Star Trek: Generations', 1994, 35)
insert into film values(3, 'Star Wars 4', 1977, 11)
insert into film values(4, 'Star Wars 5', 1980, 33)
insert into film values(5, 'Serenity', 2005, 39)

drop table if exists schiff
create table schiff(
    id int primary key,
    name varchar(20))

insert into schiff values(1, 'USS Enterprise')
insert into schiff values(2, 'USS Enterprise')
insert into schiff values(3, 'Millennium Falcon')
insert into schiff values(4, 'Death Star')
insert into schiff values(5, 'Serenity')

drop table if exists personfilm
create table personfilm(
    id int primary key,
    person_id int,
    film_id int)

insert into personfilm values(1, 1, 1)
insert into personfilm values(2, 1, 2)
insert into personfilm values(3, 2, 1)
insert into personfilm values(4, 3, 2)
insert into personfilm values(5, 4, 3)
insert into personfilm values(6, 4, 4)
insert into personfilm values(7, 5, 3)
insert into personfilm values(8, 6, 5)

select * from person
select a.vorname, a.nachname, s.name as Schiff from person as a, schiff as s where a.schiff_id = s.id
