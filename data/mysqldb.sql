create database falcr;
use falcr;
create table quotes(
    id int not null auto_increment,
    author varchar(100) not null,
    quote text,
    primary key(id)
);
create table appusers(
    id int not null auto_increment,
    email varchar(256) not null,
    password varchar(256) not null,
    primary key(id)
);
