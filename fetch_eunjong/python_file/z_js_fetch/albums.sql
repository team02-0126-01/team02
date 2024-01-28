use test;

create table tbl_albums(
    userId bigint default 1,
    id bigint auto_increment primary key,
    title varchar(225)
);

select * from tbl_albums;

create table tbl_posts(
    userId bigint default 1,
    id bigint auto_increment primary key,
    title varchar(225),
    body varchar(225)
);

select * from tbl_posts;

create table tbl_comments(
    postid bigint default 1,
    id bigint auto_increment primary key,
    name varchar(225),
    email varchar(225),
    body varchar(225)
);

select * from tbl_comments;

create table tbl_photos(
    albumid bigint default 1,
    id bigint auto_increment primary key,
    title varchar(225),
    url varchar(225),
    thumbnailUrl varchar(225)
);

select * from tbl_photos;

create table tbl_todos(
    userid bigint default 1,
    id bigint auto_increment primary key,
    title varchar(225),
    completed bool
);

select * from tbl_todos;

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

