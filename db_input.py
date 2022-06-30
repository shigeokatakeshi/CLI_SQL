from db_issueF import user_list


def create_user():
    # インスタンスを作成してから保存
    # user_list = user_list(Name="Bob ", Age="15")
    # user_list.save()
    # インスタンスをそのまま保存
    # user_list.create(Name="Bob", Age="15")
    # user_list.create(Name="Tom", Age="57")
    user_list.create(Name="Ken", Age="73")


def all_print():
    for msg in user_list.select():
        print(msg.id, msg.Name, msg.Age, msg.pub_date)


def one_print():
    id = 0
    id = 1
    msg = user_list.get(user_list.id == id)
    print(msg.id, msg.Name, msg.Age, msg.pub_date)


def id_derete():
    id = 2  # REPLで削除したのでid:1はデータが無い
    msg = user_list.select().where(user_list.id == id).get()
    msg.delete_instance()


def data_update():
    msg = user_list.select().where(user_list.id == 17).get()
    msg.Name = "Tom Ford"
    msg.save()


if __name__ == "__main__":
    # create_user()  # id 作成
    input_key = input("Your command >")
    # print(input_key)
    if input_key == str("s"):
        all_print()  # 全てのデータを取得し表示

    # one_print()   # 一つのデータを取得し表示

    # id_derete()   # id 消去

    # data_update()
