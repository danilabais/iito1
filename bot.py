from vk_api import *  # импорт всего из модуля vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, sjson_dumps
from vk_api.utils import get_random_id
import six
import json

import random

with open("token.txt") as f:  # читаем токен из файла token.secret
    vk_session = VkApi(token=f.read(), api_version="5.150")

with open("group_id.txt") as f:  # id группы из файла
    group_id: int = int(f.read())

vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, group_id)


class VkKeyboardCallback(VkKeyboard):
    def add_callback_button(self, label, color='default', payload=None):
        """ Добавить кнопку с текстом.
            Максимальное количество кнопок на строке - 4

        :param label: Надпись на кнопке и текст, отправляющийся при её нажатии.
        :type label: str
        :param color: цвет кнопки.
        :type color: VkKeyboardColor or str
        :param payload: Параметр для callback api
        :type payload: str or list or dict
        """

        current_line = self.lines[-1]

        if len(current_line) >= 4:
            raise ValueError('Max 4 buttons on a line')

        color_value = color

        if isinstance(color, VkKeyboardColor):
            color_value = color_value.value

        if payload is not None and not isinstance(payload, six.string_types):
            payload = sjson_dumps(payload)

        button_type = "callback"

        current_line.append({
            'color': color_value,
            'action': {
                'type': button_type,
                'payload': payload,
                'label': label,
            }
        })


def fuck(event: VkBotMessageEvent):
    kb = VkKeyboardCallback(inline=True)
    kb.add_callback_button("Пожелать спокойной ночи беседе!",
                           color=VkKeyboardColor.PRIMARY, link="https://vk.com", type="open_link")
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Привет!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def start_menu(event: VkBotMessageEvent):
    kb = VkKeyboardCallback()
    kb.add_openlink_button("ДОМАШНЕЕ ЗАДАНИЕ",
                           "https://docs.google.com/spreadsheets/d/1pLdm10XL0JKNR5q6ibTfOfYLEjrkFfQMoaMnsBZlwZ4/edit#gid=0")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("РАСПИСАНИЕ",
                           "https://guide.herzen.spb.ru/static/schedule_view.php?id_group=12456&sem=2")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("МУДЛ",
                           "https://moodle.herzen.spb.ru/my/")
    kb.add_line()  # новая строка
    kb.add_callback_button("КОНТАКТЫ", color=VkKeyboardColor.PRIMARY,
                           payload={"goto": 'КОНТАКТЫ'})  # идём в раздел 1
    kb.add_line()
    kb.add_callback_button("Случайный человек", payload={"send": "randomuser"})
    kb.add_callback_button("ОРЕЛ И РЕШКА", payload={"send": "orel"})
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Привет!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def vvi(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Введение в информатику (+вви)\n\nСсылка для конференции в Zoom:\n https://vk.com/away.php?to=https%3A%2F%2Fus04web.zoom.us%2Fj%2F5656613684%3Fpwd%3DNndPNWFENmMyNWNwMzE5OGNXdjhJZz09%5Cn&cc_key= Идентификатор конференции: 565 661 3684\n Код доступа: 860852 \n\n Курс в Moodle: \n https://moodle.herzen.spb.ru/course/view.php?id=7496 \n\n Не забудьте войти в чат, который висит в самом верху и поздороваться!",
                     random_id=get_random_id())

def a(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Алгебра (+а) \n\n Ссылка для конференции в Zoom: \n https://vk.com/away.php?to=https%3A%2F%2Fus04web.zoom.us%2Fj%2F4480633030%3Fpwd%3DM29zSWRQUGRYWS9USFJheDdsdTdMQT09&cc_key= \n\n Материалы для лекций и домашних заданий на Google Диске:  \nhttps://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1pBRk3BMrfiiFX7FA0b8Qiae36ov2U_te%3Fusp%3Dsharing&cc_key=",
                     random_id=get_random_id())

def p(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Программирование (+п): \n\n Ссылка для конференции в Google Meet: \n https://meet.google.com/hvj-swyu-dhg \n\n Ссылка на курс в Moodle: \n https://moodle.herzen.spb.ru/course/view.php?id=1391",
                     random_id=get_random_id())

