from re import U
from db_issueF import user_list
from db_orderlist import order

print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")

while True:
    input_key = input("Your command >")

    if input_key == str("s"):
        order.all_print()  # 全てのデータを取得し表示

    elif input_key == str("a"):
        input_name = input("New user name >")
        input_age = input("New user age >")
        print("Add new user:", input_name)
        # user_list = user_list(Name=input_name, Age=input_age)
        # user_list.save()
        user_list.create(Name=input_name, Age=input_age)

    elif input_key == str("d"):
        input_name = input("user name >")
        print("User", input_name, " is deleted")
        msg = user_list.select().where(user_list.Name == input_name).get()
        msg.delete_instance()

    elif input_key == str("q"):
        print("Bye!")
        break

    else:
        print(input_key, ": command not found")
