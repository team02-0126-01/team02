use test;

create table tbl_albums
(
    id      bigint auto_increment primary key,
    title   varchar(255) not null,
    user_id bigint       not null,
    constraint fk_comments_users foreign key (user_id)
        references tbl_users (id)
);
select *
from tbl_albums;


insert into tbl_albums(title, user_id)
values ('quidem molestiae enim', 1),
       ('sunt qui excepturi placeat culpa', 2),
       ('omnis laborum odio', 3),
       ('non esse culpa molestiae omnis sed optio', 4),
       ('eaque aut omnis a', 5),
       ('natus impedit quibusdam illo est', 6),
       ('quibusdam autem aliquid et et quia', 7),
       ('qui fuga est a eum', 8),
       ('saepe unde necessitatibus rem', 9),
       ('distinctio laborum qui', 10);
