from z_jsonplaceholder.module.crud_module import *

if __name__ == '__main__':
    ## create
    insert_by_query = "insert into tbl_albums (title, user_id) values (%s, %s)"
    insert_by_params = ('quidem molestiae enim',
                        1)
    # save(insert_by_query, insert_by_params)

    ## read all
    select_all_query = "select id, title, user_id from tbl_albums"
    albums = find_all(select_all_query)
    # print(albums)

    ## read
    select_by_id_query = "select id, title, user_id from tbl_albums where id = %s"
    select_by_id_params = 1,
    album = find_by_id(select_by_id_query, select_by_id_params)
    # print(album)

    ## update
    album_id = 1
    user_id = 1
    update_by_id_query = "update tbl_albums set title=%s where id = %s and user_id = %s"
    update_by_id_params = ('수정된 제목', album_id, user_id)
    # update(update_by_id_query, update_by_id_params)

    ## delete
    album_id = 1
    user_id = 1
    delete_by_id_query = "delete from tbl_albums where id = %s and user_id = %s"
    delete_by_id_params = (album_id, user_id)
    delete(delete_by_id_query, delete_by_id_params)
