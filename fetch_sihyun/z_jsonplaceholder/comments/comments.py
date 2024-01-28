from z_jsonplaceholder.comments.comments_class import CommentsInfo
from z_jsonplaceholder.module.crud_module import *

if __name__ == '__main__':
    ## create
    insert_by_query = "insert into tbl_comments (name, email, body, post_id) values (%s, %s, %s, %s)"
    insert_by_params = tuple(CommentsInfo(name='id labore ex et quam laborum',
                                          email='Eliseo@gardner.biz',
                                          body='laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'
                                          , post_id=2).__dict__.values())
    # save(insert_by_query, insert_by_params)

    ## read all
    select_all_query = "select id, name, email, body, post_id from tbl_comments"
    comments = find_all(select_all_query)
    # print(comments)

    ## read
    select_by_id_query = "select id, name, email, body, post_id from tbl_comments where id = %s"
    select_by_id_params = 3,
    comment = find_by_id(select_by_id_query, select_by_id_params)
    # print(comment)

    ## update
    comment_id = 3
    update_by_id_query = "update tbl_comments set name=%s, email=%s, body=%s where id = %s"
    update_by_id_params = ('수정된 이름', '수정된 이메일', '수정된 내용', comment_id)
    # update(update_by_id_query, update_by_id_params)

    ## delete
    comment_id = 3
    post_id = 2
    delete_by_id_query = "delete from tbl_comments where id = %s and post_id = %s"
    delete_by_id_params = (comment_id, post_id)
    delete(delete_by_id_query, delete_by_id_params)
