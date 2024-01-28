use test;


create table tbl_posts(
    id bigint auto_increment primary key,
    user_id bigint not null,
    title varchar(255) not null,
    body varchar(255) not null,
    constraint fk_post_user foreign key(user_id)
    references tbl_users(id) on delete cascade
);

create table tbl_comments(
    id bigint auto_increment primary key,
    post_id bigint not null,
    name varchar(255) not null,
    email varchar(255) not null,
    body varchar(255) not null,
    constraint fk_comment_post foreign key(post_id)
    references tbl_posts(id) on delete cascade
);

create table tbl_albums(
    id bigint auto_increment primary key,
    user_id bigint not null,
    title varchar(255) not null,
    constraint fk_album_user foreign key (user_id)
    references tbl_users(id) on delete cascade
);

create table tbl_photos(
    id bigint auto_increment primary key,
    album_id bigint not null,
    title varchar(255) not null,
    url varchar(255) not null,
    thumbnail_url varchar(255) not null,
    constraint fk_photo_album foreign key (album_id)
    references tbl_albums(id) on delete cascade
);

create table tbl_todos(
    id bigint auto_increment primary key,
    user_id bigint not null,
    title varchar(255) not null,
    conpleted bool not null,
    constraint fk_todo_user foreign key (user_id)
    references tbl_users(id) on delete cascade
);

create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    email varchar(255) not null,
    address varchar(255) not null,
    phone varchar(255) not null,
    website varchar(255) not null,
    company bigint not null,
    constraint fk_users_address foreign key (address)
    references tbl_addresses(zipcode) on delete cascade
);

alter table tbl_users add constraint fk_user_company foreign key(company) references tbl_company(id) on delete cascade;

create table tbl_company(
    id bigint primary key auto_increment,
    name varchar(255) not null,
    catch_phrase varchar(255) not null,
    bs varchar(255) not null
);
create table tbl_addresses(
    zipcode varchar(255) primary key,
    street varchar(255) not null,
    suite varchar(255) not null,
    city varchar(255) not null,
    geo bigint not null,
    constraint fk_adresses_geo foreign key(geo)
    references tbl_geo(id) on delete cascade
);

create table tbl_geo(
    id bigint auto_increment primary key,
    lat varchar(255) not null,
    lng varchar(255) not null
);

alter table tbl_users add column username varchar(255) not null after name;

select * from  tbl_albums;
select * from  tbl_users;
select * from  tbl_posts;
select * from  tbl_addresses;
select * from tbl_comments;
select * from tbl_photos;
select * from tbl_todos;