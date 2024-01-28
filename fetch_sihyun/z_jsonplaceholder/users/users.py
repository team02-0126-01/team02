from z_jsonplaceholder.module.crud_module import *
from z_jsonplaceholder.users.relation.address_info import AddressInfo
from z_jsonplaceholder.users.relation.company_info import CompanyInfo
from z_jsonplaceholder.users.relation.user_info import UserInfo
from z_jsonplaceholder.users.relation.geo_info import GeoInfo
from z_jsonplaceholder.users.users_class.address_class import Address
from z_jsonplaceholder.users.users_class.company_class import Company
from z_jsonplaceholder.users.users_class.geo_class import Geo
from z_jsonplaceholder.users.users_class.users_class import Users

if __name__ == '__main__':
    # create_tbl_users = "create table tbl_users\
    #                 (\
    #                     id       bigint auto_increment primary key,\
    #                     name     varchar(255) not null,\
    #                     username varchar(255) not null,\
    #                     email    varchar(255) not null,\
    #                     phone    varchar(255) not null,\
    #                     website  varchar(255) not null\
    #                 );"
    # Users.create_table(create_tbl_users)

    # insert_query = ("insert into tbl_users(name, username, email, phone, \
    #                 website) values (%s, %s, %s, %s, %s)")
    # user_data = {"name": "Ervin Howell", "username": "Antonette", "email": "Shanna@melissa.tv",
    #              "phone": "010-692-6593 x09125", "website": "anastasia.net"}
    # users_object = Users(**user_data).__dict__
    # insert_params = tuple(users_object.values())
    # save(insert_query, insert_params)

    # create_tbl_address = "create table tbl_address\
    #                     (\
    #                         id      bigint auto_increment primary key,\
    #                         street  varchar(255) not null,\
    #                         suite   varchar(255) not null,\
    #                         city    varchar(255) not null,\
    #                         zipcode varchar(255) not null,\
    #                         user_id bigint       not null,\
    #                         constraint fk_address_users foreign key (user_id)\
    #                             references tbl_users (id) on delete cascade\
    #                     );"
    # Address.create_table(create_tbl_address)

    # insert_query = ("insert into tbl_address(street, suite, city, zipcode, \
    #                 user_id) values (%s, %s, %s, %s, %s)")
    # address_data = {"street": "Victor Plains", "suite": "Suite 879", "city": "Wisokyburgh",
    #                 "zipcode": "90566-7771", "user_id": 2}
    # address_object = Address(**address_data).__dict__
    # insert_params = tuple(address_object.values())
    # save(insert_query, insert_params)

    # create_tbl_geo = "create table tbl_geo\
    #                 (\
    #                     id         bigint auto_increment primary key,\
    #                     lat        varchar(255) not null,\
    #                     lng        varchar(255) not null,\
    #                     address_id bigint       not null,\
    #                     constraint fk_geo_address foreign key (address_id)\
    #                         references tbl_address (id) on delete cascade\
    #                 );"
    # Geo.create_table(create_tbl_geo)

    # insert_query = "insert into tbl_geo(lat, lng, address_id) values (%s, %s, %s)"
    # geo_data = {"lat": "-43.9509", "lng": "-34.4618", "address_id": 3}
    #
    # geo_object = Geo(**geo_data).__dict__
    # insert_params = tuple(geo_object.values())
    # save(insert_query, insert_params)

    # create_tbl_company = "create table tbl_company\
    #                     (\
    #                         id           bigint auto_increment primary key,\
    #                         name         varchar(255) not null,\
    #                         catch_phrase varchar(255) not null,\
    #                         bs           varchar(255) not null,\
    #                         user_id      bigint       not null,\
    #                         constraint fk_company_users foreign key (user_id)\
    #                             references tbl_users (id) on delete cascade\
    #                     );"
    # Company.create_table(create_tbl_company)

    # insert_query = "insert into tbl_company(name, catch_phrase, bs, user_id) values (%s, %s, %s, %s)"
    # company_data = {"name": "Deckow-Crist", "catch_phrase": "Proactive didactic contingency",
    #                 "bs": "synergize scalable supply-chains", "user_id": 2}
    #
    # company_object = Company(**company_data).__dict__
    # insert_params = tuple(company_object.values())
    # save(insert_query, insert_params)

    ## create
    user_update_data = {'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz',
                        'address':
                            {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough',
                             'zipcode': '92998-3874',
                             'geo': {'lat': '-37.3159', 'lng': '81.1496'}
                             },
                        'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org',
                        'company':
                            {'name': 'Romaguera-Crona',
                             'catch_phrase': 'Multi-layered client-server neural-net',
                             'bs': 'harness real-time e-markets'}
                        }
    insert_by_query = "insert into tbl_users (name, username, email, phone, website) values (%s, %s, %s, %s, %s)"
    insert_by_params = (user_update_data.get('name'), user_update_data.get('username'), user_update_data.get('email'),
                        user_update_data.get('phone'), user_update_data.get('website'))
    # save(insert_by_query, insert_by_params)

    select_by_id_query = "select id from tbl_users order by id desc limit 1"
    user_id = find_one(select_by_id_query).get('id')
    insert_by_query = "insert into tbl_address (street, suite, city, zipcode, user_id) values (%s, %s, %s, %s, %s)"
    address_update_data = user_update_data.get('address')
    insert_by_params = (
        address_update_data.get('street'), address_update_data.get('suite'), address_update_data.get('city'),
        address_update_data.get('zipcode'), user_id)
    # save(insert_by_query, insert_by_params)

    select_by_id_query = "select id from tbl_address order by id desc limit 1"
    address_id = find_one(select_by_id_query).get('id')
    insert_by_query = "insert into tbl_geo (lat, lng, address_id) values (%s, %s, %s)"
    geo_update_data = address_update_data.get('geo')
    insert_by_params = (
        geo_update_data.get('lat'), geo_update_data.get('lng'), address_id)
    # save(insert_by_query, insert_by_params)

    insert_by_query = "insert into tbl_company (name, catch_phrase, bs, user_id) values (%s, %s, %s, %s)"
    company_update_data = user_update_data.get('company')
    insert_by_params = (
        company_update_data.get('name'), company_update_data.get('catch_phrase'), company_update_data.get('bs'),
        user_id)
    # save(insert_by_query, insert_by_params)

    ## read all
    # select_query = "select lat, lng, address_id from tbl_geo"
    # geos = find_all(select_query)
    # user_list = []
    # for geo in geos:
    #     find_all_by_id_query = "select street, suite, city, zipcode, user_id from tbl_address where id = %s"
    #     find_all_by_params = geo.get("address_id")
    #     addresses = find_by_all(find_all_by_id_query, find_all_by_params)
    #
    #     for address in addresses:
    #         find_all_by_id_query = "select id, name, username, email, phone, website from tbl_users where id = %s"
    #         find_all_by_params = address.get("user_id")
    #         users = find_by_all(find_all_by_id_query, find_all_by_params)
    #
    #         for user in users:
    #             find_all_by_id_query = "select name, catch_phrase, bs from tbl_company where user_id = %s"
    #             find_all_by_params = user.get("id")
    #             companies = find_by_all(find_all_by_id_query, find_all_by_params)
    #
    #             address_info = AddressInfo(street=address.get('street'),
    #                                        suite=address.get('suite'),
    #                                        city=address.get('city'), zipcode=address.get('zipcode'), lat=geo.get('lat'),
    #                                        lng=geo.get('lng')
    #                                        ).__dict__
    #             user_info = UserInfo(id=user.get('id'), name=user.get('name'), username=user.get('username'),
    #                                  email=user.get('email'), address=address_info, phone=user.get('phone'),
    #                                  website=user.get('website'), company=companies).__dict__
    #             user_list.append(user_info)
    # print(user_list)

    ## read
    # user_id = 1
    #
    # find_by_query = "select id, name, username, email, phone, website from tbl_users where id = %s"
    # find_by_params = user_id
    # user = find_by_id(find_by_query, find_by_params)
    #
    # find_all_by_query = "select id, name, catch_phrase, bs, user_id from tbl_company where user_id = %s"
    # companies = find_by_all(find_all_by_query, find_by_params)
    # company_list = []
    # for company in companies:
    #     company_list.append(
    #         CompanyInfo(id=company.get('id'), name=company.get('name'), catch_phrase=company.get('catch_phrase'),
    #                     bs=company.get('bs')).__dict__)
    # find_all_by_query = "select id, street, suite, city, zipcode, user_id from tbl_address where user_id = %s"
    # addresses = find_by_all(find_all_by_query, find_by_params)
    # address_list = []
    # for address in addresses:
    #     find_all_by_query = "select id, lat, lng, address_id from tbl_geo where address_id = %s"
    #     find_all_by_params = address.get('id')
    #     geos = find_by_all(find_all_by_query, find_all_by_params)
    #     for geo in geos:
    #         address_list.append(
    #             AddressInfo(id=address.get('id'), street=address.get('street'), suite=address.get('suite'),
    #                         city=address.get('city'),
    #                         zipcode=address.get('zipcode'),
    #                         geo=geo).__dict__)
    # user = UserInfo(id=user.get('id'), name=user.get('name'), username=user.get('username'), email=user.get('email'),
    #                 address=address_list,
    #                 phone=user.get('phone'), website=user.get('website'), company=company_list).__dict__
    #
    # print(user)

    ## update
    # user_update_data = {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz',
    #                     'address': [
    #                         {'id': 1, 'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough',
    #                          'zipcode': '92998-3874',
    #                          'geo': {'id': 1, 'lat': '-37.3159', 'lng': '81.1496', 'address_id': 1}
    #                          }
    #                     ],
    #                     'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org',
    #                     'company': [
    #                         {'id': 1, 'name': 'Romaguera-Crona',
    #                          'catch_phrase': 'Multi-layered client-server neural-net',
    #                          'bs': 'harness real-time e-markets'}
    #                     ]}

    # update_by_id_query = "update tbl_users set name = %s, username=%s, email = %s, phone = %s, website = %s where id = %s"
    # update_bt_id_params = ('백시현', 'baek', 'qortlgus100@qwert.com', '01011111211', 'qortlgus@qortlgus', user_update_data.get('id'))
    # update(update_by_id_query, update_bt_id_params)
    # user_id = user_update_data.get('id')
    # update_by_id_query = "update tbl_address set street = %s, suite=%s, city = %s, zipcode = %s where user_id = %s and id = %s"
    # address_list = user_update_data.get('address')
    # for address_item in address_list:
    #     address_id = address_item.get('id')
    #     update_bt_id_params = (
    #         '수원시', '장안구', '천천동', '123-123', user_update_data.get('id'), address_id)
    #     update(update_by_id_query, update_bt_id_params)
    #
    #     geo_id = address_item.get('geo').get('id')
    #     update_by_id_query = "update tbl_geo set lat= %s, lng=%s where address_id = %s and id = %s"
    #     update_bt_id_params = ('-39.0101', '-38.1010', address_id, geo_id)
    #     update(update_by_id_query, update_bt_id_params)
    # company_list = user_update_data.get('company')
    # for company_item in company_list:
    #     company_id = company_item.get('id')
    #     update_by_id_query = "update tbl_company set name = %s, catch_phrase = %s, bs = %s where user_id = %s and id = %s"
    #     update_bt_id_params = ('코리아it', 'catch_phrase', '아에이오우', user_id, company_id)
    #     update(update_by_id_query, update_bt_id_params)

    ## delete
    # user_id = 2
    #
    # delete_by_id_query = "delete from tbl_users where id = %s"
    # delete_by_id_params = user_id
    #
    # delete(delete_by_id_query, delete_by_id_params)
