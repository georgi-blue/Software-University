journal_list = input().split(",")

while True:
    command = input().split("-")
    if command[0] == "Craft!":
        break
    else:
        action = command[0]
        if action == "Combine Items ":
            command.split(":")
            old_item = command[1]
            new_item = command[2]
            if old_item in journal_list:
                index = journal_list.index(old_item)
                journal_list.insert(index, new_item)

        else:
            item = command[1]

            if action == "Collect ":
                if item not in journal_list:
                    journal_list.append(item)

            elif action == "Drop ":
                if item in journal_list:
                    journal_list.remove(item)

            elif action == "Renew ":
                journal_list.remove(item)
                journal_list.append(item)