def ikl(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Информационная культура личности (+икл): \nСсылка на курс в Moodle (где размещается непостоянная ссылка каждую пару): \n https://moodle.herzen.spb.ru/course/view.php?id=5280 \n\n Ссылка на Электронный журнал: \nhttps://vk.com/away.php?to=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F13_lS1BCe1CF3q9th3Bkz8j7UYhJ3Sf_8da3mU6M-mkc%2Fedit%3Fusp%3Dsharing&cc_key=\n\n Ссылка на таблицу с адресами сайтов: \nhttps://vk.com/away.php?to=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1mGkvRX8PM6pGPpN4mlFr8VKULG9wNJrb3et6Yyce2uw%2Fedit%3Fusp%3Dsharing&cc_key=",
                     random_id=get_random_id())

def en(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Иностранный язык (+иняз): \n\n Ссылка на конференцию в Zoom: \nhttps://vk.com/away.php?to=https%3A%2F%2Fzoom.us%2Fj%2F5227891980%3Fpwd%3DMU81SDNUOEFKN2hLaWhJZzhDcko5dz09&cc_key=\n Идентификатор конференции: 522 789 1980 \n Код доступа: VApZ9F \n\n Ссылка на Практический курс в Moodle: \n https://moodle.herzen.spb.ru/course/view.php?id=9004 \n\n Ссылка на Лекционный курс в Moodle: \n https://moodle.herzen.spb.ru/course/view.php?id=17109 \n\n Но для начала войдите в чат в Практическом ЭУК-е и поздоровайтесь (Hello, Good Day, Good afternoon)!",
                     random_id=get_random_id())

def g(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Геометрия (+г): \n\n Ссылка на конференцию в Zoom: \nhttps://vk.com/away.php?to=https%3A%2F%2Fus04web.zoom.us%2Fj%2F5656613684%3Fpwd%3DNndPNWFENmMyNWNwMzE5OGNXdjhJZz09&cc_key=Идентификатор конференции: 565 661 3684 \n Код доступа: 860852 \n\n Ссылка на курс в Moodle: \n https://moodle.herzen.spb.ru/course/view.php?id=8219 \n\n Ссылка на Доску: \n https://www.notebookcast.com/en/board/7g1ottpcd8e4 \n\n Ссылка на профиль Светлакова в ЖЖ: \n https://mathdialogue.livejournal.com/",
                     random_id=get_random_id())

def ph(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Философия (+ф): \n\n Ссылка на курс в Moodle (в шапке висит непостоянная ссылка для занятий. если её нет, то в шапке должно быть задание на сегодняшний день): \n https://moodle.herzen.spb.ru/course/view.php?id=24504",
                     random_id=get_random_id())






def spok(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Введение в информатику\nИскусственный интеллект (KiReal) приглашает вас на зум-пару по ссылке:\n\nhttps://us04web.zoom.us/j/75923959296?pwd=elNzS082MkNxOW9hdGFNOGRNenMwQT09\nИдентификатор конференции: 759 2395 9296\nКод доступа: zjPXE6\n\nТакже, следует войти в чат по ссылке:\nhttps://moodle.herzen.spb.ru/mod/chat/gui_ajax/index.php?id=53362",
                     random_id=get_random_id())


def v(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Пожалуйста, @everyone, перейдите в \"Важное за день\" по ссылке:\n\nhttps://vk.cc/aAFgWr\n\n&#127381;&#127384;&#127381;&#127384;&#127381;&#127384;&#127381;&#127384;&#127381;",
                     random_id=get_random_id())


def k(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Пожалуйста, перейдите в \"Важное за день\" по ссылке:\n\nhttps://vk.cc/aAFgWr\n\n&#127381;&#127384;&#127381;&#127384;&#127381;&#127384;&#127381;&#127384;&#127381;",
                     random_id=get_random_id())

def i(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Алгебра\nИскусственный интеллект (OkeyGoogle) приглашает вас на зум-пару по ссылке:\n\nhttps://us04web.zoom.us/j/4480633030?pwd=M29zSWRQUGRYWS9USFJheDdsdTdMQT09#success\n\nТакже следует зайти в общую папку с материалами:\nhttps://drive.google.com/drive/folders/1pBRk3BMrfiiFX7FA0b8Qiae36ov2U_te\n\nСсылка на Sage:\nhttps://cocalc.com/app",
                     random_id=get_random_id())

