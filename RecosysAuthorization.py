# import libraries
import vk_api
import pandas as pd
from vk_api.longpoll import VkLongPoll, VkEventType

# get group token
club_token = 'token'
# authorization to vk
vk_session = vk_api.VkApi(token=club_token)
# create request server
longpoll = VkLongPoll(vk_session, wait=5)
# object of vk
vk = vk_session.get_api()
random = 0


def get_user_id():
    global user_id
    random = 0
    for event in longpoll.listen():
        random += 1
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            vk.messages.send(
                user_id=event.user_id,
                random_id=random,
                message='ID принят.')
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                random += 1
                users_id = vk.users.get(user_id=event.user_id)
                user_items = pd.DataFrame(users_id)
                user_id = user_items.id[0]
                break
    return user_id


def get_name():
    global name
    random = 0
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            vk.messages.send(
                user_id=event.user_id,
                random_id=random,
                message='Название принято, запуск рекомендательной системы. Напиши что-нибудь.')
            name = str(event.message)
            random += 1
            break
    return name
