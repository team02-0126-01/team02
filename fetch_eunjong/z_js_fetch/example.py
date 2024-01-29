from crud_module import *
from albums import Albums
from posts import Posts
from comments import Comments
from photos import Photos
from todos import Todos
from users import Users


if __name__ == '__main__':
    # 값 추가
    # insert_query = "insert into tbl_albums(userId, title) values (%s, %s)"
    # # insert_params = [1, "quidem molestiae enim"]
    # insert_params = (
    #     (1, "quidem molestiae enim"),
    #     (1, "sunt qui excepturi placeat culpa"),
    #     (1, "omnis laborum odio"),
    #     (1, "non esse culpa molestiae omnis sed optio"),
    #     (1, "eaque aut omnis a")
    # )
    # save_many(insert_query, insert_params)

    # insert_query = "insert into tbl_posts(title, body) values (%s, %s)"
    # insert_params = (
    #     ("sunt aut facere repellat provident occaecati", "quidem molestiae"),
    #     ("qui est esse", "quidem molestiae"),
    #     ("eum et est occaecati", "quidem molestiae"),
    #     ("nesciunt quas odio", "quidem molestiae"),
    #     ("magnam facilis autem", "quidem molestiae")
    # )
    # save_many(insert_query, insert_params)

    # insert_query = "insert into tbl_comments(name, email, body) values (%s, %s, %s)"
    # insert_params = (
    #     ("id labore ex et quam laborum", "Eliseo@gardner.biz", "laudantium enim quasi est quidem magnam voluptate ipsam eos"),
    #     ("quo vero reiciendis velit similique earum", "Jayne_Kuhic@sydney.com",
    #      "est natus enim nihil est dolore omnis voluptatem numquam"),
    #     ("odio adipisci rerum aut animi", "Nikita@garfield.biz",
    #      "quia molestiae reprehenderit quasi aspernatur")
    # )
    # save_many(insert_query, insert_params)

    # insert_query = "insert into tbl_photos(title, url, thumbnailUrl) values (%s, %s, %s)"
    # insert_params = (
    #     ("accusamus beatae ad facilis cum similique qui sunt", "https://via.placeholder.com/600/92c952", "https://via.placeholder.com/150/92c952"),
    #     ("reprehenderit est deserunt velit ipsam", "https://via.placeholder.com/600/771796",
    #      "https://via.placeholder.com/150/771796"),
    #     ("officia porro iure quia iusto qui ipsa ut modi", "https://via.placeholder.com/600/24f355",
    #      "https://via.placeholder.com/150/24f355")
    # )
    # save_many(insert_query, insert_params)

    # insert_query = "insert into tbl_todos(title, completed) values (%s, %s)"
    # insert_params = (
    #     ("delectus aut autem", False),
    #     ("quis ut nam facilis et officia qu", False),
    #     ("fugiat veniam minus", False)
    # )
    # save_many(insert_query, insert_params)

    insert_by_query = "insert into tbl_photos(albumId, id, title, url, thumbnailUrl) values (%s, %s, %s, %s, %s) "
    insert_by_params = tuple(Photos(albumId=1, id=1, title='accusamus beatae ad facilis cum similique qui sunt', url='https://via.placeholder.com/600/92c952', thumbnailUrl='https://via.placeholder.com/150/92c952').__dict__.values())
    # save(insert_by_query, insert_by_params)

    print(insert_by_params)

    insert_by_query = "insert into tbl_users(id, name, username, email, phone, website) values (%s, %s, %s, %s, %s, %s)"
    insert_by_params = tuple(Users(id =1, name="", rname="sunsin", email="<EMAIL>", phone="010-1234-5687", website="https://via.placeholder.com").__dict__.values())
    # save(insert_by_query, insert_by_params)

    insert_by_query = "insert into tbl_posts(title, body) values (%s, %s)"
    insert_by_params = tuple(Posts(title="sunt aut facere repellat provident occaecati", boby="quidem molestiae").__dict__.values())
    # save(insert_by_query, insert_by_params)