def ii(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="С Днем рождения, Саша!\n Желаю добра, здоровья, побольше пятерок, хотя ты только их  и получаешь)) \nОставайся такой же лучшей старостой в мире!!!",
                     random_id=get_random_id())

def urlkb(event: VkBotMessageEvent):
    kb = VkKeyboardCallback()

    kb.add_openlink_button("В ГРУППУ",
                           "https://vk.com/club198561767")  # кнопка с ссылкой
    kb.add_line()
    kb.add_openlink_button("ДОМАШНЕЕ ЗАДАНИЕ",
                           "https://docs.google.com/spreadsheets/d/1pLdm10XL0JKNR5q6ibTfOfYLEjrkFfQMoaMnsBZlwZ4/edit#gid=0")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("РАСПИСАНИЕ",
                           "https://guide.herzen.spb.ru/static/schedule_view.php?id_group=12456&sem=2")  # кнопка с ссылкой
    kb.add_line()  # новая строка
    kb.add_openlink_button("МУДЛ",
                           "https://moodle.herzen.spb.ru/my/")
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Привет!",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel1(event: VkBotMessageEvent):
    kb = VkKeyboard(inline=True)
    kb.add_button("КОНТАКТЫ СТАРОСТ", color=VkKeyboardColor.PRIMARY,
                  payload={"send": "send1"})
    kb.add_line()
    kb.add_button("КОНТАКТЫ ДЕКАНАТА",
                  color=VkKeyboardColor.PRIMARY, payload={"send": "send6"})
    kb.add_line()
    kb.add_button("КОНТАКТЫ ПРОФСОЮЗА И ПРОФКОМА",
                  color=VkKeyboardColor.PRIMARY, payload={"send": "send3"})
    kb.add_line()
    kb.add_button("Назад",
                  color=VkKeyboardColor.NEGATIVE,
                  payload={"goto": "start"})

    vk.messages.send(peer_id=event.message.peer_id,
                     message="Вы в контактах",
                     random_id=get_random_id(),
                     keyboard=kb.get_keyboard())


def razdel2(event: VkBotMessageEvent):
    kb = VkKeyboard(inline=True)
    kb.add_button("Случайный человек", payload={"send": "randomuser"})
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

def helper(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Подсказка по предметам: \n\n - Введение в информатику (+вви) \n - Алгебра (+а) \n - Программирование (+п) \n - Информационная культура личности (+икл) \n - Иностранный язык (+иняз) \n - Геометрия (+г) \n - Философия (+ф)",
                     random_id=get_random_id())


def send3(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Владимир Валерьевич Казанкин\n+7 (951) 647-09-05\n\nАлександра\n+7 (911) 822-59-25\n\nОбщий\n+7 (812) 570-14-12\n\nПрофком\n+7 (812) 570-14-12",
                     random_id=get_random_id())


def send6(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Адрес: 191186, гСанкт-Петербург, наб. реки Мойки, корп. 2, ауд. 266\n\nТелефон: +7 (812) 571-10-03\n\nПочта: icsto@herzen.spb.ru\n\nЧасы приема директора института: вт, чт с 14:00 до 16:00",
                     random_id=get_random_id())  # ДОБАВИЛ ЯЯЯЯЯЯ


def orel(event: VkBotMessageEvent):
    vk.messages.send(peer_id=event.message.peer_id,
                     message=random.choice(["Орел", "Решка"]),
                     random_id=get_random_id())


def cmdNotFound(event: VkBotMessageEvent):
    if event.from_chat:
        return
    vk.messages.send(peer_id=event.message.peer_id,
                     message="Неизвестная комманда, введите \"+urlkb\" или \"+kb\" для продолжения.",
                     random_id=get_random_id())


def randomuser(event: VkBotMessageEvent):
    profiles = vk.messages.getConversationMembers(peer_ids=str(
        event.message.peer_id), extended=True)["profiles"]
    profile = random.choice(profiles)
    text = f"@id{profile['id']} ({profile['first_name']} {profile['last_nameа']})"
    vk.messages.send(peer_id=event.message.peer_id,
                     message=text,
                     random_id=get_random_id())


