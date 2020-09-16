from vk_api import *  # импорт всего из модуля vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json

import random

with open("token.txt") as f:  # читаем токен из файла token.secret
    vk_session = VkApi(token=f.read(), api_version="5.103")

with open("group_id.txt") as f:  # id группы из файла
    group_id: int = int(f.read())

vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, group_id)


def start_menu(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_openlink_button("ДОМАШНЕЕ ЗАДАНИЕ",
                           "https://docs.google.com/spreadsheets/d/1pLdm10XL0JKNR5q6ibTfOfYLEjrkFfQMoaMnsBZlwZ4/edit#gid=0")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("РАСПИСАНИЕ",
                           "https://guide.herzen.spb.ru/static/schedule_view.php?id_group=12456&sem=1")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("МУДЛ",
                           "https://moodle.herzen.spb.ru/my/") 
    kb.add_line()  # новая строка
    kb.add_button("КОНТАКТЫ",color=VkKeyboardColor.PRIMARY, payload={"goto": 'КОНТАКТЫ'})  # идём в раздел 1
    kb.add_line()
    kb.add_button("РАНДОМ",color=VkKeyboardColor.POSITIVE, payload={"goto": 'РАНДОМ'})
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Привет!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel1(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_button("КОНТАКТЫ СТАРОСТ",color=VkKeyboardColor.PRIMARY, payload={"send": "send1"})
    kb.add_line()
    kb.add_button("КОНТАКТЫ ДЕКАНАТА",color=VkKeyboardColor.PRIMARY, payload={"send": "send6"})
    kb.add_line()  #    ДОБАВИЛ ЯЯЯЯЯЯ
    kb.add_button("КОНТАКТЫ ПРОФСОЮЗА И ПРОФКОМА",color=VkKeyboardColor.PRIMARY, payload={"send": "send3"})
    kb.add_line()
    kb.add_button("Назад",
                  color=VkKeyboardColor.NEGATIVE,
                  payload={"goto": "start"})

    vk.messages.send(peer_id=event.message.peer_id,
                     message="Вы в контактах",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel2(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_button("отправить сообщение 1", payload={"send": "send1"})
    kb.add_line()
    kb.add_button("ОРЕЛ И РЕШКА", payload={"send": "orel"})
    kb.add_line()
    kb.add_button("Назад",
                  color=VkKeyboardColor.NEGATIVE,
                  payload={"goto": "start"})

    vk.messages.send(peer_id=event.message.peer_id,
                     message="Раздел 2",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())



def send1(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Александра Епифанцева\nСтароста\n+7 (981) 975-31-99\nsani403@mail.ru\n\n\nКирилл Кувшинов\nЗам. Старосты\n+7 (952) 969-38-64\nkuvshinovich.01@mail.ru\n\n\nСветлана Николаевна\nОтветственная за расписание на нашем направлении\n+7 (911) 231-41-80\nsveta25.03@yandex.ru",
                     random_id=get_random_id())
def send3(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Владимир Валерьевич Казанкин\n+7 (951) 647-09-05\n\nАлександра\n+7 (911) 822-59-25\n\nОбщий\n+7 (812) 570-14-12\n\nПрофком\n+7 (812) 570-14-12",
                     random_id=get_random_id())

def send6(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Адрес: 191186, г. Санкт-Петербург, наб. реки Мойки, корп. 2, ауд. 266\n\nТелефон: +7 (812) 571-10-03\n\nПочта: icsto@herzen.spb.ru\n\nЧасы приема директора института: вт, чт с 14:00 до 16:00",
                     random_id=get_random_id())                 #    ДОБАВИЛ ЯЯЯЯЯЯ

def orel(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message=random.choice(["Орел","Решка"]),
                     random_id=get_random_id())

def process(event: VkBotMessageEvent):
    text: str = event.message.text.lower()  # текст в нижнем регистре






    # текстовые команды
    if text == "привет":
        start_menu(event)
        return
    try:
        payload: dict = json.loads(event.message.payload)
    except json.JSONDecodeError:
        vk.messages.send(peer_id=event.message.peer_id,
                     message="Неизвестная комманда, введите \"привет\" для продолжения.",
                     random_id=get_random_id()) 
        return

    goto = payload.get("goto", None)
    if goto is not None:
        # команды с переходом в другой раздел
        if goto == 'КОНТАКТЫ':
            razdel1(event)
        elif goto == "start":
            start_menu(event)
        elif goto == 'РАНДОМ':
            razdel2(event)
        return

    send = payload.get("send", None)
    if send is not None:
        # отправка сообщения
        if send == "send1":
            send1(event)
        elif send == "send6":                                  #    ДОБАВИЛ ЯЯЯЯЯЯ
            send6(event)                            #    ДОБАВИЛ ЯЯЯЯЯЯ
        elif send == "send3":                                  #    ДОБАВИЛ ЯЯЯЯЯЯ
            send3(event) 
        elif send == "orel":
            orel(event)
        return
    vk.messages.send(peer_id=event.message.peer_id,
                message="Неизвестная комманда, введите \"привет\" для продолжения.",
                random_id=get_random_id())

def listen():
    while 1:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    process(event)
        except Exception as err:
            print(err)
listen()