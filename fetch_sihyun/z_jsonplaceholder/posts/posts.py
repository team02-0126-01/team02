from z_jsonplaceholder.module.crud_module import *

if __name__ == '__main__':
    ## create
    insert_by_query = "insert into tbl_posts (title, body, user_id) values (%s, %s, %s)"
    insert_by_params = ('sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
                        'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto',
                        1)
    save(insert_by_query, insert_by_params)

    ## read all
    select_all_query = "select id, title, body, user_id from tbl_posts"
    posts = find_all(select_all_query)
    # print(posts)

    ## read
    select_by_id_query = "select id, title, body, user_id from tbl_posts where id = %s"
    select_by_id_params = 1,
    post = find_by_id(select_by_id_query, select_by_id_params)
    # print(post)

    ## update
    post_id = 1
    update_by_id_query = "update tbl_posts set title=%s, body=%s where id = %s"
    update_by_id_params = ('수정된 제목', '수정된 내용', post_id)
    # update(update_by_id_query, update_by_id_params)

    ## delete
    post_id = 1
    user_id = 1
    delete_by_id_query = "delete from tbl_posts where id = %s and user_id = %s"
    delete_by_id_params = (post_id, user_id)
    # delete(delete_by_id_query, delete_by_id_params)
