import handler

handler = handler.CommandHandler()
while True:
    handler.set_new_host(str(input("Enter recipe source link\n>")))
    print(handler.get_dto())
