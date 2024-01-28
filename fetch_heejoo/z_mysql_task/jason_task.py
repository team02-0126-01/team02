from crud_module import *
from posts import *
if __name__ == '__main__':

    # save_many_query = "insert into tbl_geo(lat, lng) values(%s,%s)"
    # save_many_params = (('-37.3159','81.1496'),('-43.9509','-34.4618'),("-68.6102","-47.0653"),("29.4572","-164.2990"),("-31.8129","62.5342"))
    #
    # save_many(save_many_query, save_many_params)
    #
    # find_by_id_query = "select id,lat,lng from tbl_geo where id = %s"
    # find_by_id_params = 1
    # find_by_id_params = 2
    # find_by_id_params = 3
    # find_by_id_params = 4
    # find_by_id_params = 5
    # geo = find_by_id(find_by_id_query, find_by_id_params)
    # geo_id = geo.get("id")
    # print(geo_id)
    # save_many_query = "insert into tbl_addresses(zipcode, street, suite, city, geo) values(%s,%s,%s,%s,%s)"
    # save_many_params = (
        # ("92998-3874","Kulas Light","Apt. 556","Gwenborough",geo_id)
        # ("90566-7771","Victor Plains","Suite 879","Wisokyburgh",geo_id)
        # ("59590-4157","Douglas Extension","Suite 847","McKenziehaven",geo_id)
        # ("53919-4257","Hoeger Mall","Apt. 692","South Elvis",geo_id)
        # ( "33263","Skiles Walks", "Suite 351","Roscoeview",geo_id)
    # )
    # save(save_many_query, save_many_params)
    #

    # save_many_query = "insert into tbl_company(name, catch_phrase, bs) values (%s, %s, %s)"
    # save_many_params = (
    #     # ("Romaguera-Crona","Multi-layered client-server neural-net","harness real-time e-markets")
    #     ("Deckow-Crist","Proactive didactic contingency","synergize scalable supply-chains"),
    #     ("Romaguera-Jacobson","Face to face bifurcated interface","e-enable strategic applications"),
    #     ("Robel-Corkery","Multi-tiered zero tolerance productivity","transition cutting-edge web services"),
    #     ("Keebler LLC","User-centric fault-tolerant solution" ,"revolutionize end-to-end systems")
    #     )
    # save_many(save_many_query, save_many_params)
    # find_by_id_query = "select zipcode, street, suite, city, geo from tbl_addresses where zipcode = %s"
    # find_by_id_params = "92998-3874"
    # find_by_id_params = "90566-7771"
    # find_by_id_params = "59590-4157"
    # find_by_id_params = "53919-4257"
    # find_by_id_params = "33263"
    # address = find_by_id(find_by_id_query, find_by_id_params)
    # zipcode = address.get("zipcode")

    # find_by_id_query = "select id, name, catch_phrase, bs from tbl_company where id = %s"
    # find_by_id_params = 1
    # find_by_id_params = 2
    # find_by_id_params = 3
    # find_by_id_params = 4
    # find_by_id_params = 5
    # company = find_by_id(find_by_id_query, find_by_id_params)
    # company_id = company.get("id")
    # save_many_query = "insert into tbl_users(name, username,email, address,phone, website, company) \
    #                            values(%s, %s, %s, %s, %s, %s,%s)"
    # save_many_params = (
        # ("Leanne Graham","Bret","Sincere@april.biz",zipcode,"1-770-736-8031 x56442","hildegard.org",company_id)
        # ("Ervin Howell","Antonette","Shanna@melissa.tv",zipcode,"010-692-6593 x09125","anastasia.net",company_id)
        # ("Clementine Bauch", "Samantha","Nathan@yesenia.net",zipcode,"1-463-123-4447","ramiro.info",company_id)
        # ("Patricia Lebsack","Karianne","Julianne.OConner@kory.org",zipcode, "493-170-9623 x156", "kale.biz",company_id)
        # ("Chelsey Dietrich","Kamren","Lucio_Hettinger@annie.ca",zipcode,"(254)954-1289", "demarco.info",company_id)
    # )
    # save(save_many_query, save_many_params)
    #
    # find_by_id_query = "select id, name, username, email, address, phone, website, company from tbl_users where id = %s"
    # find_by_id_params = 1
    # user = find_by_id(find_by_id_query, find_by_id_params)
    # user_id = user.get("id")
    #
    # save_many_query = "insert into tbl_posts(user_id, title, body) \
    #                    values(%s,%s,%s)"
    # save_many_params = (
    #     (user_id,'sunt aut facere repellat provident occaecati excepturi optio reprehenderit','quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
    #     (user_id,'qui est esse','est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'),
    #     (user_id,"ea molestias quasi exercitationem repellat qui ipsa sit aut","et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"),
    #     (user_id,"eum et est occaecati","ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"),
    #     (user_id,"nesciunt quas odio", "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque")
    # )
    # save_many(save_many_query,save_many_params)

    find_by_id_query = "select id, user_id, title, body from tbl_posts where id = %s"
    find_by_id_params = 1
    post= find_by_id(find_by_id_query, find_by_id_params)
    post_id = post.get("id")
    # save_many_query = "insert into tbl_comments(post_id, name, email, body) values (%s,%s,%s,%s)"
    # save_many_params = ((post_id,"id labore ex et quam laborum","Eliseo@gardner.biz","laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"),
    #                     (post_id,"quo vero reiciendis velit similique earum","Jayne_Kuhic@sydney.com","est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"),
    #                     (post_id,"odio adipisci rerum aut animi","Nikita@garfield.biz", "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"))
    # save_many(save_many_query, save_many_params)
    #
    # find_by_id_query = "select id, name, username, email, address, phone, website, company from tbl_users where id = %s"
    # find_by_id_params = 1
    # user = find_by_id(find_by_id_query, find_by_id_params)
    # user_id = user.get("id")
    # save_many_query = "insert into tbl_albums(user_id, title) values(%s,%s)"
    # save_many_params = (
    #     (user_id,"quidem molestiae enim"),
    #     (user_id,"sunt qui excepturi placeat culpa"),
    #     (user_id, "omnis laborum odio"),
    #     (user_id,"non esse culpa molestiae omnis sed optio")
    # )
    # save_many(save_many_query, save_many_params)

    # find_by_id_query = "select id, user_id, title from tbl_albums where id = %s"
    # find_by_id_params = 1
    # album= find_by_id(find_by_id_query, find_by_id_params)
    # album_id = album.get("id")
    #
    # save_many_query = "insert into tbl_photos(album_id, title, url, thumbnail_url) values(%s,%s,%s,%s)"
    # save_many_params = (
    #     (album_id,"accusamus beatae ad facilis cum similique qui sunt","https://via.placeholder.com/600/92c952","https://via.placeholder.com/150/92c952"),
    #     (album_id, "reprehenderit est deserunt velit ipsam","https://via.placeholder.com/600/771796","https://via.placeholder.com/150/771796"),
    #     (album_id,"officia porro iure quia iusto qui ipsa ut modi","https://via.placeholder.com/600/24f355","https://via.placeholder.com/150/24f355"),
    #     (album_id,"culpa odio esse rerum omnis laboriosam voluptate repudiandae","https://via.placeholder.com/600/d32776","https://via.placeholder.com/150/d32776"))
    # save_many(save_many_query, save_many_params)
    #
    # find_by_id_query = "select id, name, username, email, address, phone, website, company from tbl_users where id = %s"
    # find_by_id_params = 1
    # user = find_by_id(find_by_id_query, find_by_id_params)
    # user_id = user.get("id")
    #
    # save_many_query = "insert into tbl_todos(user_id, title, conpleted) values(%s,%s,%s)"
    # save_many_params =(
    #     (user_id, "delectus aut autem", False),
    #     (user_id,"quis ut nam facilis et officia qui",False),
    #     (user_id, "et porro tempora",True)
    # )
    # save_many(save_many_query, save_many_params)



    # 게시글 보기
    # find_all_query = "select p.id, title, body, u.username\
    #                   from tbl_users u join tbl_posts p\
    #                   on u.id = p.user_id\
    #                   order by id desc"
    # posts = find_all(find_all_query)
    # for post in posts:
    #     print(post)
    #
    # togo 목록 보기
    # find_all_by_query = "select title,conpleted from tbl_todos t join tbl_users u \
    #                     on t.user_id = u.id and u.id = %s order by t.id desc"
    # find_all_by_params = 1
    # todos = find_all_by(find_all_by_query,find_all_by_params)
    # for todo in todos:
    #     print(todo)

    # 게시글과 댓글 내용 보기
    find_by_id_query = "select p.id, title, body, u.name \
                        from tbl_users u join tbl_posts p \
                        on u.id = p.user_id\
                        where p.id = %s"
    find_by_id_params = post_id
    post = find_by_id(find_by_id_query, find_by_id_params)
    find_all_by_query = "select p.id, p.title, p.body, c.name, c.body\
                       from tbl_posts p join tbl_comments c\
                       on c.post_id = %s and p.id = c.post_id"
    find_all_by_params = post.get("id"),
    comments = find_all_by(find_all_by_query, find_all_by_params)

    post = Posts(post.get("id"), post.get("title"), post.get("content"), comments)
    print(post.__dict__)