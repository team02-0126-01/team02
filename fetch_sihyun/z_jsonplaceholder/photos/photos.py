from z_jsonplaceholder.module.crud_module import *

if __name__ == '__main__':
    ## create
    insert_by_query = "insert into tbl_photos (title, url, thumbnail_url, album_id) values (%s, %s, %s, %s)"
    insert_by_params = ('accusamus beatae ad facilis cum similique qui sunt',
                        'https://via.placeholder.com/600/92c952',
                        'https://via.placeholder.com/150/92c952'
                        , 1)
    # save(insert_by_query, insert_by_params)

    ## read all
    select_all_query = "select id, title, url, thumbnail_url, album_id from tbl_photos"
    photos = find_all(select_all_query)
    # print(photos)

    ## read
    select_by_id_query = "select id, title, url, thumbnail_url, album_id from tbl_photos where id = %s"
    select_by_id_params = 3,
    photo = find_by_id(select_by_id_query, select_by_id_params)
    # print(photo)

    ## update
    photo_id = 1
    update_by_id_query = "update tbl_photos set title=%s, url=%s, thumbnail_url=%s  where id = %s"
    update_by_id_params = ('수정된 제목', '수정된 경로', '수정된 썸네일 경로', photo_id)
    # update(update_by_id_query, update_by_id_params)

    ## delete
    photo_id = 1
    album_id = 1
    delete_by_id_query = "delete from tbl_photos where id = %s and album_id = %s"
    delete_by_id_params = (photo_id, album_id)
    delete(delete_by_id_query, delete_by_id_params)