def process(event: VkBotMessageEvent):
    text: str = event.message.text.lower()

    # текстовые команды
    if text == "+kb":
        start_menu(event)
        return
    elif text == "+urlkb":
        urlkb(event)
        return
    elif text == "+вв":
        spok(event)
        return
    elif text == "+рандом":
        randomuser(event)
        return
    elif text == "+v":
        v(event)
        return
    elif text == "+а":
        i(event)
        return
    elif text == "04":
        ii(event)
        return
    elif text == "+вви":
        vvi(event)
        return
    elif text == "+а":
        a(event)
        return
    elif text == "+п":
        p(event)
        return
    elif text == "+подсказки":
        helper(event)
        return
    elif text == "+икл":
        ikl(event)
        return
    elif text == "+иняз":
        en(event)
        return
    elif text == "+г":
        g(event)
        return
    elif text == "+ф":
        ph(event)
        return
    elif text == "+f":
        fuck(event)
        return
    try:
        payload: dict = json.loads(event.message.payload)
    except json.JSONDecodeError:
        cmdNotFound(event)
        return
    except TypeError:
        cmdNotFound(event)
        return
    if payload.get("command", None) == 'not_supported_button':
        while 1:
            try:
                payload = json.loads(payload["payload"])
            except Exception:
                break
    goto = payload.get("goto", None)
    if goto is not None:
        # команды с переходом в другой раздел
        if goto == 'КОНТАКТЫ':
            razdel1(event)
        elif goto == "start":
            start_menu(event)
        elif goto == "спок":
            spok(event)
        elif goto == 'РАНДОМ':
            razdel2(event)
        return

    send = payload.get("send", None)
    if send is not None:
        # отправка сообщения
        if send == "send1":
            send1(event)
        elif send == "send6":
            send6(event)
        elif send == "send3":
            send3(event)
        elif send == "orel":
            orel(event)
        elif send == "randomuser":
            randomuser(event)
        return
    cmdNotFound(event)


def processCallback(event):
    payload: dict = event.payload
    goto: str = payload.get("goto", None)
    if goto == 'КОНТАКТЫ':
        kb = VkKeyboard()
        kb.add_button("КОНТАКТЫ СТАРОСТ", color=VkKeyboardColor.PRIMARY,
                      payload={"send": "send1"})
        kb.add_line()
        kb.add_button("КОНТАКТЫ ДЕКАНАТА",
                      color=VkKeyboardColor.PRIMARY, payload={"send": "send6"})
        kb.add_line()  # ДОБАВИЛ ЯЯЯЯЯЯ
        kb.add_button("КОНТАКТЫ ПРОФСОЮЗА И ПРОФКОМА",
                      color=VkKeyboardColor.PRIMARY, payload={"send": "send3"})
        try:
            vk.messages.send(peer_id=event["user_id"],
                             message="Вы в контактах",
                             random_id=get_random_id(),
                             keyboard=kb.get_keyboard())
        except Exception:
            vk.messages.sendMessageEventAnswer(**event, event_data=json.dumps({
                "type": "show_snackbar",
                "text": "Бот не смог отправить сообщение в лс"}))
        else:
            vk.messages.sendMessageEventAnswer(**event, event_data=json.dumps({
                "type": "open_link",
                "link": "https://vk.me/club198561767"
            }))
    send: str = payload.get("send", None)
    if send == "orel":
        vk.messages.send(peer_id=event.peer_id,
                         message=f"@id{event.user_id} выпал(а):\n{random.choice(['Орел', 'Решка'])}",
                         random_id=get_random_id())
        vk.messages.sendMessageEventAnswer(**event, event_data=json.dumps({
            "type": "show_snackbar",
            "text": "Команда успешно выполнена"}))
    elif send == "randomuser":
        profiles = vk.messages.getConversationsById(peer_ids=str(
            event.peer_id), extended=True)["profiles"]  # люди в этой беседе
        profile = random.choice(profiles)
        text = f"@id{event.user_id} зарандомил случайного человека, выпал/a:\n@id{profile['id']} ({profile['first_name']} {profile['last_name']})"
        vk.messages.send(peer_id=event.peer_id,
                         message=text,
                         random_id=get_random_id())
        vk.messages.sendMessageEventAnswer(**event, event_data=json.dumps({
            "type": "show_snackbar",
            "text": "Команда успешно выполнена"}))


def listen():
    while 1:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    process(event)
                elif event.type == 'message_event':
                    processCallback(event.obj)
        except Exception as err:
            print(err)


listen()
