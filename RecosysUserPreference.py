# importing libraries
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType
from time import sleep

# importing modules
import RecosysAuthorization as rb

# create keyboard object
keyboard = VkKeyboard(one_time=True)

# create buttons on keyboard with our functions
keyboard.add_button('Аниме', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Фильмы', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Игры', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Вывод руководства по использованию', color=VkKeyboardColor.DEFAULT)

functions = ['Аниме', 'Фильмы', 'Игры', 'Вывод руководства по использованию']


def get_dataset_type():
    '''
    This function asks user about his preferences in useless things.

    :return: dataset_type - to set type of recommendations
    '''
    global dataset_type
    for event in rb.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text == 'Привет, Recosys.':
            rb.random += 1
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                keyboard=keyboard.get_keyboard(),
                message='Привет. Что-то нужно?')
            rb.random += 1
        if event.type == VkEventType.MESSAGE_NEW and event.message == str(functions[0]):
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Я понял. Теперь введи название на английском.')
            rb.random += 1
            dataset_type = 'anime'
            break
        if event.type == VkEventType.MESSAGE_NEW and event.message == str(functions[1]):
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Хорошо. Введи название на английском.')
            rb.random += 1
            dataset_type = 'films'
            break
        if event.type == VkEventType.MESSAGE_NEW and event.message == str(functions[2]):
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Ладно. Введи название на английском.')
            rb.random += 1
            dataset_type = 'games'
            break
        if event.type == VkEventType.MESSAGE_NEW and event.message == str(functions[3]):
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Итак, я могу подсказать тебе что можно посмотреть/поиграть, основываясь на предмете.')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Предмет - это название того, на чём нужно построить рекомендации. '
                        'Предметом может выступать название фильма или игры, название нужно писать на английском. '
                        'Связано это с тем, что все данные берутся из разных англоязычных сайтов.')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Список сайтов (можно сверяться, если бот не смог найти предмет в словаре):\n'
                        '- MyAnimeList (для аниме, логично)\n'
                        '- IMDb (для фильмов)\n'
                        '- VGTimes (для игр)')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Кстати, некоторые данные на этот момент устарели. '
                        'Например, у данных по аниме последнее обновление было в 2016 году.\n'
                        'Что это значит? '
                        '- Все тайтлы, выходившие позднее 2016 года, не берутся в расчёт при создании рекомендаций.')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='Также, наверное, нужно сказать, что система на данном этапе работает плохо, '
                        'а рекомендации не точные.\n'
                        'Но, я думаю ты знал, на что идёшь. Да?')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                message='А, чуть не забыл! '
                        'Когда система попросит что-нибудь написать, напиши. Это нужно, чтобы получить твой ID.')
            rb.random += 1
            sleep(3)
            rb.vk.messages.send(
                user_id=event.user_id,
                random_id=rb.random,
                keyboard=keyboard.get_keyboard(),
                message='Кажется, всё. Можешь начать пользоваться ботом.')
            rb.random += 1
    return dataset_type
