from vk_api import *  # импорт всего из модуля vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json

with open("token.txt") as f:  # читаем токен из файла token.secret
    vk_session = VkApi(token=f.read(), api_version="5.103")

with open("group_id.txt") as f:  # id группы из файла
    group_id: int = int(f.read())

vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, group_id)


def start_menu(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_openlink_button("РАСПИСАНИЕ",
                           "https://guide.herzen.spb.ru/static/schedule_view.php?id_group=12456&sem=1")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("МУДЛ",
                           "https://moodle.herzen.spb.ru/my/") 
    kb.add_line()  # новая строка
    kb.add_button("КОНТАКТЫ",color=VkKeyboardColor.PRIMARY, payload={"goto": 'КОНТАКТЫ'})  # идём в раздел 1
    kb.add_line()
    kb.add_button("Раздел 2",color=VkKeyboardColor.PRIMARY, payload={"goto": 'Раздел 2'})
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Привет!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel1(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_button("отправить сообщение 1", payload={"send": "send1"})
    kb.add_line()
    kb.add_button("Назад",
                  color=VkKeyboardColor.NEGATIVE,
                  payload={"goto": "start"})

    vk.messages.send(peer_id=event.message.peer_id,
                     message="Вы в контактах!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel2(event: VkBotMessageEvent):
    kb = VkKeyboard()
    kb.add_button("отправить сообщение 1", payload={"send": "send1"})
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
                     message="Сообщение 1",
                     random_id=get_random_id())


def process(event: VkBotMessageEvent):
    text: str = event.message.text.lower()  # текст в нижнем регистре

    # текстовые команды
    if text == "привет":
        start_menu(event)

    try:
        payload: dict = json.loads(event.message.payload)
    except json.JSONDecodeError:
        return

    goto = payload.get("goto", None)
    if goto is not None:
        # команды с переходом в другой раздел
        if goto == 'КОНТАКТЫ':
            razdel1(event)
        elif goto == "start":
            start_menu(event)
        elif goto == 'Раздел 2':
            razdel2(event)
        return

    send = payload.get("send", None)
    if send is not None:
        # отправка сообщения
        if send == "send1":
            send1(event)


def listen():
    while 1:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    process(event)
        except Exception as err:
            print(err)
listen()