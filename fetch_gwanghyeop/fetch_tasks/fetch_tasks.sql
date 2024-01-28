# posts 테이블
create table tbl_posts(
    id bigint auto_increment primary key,
    userid bigint not null,
    title varchar(255) not null,
    body varchar(2550) not null
);

# comments 테이블
create table tbl_comments(
    id bigint auto_increment primary key,
    userid bigint not null,
    name varchar(255) not null,
    email varchar(255) not null,
    body varchar(2550) not null
);

# albums 테이블
create table tbl_albums(
    id bigint auto_increment primary key,
    userid bigint not null,
    title varchar(255) not null
);

# photos 테이블
create table tbl_photos(
    id bigint auto_increment primary key,
    userid bigint not null,
    name varchar(255) not null,
    url varchar(255) not null,
    thumbnail_url varchar(255) not null
);

# todos 테이블
create table tbl_todos(
    id bigint auto_increment primary key,
    userid bigint not null,
    title varchar(255) not null,
    completed boolean not null
);

# users 테이블
create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255) not null,
    website varchar(255) not null
);

# address 클래스
create table tbl_address(
    id bigint auto_increment primary key,
    street varchar(255) not null,
    suite varchar(255) not null,
    city varchar(255) not null,
    zipcode varchar(255) not null,
    website varchar(255) not null,
    constraint fk_address_user foreign key (id)
                      references tbl_users(id)
);

# geo 클래스
create table tbl_geo(
    id bigint auto_increment primary key,
    lat varchar(255) not null,
    lng varchar(255) not null,
    constraint fk_geo_address foreign key (id)
                      references tbl_address(id)
);

# company 클래스
create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    catch_phrase varchar(255) not null,
    bs varchar(255) not null,
    constraint fk_company_user foreign key (id)
                      references tbl_users(id)
);

use test;