use test;

create table tbl_photos
(
    id            bigint auto_increment primary key,
    title         varchar(255) not null,
    url           varchar(255) not null,
    thumbnail_url varchar(255) not null,
    album_id      bigint       not null,
    constraint fk_photos_album foreign key (album_id)
        references tbl_albums (id)
);
select *
from tbl_photos;

insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('accusamus beatae ad facilis cum similique qui sunt', 'https://via.placeholder.com/600/92c952',
        'https://via.placeholder.com/150/92c952', 1),
       ('reprehenderit est deserunt velit ipsam', 'https://via.placeholder.com/600/771796',
        'https://via.placeholder.com/150/771796', 2),
       ('officia porro iure quia iusto qui ipsa ut modi', 'https://via.placeholder.com/600/24f355',
        'https://via.placeholder.com/150/24f355', 3),
       ('culpa odio esse rerum omnis laboriosam voluptate repudiandae', 'https://via.placeholder.com/600/d32776',
        'https://via.placeholder.com/150/d32776', 4),
       ('natus nisi omnis corporis facere molestiae rerum in', 'https://via.placeholder.com/600/f66b97',
        'https://via.placeholder.com/150/f66b97', 5),
       ('accusamus ea aliquid et amet sequi nemo', 'https://via.placeholder.com/600/56a8c2',
        'https://via.placeholder.com/150/56a8c2', 6),
       ('officia delectus consequatur vero aut veniam explicabo molestias', 'https://via.placeholder.com/600/b0f7cc',
        'https://via.placeholder.com/150/b0f7cc', 7),
       ('aut porro officiis laborum odit ea laudantium corporis', 'https://via.placeholder.com/600/54176f',
        'https://via.placeholder.com/150/54176f', 8),
       ('qui eius qui autem sed', 'https://via.placeholder.com/600/51aa97', 'https://via.placeholder.com/150/51aa97',
        9),
       ('beatae et provident et ut vel', 'https://via.placeholder.com/600/810b14',
        'https://via.placeholder.com/150/810b14', 10);
