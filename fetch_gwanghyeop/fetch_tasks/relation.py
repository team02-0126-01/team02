# CRUD 모듈 import
from crud_module import *

# CRUD 할 클래스 객체 import
from posts import Posts
from comments import Comments
from albums import Albums
from photos import Photos
from todos import Todos
from users import Users
from address import Address
from geo import Geo
from company import Company

if __name__ == '__main__':
    # posts에 save_many 실행
    # save_many_query = "insert into tbl_posts (userid, title, body) \
    #               values (%s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "sunt aut facere repellat", "quia et suscipit"),
    #     (1, "qui est esse", "est rerum tempore vitae"),
    #     (1, "ea molestias quasi", "et iusto sed quo iure"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # comments 에 save_many 실행 후, 특정 post_id를 가진 데이터 조회
    # save_many_query = "insert into tbl_comments (post_id, name, email, body) \
    #                   values (%s, %s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "id labore ex", "Eliseo@gardner.biz", "laudantium enim quasi est"),
    #     (2, "et fugit eligendi", "Presley.Mueller@myrl.com", "doloribus at sed quis"),
    #     (3, "fugit labore quia", "Veronica_Goodwin@timmothy.net", "ut dolorum nostrum"),
    # )
    #
    # save_many(save_many_query, save_many_params)
    
    # # 특정 post_id를 가진 데이터 조회
    # find_all_by_query = "select * from tbl_users where id = %s"
    # find_all_by_params = 2
    #
    # result = find_all_by(find_all_by_query, find_all_by_params)
    #
    # print(result)

    # tbl_albums 에 save_many 실행 하고 특정 userid 를 가진 데이터 update 해보기
    # save_many_query = "insert into tbl_albums (userid, title) \
    #               values (%s, %s)"
    #
    # save_many_params = (
    #   (1, "distinctio laborum qui"),
    #   (2, "quam nostrum impedit mollitia quod et dolor"),
    #   (3, "et rem non provident vel ut"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 특정 userid를 가진 데이터의 title에 update 실행
    # new_content = input("원하는 내용을 입력해주세요: ")
    # new_id = int(input("원하는 번호를 입력해주세요: "))
    #
    # update_query = "update tbl_albums set title = %s \
    #                 where userid = %s"
    #
    # update_params = (new_content, new_id)
    #
    # update(update_query, update_params)

    # photos 테이블에서 특정 요소 delete 실행
    # save_many_query = "insert into tbl_photos (album_id, title, url, thumbnail_url) \
    #                    values (%s, %s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "사진 1", "주소 1", "https://via.placeholder.com/600/92c952"),
    #     (2, "사진 2", "주소 2", "https://via.placeholder.com/600/771796"),
    #     (3, "사진 3", "주소 3", "https://via.placeholder.com/600/56a8c2"),
    #     (4, "사진 4", "주소 4", "https://via.placeholder.com/600/66b7d2"),
    #     (5, "사진 5", "주소 5", "https://via.placeholder.com/600/fdf73e"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 입력값보다 큰 album_id를 가진 요소 삭제
    # delete_input = int(input("입력값보다 더 큰 album_id를 가진 요소가 삭제됩니다: "))
    #
    # delete_query = "delete from tbl_photos where album_id > %s"
    # delete_params = delete_input
    #
    # delete(delete_query, delete_params)

    # todos 테이블에서 completed가 true 인 요소만 조회
    # save_many_query = "insert into tbl_todos (userid, title, completed) \
    #                    values (%s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "제목 1", True),
    #     (2, "제목 2", False),
    #     (3, "제목 3", False),
    #     (4, "제목 4", True),
    #     (5, "제목 5", True),
    #     (6, "제목 6", False),
    #     (7, "제목 7", True),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # completed가 true인 모든 요소의 전체 내용 조회
    find_all_by_query = "select * from tbl_todos where completed = %s"

    # completed가 true = 1 (bool 타입이라 그런 듯...)
    find_all_by_params = 1

    # 결과값을 변수에 저장
    todo_lists = find_all_by(find_all_by_query, find_all_by_params)
    
    # 각 줄에 출력
    for todos in todo_lists:
        print(todos)