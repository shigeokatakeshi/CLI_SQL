from db_issueF import user_list


class order:
    def create_user():
        # インスタンスを作成してから保存
        # user_list = user_list(Name="Bob ", Age="15")
        # user_list.save()
        # インスタンスをそのまま保存
        # user_list.create(Name="Bob", Age="15")
        # user_list.create(Name="Tom", Age="57")
        user_list.create(Name="input_name", Age="input_age")

    def all_print():
        for msg in user_list.select():
            print("Name:", msg.Name, "Age:", msg.Age)
            # print(msg.id, msg.Name, msg.Age, msg.pub_date)

    def one_print():
        id = 0
        id = 1
        msg = user_list.get(user_list.id == id)
        print(msg.id, msg.Name, msg.Age, msg.pub_date)

    def id_derete():
        id = 1  # REPLで削除したのでid:1はデータが無い
        msg = user_list.select().where(user_list.id == id).get()
        msg.delete_instance()

    def data_update():
        msg = user_list.select().where(user_list.id == 1).get()
        msg.Name = "Tom Ford"
        msg.save()
