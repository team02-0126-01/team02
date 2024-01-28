from z_jsonplaceholder.module.crud_module import *
from z_jsonplaceholder.todos.todos_class import TodosInfo

if __name__ == '__main__':
    ## create
    insert_by_query = "insert into tbl_todos (title, completed, user_id) values (%s, %s, %s)"
    insert_by_params = tuple(TodosInfo(title='delectus aut autem',
                                       completed='false',
                                       user_id=1).__dict__.values())
    save(insert_by_query, insert_by_params)

    ## read all
    select_all_query = "select id, title, completed, user_id from tbl_todos"
    todos = find_all(select_all_query)
    # print(todos)

    ## read
    select_by_id_query = "select id, title, completed, user_id from tbl_todos where id = %s"
    select_by_id_params = 1,
    todo = find_by_id(select_by_id_query, select_by_id_params)
    # print(todo)

    ## update
    user_id = 1
    update_by_id_query = "update tbl_todos set title=%s, completed=%s, user_id=%s where id = %s"
    update_by_id_params = ('수정된 제목', 'true', user_id)
    # update(update_by_id_query, update_by_id_params)

    ## delete
    todo_id = 1
    user_id = 1
    delete_by_id_query = "delete from tbl_todos where id = %s and user_id = %s"
    delete_by_id_params = (todo_id, user_id)
    # delete(delete_by_id_query, delete_by_id_params)
