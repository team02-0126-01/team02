use test;

create table tbl_todos
(
    id        bigint auto_increment primary key,
    title     varchar(255) not null,
    completed varchar(255) not null default 'false',
    user_id   bigint       not null,
    constraint check_todos_completed check ( completed in ('false', 'true') ),
    constraint fk_todos_users foreign key (user_id)
        references tbl_users (id)
);
select *
from tbl_todos;

insert into tbl_todos(title, completed, user_id)
values ('delectus aut autem', 'false', 1),
       ('quis ut nam facilis et officia qui', 'false', 2),
       ('fugiat veniam minus', 'false', 3),
       ('et porro tempora', 'true', 4),
       ('laboriosam mollitia et enim quasi adipisci quia provident illum', 'false', 5),
       ('qui ullam ratione quibusdam voluptatem quia omnis', 'false', 6),
       ('illo expedita consequatur quia in', 'false', 7),
       ('quo adipisci enim quam ut ab', 'true', 8),
       ('molestiae perspiciatis ipsa', 'false', 9),
       ('illo est ratione doloremque quia maiores aut', 'true', 10);