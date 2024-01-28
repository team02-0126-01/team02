use test;

create table tbl_users
(
    id       bigint auto_increment primary key,
    name     varchar(255) not null,
    username varchar(255) not null,
    email    varchar(255) not null,
    phone    varchar(255) not null,
    website  varchar(255) not null
);



create table tbl_address
(
    id      bigint auto_increment primary key,
    street  varchar(255) not null,
    suite   varchar(255) not null,
    city    varchar(255) not null,
    zipcode varchar(255) not null,
    user_id bigint       not null,
    constraint fk_address_users foreign key (user_id)
        references tbl_users (id) on delete cascade
);

create table tbl_geo
(
    id         bigint auto_increment primary key,
    lat        varchar(255) not null,
    lng        varchar(255) not null,
    address_id bigint       not null,
    constraint fk_geo_address foreign key (address_id)
        references tbl_address (id) on delete cascade
);

create table tbl_company
(
    id           bigint auto_increment primary key,
    name         varchar(255) not null,
    catch_phrase varchar(255) not null,
    bs           varchar(255) not null,
    user_id      bigint       not null,
    constraint fk_company_users foreign key (user_id)
        references tbl_users (id) on delete cascade
);

select *
from tbl_users;
select *
from tbl_address;
select *
from tbl_geo;
select *
from tbl_company;


insert into tbl_users (name, username, email, phone, website)
values ('Leanne Graham', 'Bret', 'Sincere@april.biz', '1-770-736-8031 x56442', 'hildegard.org'),
       ('Ervin Howell', 'Antonette', 'Shanna@melissa.tv', '010-692-6593 x09125', 'anastasia.net'),
       ('Clementine Bauch', 'Samantha', 'Nathan@yesenia.net', '1-463-123-4447', 'ramiro.info'),
       ('Patricia Lebsack', 'Karianne', 'Julianne.OConner@kory.org', '493-170-9623 x156', 'kale.biz'),
       ('Chelsey Dietrich', 'Kamren', 'Lucio_Hettinger@annie.ca', '(254)954-1289', 'demarco.info'),
       ('Mrs. Dennis Schulist', 'Leopoldo_Corkery', 'Karley_Dach@jasper.info', '1-477-935-8478 x6430', 'ola.org'),
       ('Kurtis Weissnat', 'Elwyn.Skiles', 'Telly.Hoeger@billy.biz', '210.067.6132', 'elvis.io'),
       ('Nicholas Runolfsdottir V', 'Maxime_Nienow', 'Sherwood@rosamond.me', '586.493.6943 x140', 'jacynthe.com'),
       ('Glenna Reichert', 'Delphine', 'Chaim_McDermott@dana.io', '(775)976-6794 x41206', 'conrad.com'),
       ('Clementina DuBuque', 'Moriah.Stanton', 'Rey.Padberg@karina.biz', '024-648-3804', 'ambrose.net');

insert into tbl_address (street, suite, city, zipcode, user_id)
values ('Kulas Light', 'Apt. 556', 'Gwenborough', '92998-3874', 1),
       ('Victor Plains', 'Suite 879', 'Wisokyburgh', '90566-7771', 2),
       ('Douglas Extension', 'Suite 847', 'McKenziehaven', '59590-4157', 3),
       ('Hoeger Mall', 'Apt. 692', 'South Elvis', '53919-4257', 4),
       ('Skiles Walks', 'Suite 351', 'Roscoeview', '33263', 5),
       ('Norberto Crossing', 'Apt. 950', 'South Christy', '23505-1337', 6),
       ('Rex Trail', 'Suite 280', 'Howemouth', '58804-1099', 7),
       ('Ellsworth Summit', 'Suite 729', 'Aliyaview', '45169', 8),
       ('Dayna Park', 'Suite 449', 'Bartholomebury', '76495-3109', 9),
       ('Kattie Turnpike', 'Suite 198', 'Lebsackbury', '31428-2261', 10);

insert into tbl_geo (lat, lng, address_id)
values ('-37.3159', '81.1496', 1),
       ('-43.9509', '-34.4618', 2),
       ('-68.6102', '-47.0653', 3),
       ('29.4572', '-164.2990', 4),
       ('-31.8129', '62.5342', 5),
       ('-71.4197', '71.7478', 6),
       ('24.8918', '21.8984', 7),
       ('-14.3990', '-120.7677', 8),
       ('24.6463', '-168.8889', 9),
       ('-38.2386', '57.2232', 10);

insert into tbl_company (name, catch_phrase, bs, user_id)
values ('Romaguera-Crona', 'Multi-layered client-server neural-net', 'harness real-time e-markets', 1),
       ('Deckow-Crist', 'Proactive didactic contingency', 'synergize scalable supply-chains', 2),
       ('Romaguera-Jacobson', 'Face to face bifurcated interface', 'e-enable strategic applications', 3),
       ('Robel-Corkery', 'Multi-tiered zero tolerance productivity', 'transition cutting-edge web services', 4),
       ('Keebler LLC', 'User-centric fault-tolerant solution', 'revolutionize end-to-end systems', 5),
       ('Considine-Lockman', 'Synchronised bottom-line interface', 'e-enable innovative applications', 6),
       ('Johns Group', 'Configurable multimedia task-force', 'generate enterprise e-tailers', 7),
       ('Abernathy Group', 'Implemented secondary concept', 'e-enable extensible e-tailers', 8),
       ('Yost and Sons', 'Switchable contextually-based project', 'aggregate real-time technologies', 9),
       ('Hoeger LLC', 'Centralized empowering task-force', 'target end-to-end models', 10);



drop table tbl_company;
drop table tbl_geo;
drop table tbl_address;
drop table tbl_users;








