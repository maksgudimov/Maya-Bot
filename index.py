from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from emoji import emojize
from dateutil.relativedelta import relativedelta
# from lorabot.lorabot import LoraBot



import sqlite3 as sq
import sqlite3
import logging
import time
import datetime
import schedule
import asyncio
import threading
import io
import math

import openai
from googletrans import Translator

from aiogram.types import ChatActions

openai.api_key = "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" #
translator = Translator()

storage = MemoryStorage()

bot = Bot(token="5454478500:AAEE7tWJYsdMbP7tFpMT-ktMW-wcH3Zpios") #5454478500:AAEE7tWJYsdMbP7tFpMT-ktMW-wcH3Zpios

dp = Dispatcher(bot,storage=storage)
logging.basicConfig(level=logging.INFO)

scheduler = AsyncIOScheduler()

CHAT_ID = '-844286975'

#print(datetime.datetime.today().weekday())

# day2 = datetime.date.today() + relativedelta(months=-1)
# print(today)
# print(day2)
# print(datetime.timedelta(2))
# lora_bot = LoraBot("MAYA_TEST")





async def on_startup(_):
    print('Бот вышел в онлайн')
    global base, cur
    base = sq.connect('main.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')

    #print(openai.Model.list())
    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER,datatime REAL,call TEXT,link TEXT, name TEXT, spec TEXT, write_about TEXT,city TEXT,company TEXT,clever TEXT,q_help TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS questions(id INTEGER,datatime REAL,call TEXT,link TEXT, text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS poshelania(id INTEGER,datatime REAL,call TEXT,link TEXT, text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS whatisfailed(id INTEGER,datatime REAL,call TEXT,link TEXT, text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS impression(id INTEGER,datatime REAL,call TEXT,link TEXT, text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS findispoln(id INTEGER,datatime REAL,call TEXT,link TEXT, who TEXT,srok TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS adminNews(id INTEGER,who TEXT,img TEXT,text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS adminNewsLast(id INTEGER,img TEXT,text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS adminNewsBest(id INTEGER,img TEXT,text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS adminAvent(id INTEGER, img TEXT,text TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS myResume(id INTEGER, datatime REAL,call TEXT,link TEXT,what TEXT,who TEXT,describe TEXT,link2 TEXT,price TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS nextgo(id INTEGER,datatime REAL,call INTEGER,name TEXT,answer INTEGER,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS statistic_start(id INTEGER,datatime REAL,spec TEXT,call INTEGER,kol INTEGER,PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()



# def mes(callback):
#     bot.send_message(callback,f"test")
#
# def message2days(callback):
#     schedule.every().minute().do(mes(callback))
#     while True:
#         schedule.run_pending()
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users(datatime,call,link,name,spec) VALUES (?,?,?,?,?)',tuple(data.values()))
        base.commit()

async def sql_add_q(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO questions(datatime,call,text,link) VALUES (?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_poshelania(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO poshelania(datatime,call,text,link) VALUES (?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_fail(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO whatisfailed(datatime,call,text,link) VALUES (?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_impression(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO impression(datatime,call,text,link) VALUES (?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_ispoln(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO findispoln(datatime,call,link,who,srok) VALUES (?,?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_adminNews(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO adminNews(who,img,text) VALUES (?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_adminAvent(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO adminAvent(img,text) VALUES (?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_MyResume(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO myResume(datatime,call,link,what,who,describe,link2,price) VALUES (?,?,?,?,?,?,?,?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_adminNewsLast(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO adminNewsLast(text) VALUES (?)',
                    tuple(data.values()))
        base.commit()

async def sql_add_adminNewsBest(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO adminNewsBest(text) VALUES (?)',
                    tuple(data.values()))
        base.commit()

# analytics_markup = types.ReplyKeyboardMarkup(True)
# menu_analytics = ['Total', 'Users', 'Messages', 'Events', 'Rating', 'SQL']
# analytics_markup.row(menu_analytics[0], menu_analytics[1])
# analytics_markup.row(menu_analytics[2], menu_analytics[3])
# analytics_markup.row(menu_analytics[4])
# analytics_markup.row(menu_analytics[5])
#
# no_markup = types.ReplyKeyboardMarkup(True)
# no_markup.row('No')

kb_spec = types.InlineKeyboardMarkup(row_width=1)
spec_b1 = types.InlineKeyboardButton(text=f"{emojize(':shopping_bags:')} Стилист", callback_data="spec_stylist")
spec_b2 = types.InlineKeyboardButton(text=f"{emojize(':lab_coat:')} Дизайнер", callback_data="spec_designer")
spec_b3 = types.InlineKeyboardButton(text=f"{emojize(':thread:')} Владелец производства", callback_data="spec_ProductionOwner")
spec_b4 = types.InlineKeyboardButton(text=f"{emojize(':newspaper:')} Специалист по рекламе", callback_data="spec_Marketing")
spec_b5 = types.InlineKeyboardButton(text=f"{emojize(':label:')} Владелец бренда", callback_data="spec_BrandOwner")
spec_b6 = types.InlineKeyboardButton(text=f"{emojize(':triangular_ruler:')} Конструктор", callback_data="spec_constructor")
spec_b7 = types.InlineKeyboardButton(text=f"{emojize(':bookmark_tabs:')} Байер", callback_data="spec_bayer")
spec_b8 = types.InlineKeyboardButton(text=f"{emojize(':office_building:')} Владелец бутика", callback_data="spec_boutiqueOwner")
spec_b9 = types.InlineKeyboardButton(text=f"{emojize(':NEW_button:')} Свой вариант", callback_data="spec_MyAnswer")
kb_spec.add(spec_b1,spec_b2,spec_b3,spec_b4,spec_b5,spec_b6,spec_b7,spec_b8,spec_b9)

# kb_bot = types.InlineKeyboardMarkup(row_width=1)
# bot_b1 = types.InlineKeyboardButton(text=f"{emojize(':magnifying_glass_tilted_left:')} Находить нужные контакты", callback_data="bot_contacts")
# bot_b2 = types.InlineKeyboardButton(text=f"{emojize(':mirror_ball:')} Организовывать еженедельный нетворкинг с другими пользователями", callback_data="bot_sure")
# bot_b3 = types.InlineKeyboardButton(text=f"{emojize(':bookmark_tabs:')} Присылать персональные подборки полезных материалов, мероприятий, последних новостей модного бизнеса", callback_data="bot_news")
# bot_b4 = types.InlineKeyboardButton(text=f"{emojize(':identification_card:')} Выдавать резюме специалистов", callback_data="bot_resume")
# bot_b5 = types.InlineKeyboardButton(text=f"{emojize(':pushpin:')} Публиковать вакансии", callback_data="bot_vacanci")
# bot_b6 = types.InlineKeyboardButton(text=f"{emojize(':woman_dancing:')} Танцевать румбу", callback_data="bot_rumba")
#
# kb_bot.add(bot_b1,bot_b2,bot_b3,bot_b4,bot_b5,bot_b6)

kb_answer1 = types.InlineKeyboardMarkup(row_width=1)
answer1_b1 = types.InlineKeyboardButton(text=f"{emojize(':magnifying_glass_tilted_left:')} Нетворкинг с коллегами", callback_data="answer_networks")
answer1_b2 = types.InlineKeyboardButton(text=f"Сообщество Майи 💵", url="https://t.me/+25qhiIYCgWw3ZTVi")#{emojize(':newspaper:')}  callback_data="answer_news" Новости и анонсы мероприятий раньше была
answer1_b3 = types.InlineKeyboardButton(text=f"{emojize(':identification_card:')} Опубликовать вакансию", callback_data="answer_ispoln")
answer1_b4 = types.InlineKeyboardButton(text=f"{emojize(':briefcase:')} Предложить свои услуги", callback_data="answer_my")
answer1_b5 = types.InlineKeyboardButton(text=f"{emojize(':fire:')} Майя, помоги", callback_data="answer_helpme")
answer1_b6 = types.InlineKeyboardButton(text=f"Искусственный Интеллект Майи 💡", callback_data="answer_AI")
kb_answer1.add(answer1_b1,answer1_b2,answer1_b3,answer1_b4,answer1_b5,answer1_b6)

kb_answer2 = types.InlineKeyboardMarkup(row_width=1)
answer2_b1 = types.InlineKeyboardButton(text=f"Подожди, есть вопрос!", callback_data="answer2_question")
answer2_b2 = types.InlineKeyboardButton(text=f"Да, начинаем!", callback_data="answer2_yes")
kb_answer2.add(answer2_b1,answer2_b2)

kb_answer3 = types.InlineKeyboardMarkup(row_width=1)
answer3_b1 = types.InlineKeyboardButton(text=f"Подожди, есть вопрос!", callback_data="answer3_question")
answer3_b2 = types.InlineKeyboardButton(text=f"Да, иду знакомиться!", callback_data="answer3_yes")
kb_answer3.add(answer3_b1,answer3_b2)

kb_parser = types.InlineKeyboardMarkup(row_width=1)
parser_b1 = types.InlineKeyboardButton(text=f"{emojize(':newspaper:')} Новости", callback_data="parser_news")
parser_b2 = types.InlineKeyboardButton(text=f"{emojize(':calendar:')} Мероприятия", callback_data="parser_meropri")
kb_parser.add(parser_b1,parser_b2)

def kb_dop_parser(callback):
    # (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = {callback}").fetchone()
    # base.commit()
    kb_dop_parser = types.InlineKeyboardMarkup(row_width=1)
    dop_b1 = types.InlineKeyboardButton(text=f"Последние новости", callback_data="dop_news")
    #dop_b2 = types.InlineKeyboardButton(text=f"Персональная подборка", callback_data="dop_meropri")
    dop_b3 = types.InlineKeyboardButton(text=f"Лучшее за месяц", callback_data="dop_mounth")
    kb_dop_parser.add(dop_b1,dop_b3)
    return kb_dop_parser

kb_answer4 = types.InlineKeyboardMarkup(row_width=1)
# answer4_b1 = types.InlineKeyboardButton(text=f"Да", callback_data="answer4_yes")
# answer4_b2 = types.InlineKeyboardButton(text=f"Нет", callback_data="answer4_no")
answer4_b3 = types.InlineKeyboardButton(text=f"Дальше {emojize(':right_arrow:')}", callback_data="answer4_more")
kb_answer4.add(answer4_b3)

kb_answer6 = types.InlineKeyboardMarkup(row_width=1)
# answer6_b1 = types.InlineKeyboardButton(text=f"Да", callback_data="answer6_yes")
# answer6_b2 = types.InlineKeyboardButton(text=f"Нет", callback_data="answer6_no")
answer6_b3 = types.InlineKeyboardButton(text=f"Дальше {emojize(':right_arrow:')}", callback_data="answer6_more")
kb_answer6.add(answer6_b3)

kb_answer7 = types.InlineKeyboardMarkup(row_width=1)
# answer7_b1 = types.InlineKeyboardButton(text=f"Да", callback_data="answer7_yes")
# answer7_b2 = types.InlineKeyboardButton(text=f"Нет", callback_data="answer7_no")
answer7_b3 = types.InlineKeyboardButton(text=f"Дальше {emojize(':right_arrow:')}", callback_data="answer7_more")
kb_answer7.add(answer7_b3)

kb_answer8 = types.InlineKeyboardMarkup(row_width=1)
# answer8_b1 = types.InlineKeyboardButton(text=f"Да", callback_data="answer8_yes")
# answer8_b2 = types.InlineKeyboardButton(text=f"Нет", callback_data="answer8_no")
answer8_b3 = types.InlineKeyboardButton(text=f"Дальше {emojize(':right_arrow:')}", callback_data="answer8_more")
kb_answer8.add(answer8_b3)


kb_answer5 = types.InlineKeyboardMarkup(row_width=1)
answer5_b1 = types.InlineKeyboardButton(text=f"Да, хочу задать", callback_data="answer5_yes")
answer5_b2 = types.InlineKeyboardButton(text=f"Нет, все отлично", callback_data="answer5_no")
kb_answer5.add(answer5_b1,answer5_b2)

kb_days2answer1 = types.InlineKeyboardMarkup(row_width=1)
days2answer1_b1 = types.InlineKeyboardButton(text=f"Да", callback_data="days2answer1_yes")
days2answer1_b2 = types.InlineKeyboardButton(text=f"Нет", callback_data="days2answer1_no")
kb_days2answer1.add(days2answer1_b1,days2answer1_b2)

kb_days2answer2 = types.InlineKeyboardMarkup(row_width=1)
days2answer2_b1 = types.InlineKeyboardButton(text=f"Еще не связались", callback_data="days2answer2_nosobes")
days2answer2_b2 = types.InlineKeyboardButton(text=f"Собеседник не ответил", callback_data="days2answer2_noanswer")
days2answer2_b3 = types.InlineKeyboardButton(text=f"Не договорились по времени", callback_data="days2answer2_notime")
days2answer2_b4 = types.InlineKeyboardButton(text=f"Другое", callback_data="days2answer2_some")
kb_days2answer2.add(days2answer2_b1,days2answer2_b2,days2answer2_b3,days2answer2_b4)

kb_days2answer3 = types.InlineKeyboardMarkup(row_width=1)
days2answer3_b1 = types.InlineKeyboardButton(text=f"Да {emojize(':repeat_button:')}", callback_data="days2answer3_yes")
days2answer3_b2 = types.InlineKeyboardButton(text=f"Возьму паузу {emojize(':pause_button:')}", callback_data="days2answer3_pause")
kb_days2answer3.add(days2answer3_b1,days2answer3_b2)

kb_helpMaya = types.InlineKeyboardMarkup(row_width=1)
helpMaya_b1 = types.InlineKeyboardButton(text=f"Да, есть запрос", callback_data="helpMaya_yes")
helpMaya_b2 = types.InlineKeyboardButton(text=f"Сейчас нет запроса", callback_data="helpMaya_no")
kb_helpMaya.add(helpMaya_b1,helpMaya_b2)



def kb_for_admin():
    kb_admin = types.InlineKeyboardMarkup(row_width=1)
    admin_b1 = types.InlineKeyboardButton(text=f"Статистика", callback_data="admin_stats")
    admin_b2 = types.InlineKeyboardButton(text=f"Добавить мероприятие в Базу Данных", callback_data="admin_avent")
    admin_b3 = types.InlineKeyboardButton(text=f"Ответить пользователю", callback_data="admin_answer")
    admin_b4 = types.InlineKeyboardButton(text=f"Ответить по группам(Дизайнеры и т.д.)", callback_data="admin_group")
    admin_b5 = types.InlineKeyboardButton(text=f"Написать всем", callback_data="admin_all")
    admin_b6 = types.InlineKeyboardButton(text=f"Удалить все Новости", callback_data="admin_delNews")
    admin_b7 = types.InlineKeyboardButton(text=f"Удалить все Мероприятия", callback_data="admin_delAvent")
    admin_b8 = types.InlineKeyboardButton(text=f"Добавить последние новости", callback_data="admin_lastNews")
    admin_b9 = types.InlineKeyboardButton(text=f"Добавить лучшее за месяц", callback_data="admin_bestNews")
    admin_b10 = types.InlineKeyboardButton(text=f"Ответить по группам(нетворкинг и т.д.)", callback_data="admin_groupdb")
    kb_admin.add(admin_b1,admin_b8,admin_b9,admin_b2,admin_b3,admin_b4,admin_b5,admin_b6,admin_b7,admin_b10)
    return kb_admin

kb_group = types.InlineKeyboardMarkup(row_width=1)
group_b1 = types.InlineKeyboardButton(text=f"Стилист", callback_data="group_stylist")
group_b2 = types.InlineKeyboardButton(text=f"Дизайнер", callback_data="group_designer")
group_b3 = types.InlineKeyboardButton(text=f"Владелец производства", callback_data="group_ProductionOwner")
group_b4 = types.InlineKeyboardButton(text=f"Маркетолог, HR, консультант и т.п.", callback_data="group_Marketing")
group_b5 = types.InlineKeyboardButton(text=f"Владелец бренда", callback_data="group_BrandOwner")
group_b6 = types.InlineKeyboardButton(text=f"Конструктор", callback_data="group_constructor")
group_b7 = types.InlineKeyboardButton(text=f"Байер", callback_data="group_bayer")
group_b8 = types.InlineKeyboardButton(text=f"Владелец бутика", callback_data="group_boutiqueOwner")
group_b9 = types.InlineKeyboardButton(text=f"Написать группу вручную", callback_data="group_write")
kb_group.add(group_b1,group_b2,group_b3,group_b4,group_b5,group_b6,group_b7,group_b8,group_b9)

kb_ready_networking = types.InlineKeyboardMarkup(row_width=1)
readyNetworking_b1 = types.InlineKeyboardButton(text=f"Поехали!", callback_data="readyNetworking")
kb_ready_networking.add(readyNetworking_b1)

kb_go_next1 = types.InlineKeyboardMarkup(row_width=1)
gonext_b1 = types.InlineKeyboardButton(text=f"👉 Ясно, продолжай🤓", callback_data="gonext1")
kb_go_next1.add(gonext_b1)

kb_go_next2 = types.InlineKeyboardMarkup(row_width=1)
gonext_b2 = types.InlineKeyboardButton(text=f"👉 Ок, жду понедельник👍", callback_data="gonext2")
kb_go_next2.add(gonext_b2)

kb_go_next3 = types.InlineKeyboardMarkup(row_width=1)
gonext_b3 = types.InlineKeyboardButton(text=f"👉 Продолжить", callback_data="gonext3")
kb_go_next3.add(gonext_b3)

kb_of_send_vack = types.InlineKeyboardMarkup(row_width=1)
sendVack_b1 = types.InlineKeyboardButton(text=f"В штат", callback_data="sendVack_shtat")
sendVack_b2 = types.InlineKeyboardButton(text=f"На проектную деятельность", callback_data="sendVack_project")
sendVack_b3 = types.InlineKeyboardButton(text=f"На разовую услугу", callback_data="sendVack_ones")
kb_of_send_vack.add(sendVack_b1,sendVack_b2,sendVack_b3)

kb_thankyou = types.InlineKeyboardMarkup(row_width=1)
thankyou_b1 = types.InlineKeyboardButton(text=f"Спасибо!", callback_data="thankyou")
kb_thankyou.add(thankyou_b1)

kb_greatmeropr = types.InlineKeyboardMarkup(row_width=1)
greatmeropr_b1 = types.InlineKeyboardButton(text=f"Круто, а мероприятия?", callback_data="greatmeropr")
kb_greatmeropr.add(greatmeropr_b1)

kb_greatgo = types.InlineKeyboardMarkup(row_width=1)
greatgo_b1 = types.InlineKeyboardButton(text=f"Как здорово, давай!", callback_data="greatgo")
kb_greatgo.add(greatgo_b1)

kb_stats = types.InlineKeyboardMarkup(row_width=1)
stats_b1 = types.InlineKeyboardButton(text=f"Кол-во пользователей", callback_data="stats_users")
stats_b2 = types.InlineKeyboardButton(text=f"Кол-во всего заходов", callback_data="stats_start")
stats_b3 = types.InlineKeyboardButton(text=f"Активация", callback_data="stats_activate")
stats_b4 = types.InlineKeyboardButton(text=f"Активность по специальностям", callback_data="stats_spec")
stats_b5 = types.InlineKeyboardButton(text=f"Отток пользователей", callback_data="stats_ottok")
kb_stats.add(stats_b1,stats_b2,stats_b3,stats_b4,stats_b5)
#for stat users
kb_time1 = types.InlineKeyboardMarkup(row_width=1)
time1_b1 = types.InlineKeyboardButton(text=f"День", callback_data="time1_today")
time1_b2 = types.InlineKeyboardButton(text=f"Неделя", callback_data="time1_week")
time1_b3 = types.InlineKeyboardButton(text=f"Месяц", callback_data="time1_mounth")
kb_time1.add(time1_b1,time1_b2,time1_b3)
#for stat start
kb_time2 = types.InlineKeyboardMarkup(row_width=1)
time2_b1 = types.InlineKeyboardButton(text=f"День", callback_data="time2_today")
time2_b2 = types.InlineKeyboardButton(text=f"Неделя", callback_data="time2_week")
time2_b3 = types.InlineKeyboardButton(text=f"Месяц", callback_data="time2_mounth")
kb_time2.add(time2_b1,time2_b2,time2_b3)
#for stat activation
kb_time3 = types.InlineKeyboardMarkup(row_width=1)
time3_b1 = types.InlineKeyboardButton(text=f"День", callback_data="time3_today")
time3_b2 = types.InlineKeyboardButton(text=f"Неделя", callback_data="time3_week")
time3_b3 = types.InlineKeyboardButton(text=f"Месяц", callback_data="time3_mounth")
kb_time3.add(time3_b1,time3_b2,time3_b3)
#for stat spec
kb_time4 = types.InlineKeyboardMarkup(row_width=1)
time4_b1 = types.InlineKeyboardButton(text=f"День", callback_data="time4_today")
time4_b2 = types.InlineKeyboardButton(text=f"Неделя", callback_data="time4_week")
time4_b3 = types.InlineKeyboardButton(text=f"Месяц", callback_data="time4_mounth")
kb_time4.add(time4_b1,time4_b2,time4_b3)
#back networking
kb_back1 = types.InlineKeyboardMarkup(row_width=1)
back1_b1 = types.InlineKeyboardButton(text=f"Назад", callback_data="back1_1")
kb_back1.add(back1_b1)

kb_back2 = types.InlineKeyboardMarkup(row_width=1)
back2_b2 = types.InlineKeyboardButton(text=f"Назад", callback_data="back2_1")
kb_back2.add(back2_b2)

kb_back3 = types.InlineKeyboardMarkup(row_width=1)
back3_b3 = types.InlineKeyboardButton(text=f"Назад", callback_data="back3_1")
kb_back3.add(back3_b3)

kb_back4 = types.InlineKeyboardMarkup(row_width=1)
back4_b4 = types.InlineKeyboardButton(text=f"Назад", callback_data="back4_1")
kb_back4.add(back4_b4)

# клава для админа разветвление написать всем юзерам лайк\диз или с получением ответа от юзера
kb_adminall = types.InlineKeyboardMarkup(row_width=1)
adminall_b1 = types.InlineKeyboardButton(text=f"Отправка новости с реакцией", callback_data="adminall_newslike")
adminall_b2 = types.InlineKeyboardButton(text=f"Отправка сообщения с вопросами", callback_data="adminall_quest")
kb_adminall.add(adminall_b1,adminall_b2)
# like and disslike
kb_like = types.InlineKeyboardMarkup(row_width=2)
like_b1 = types.InlineKeyboardButton(text=f"👍", callback_data="like_like")
like_b2 = types.InlineKeyboardButton(text=f"👎", callback_data="like_diss")
kb_like.add(like_b1,like_b2)
#for admin message to group by db
kb_groupbudb = types.InlineKeyboardMarkup(row_width=1)
groupbudb_b1 = types.InlineKeyboardButton(text=f"Не ушел в регистрацию", callback_data="groupbudb_reg")
groupbudb_b2 = types.InlineKeyboardButton(text=f"Не ушел в нетворкинг", callback_data="groupbudb_net")
groupbudb_b3 = types.InlineKeyboardButton(text=f"Не публикует вакансии", callback_data="groupbudb_vac")
groupbudb_b4 = types.InlineKeyboardButton(text=f"Не предлагает услуги", callback_data="groupbudb_uslugi")
groupbudb_b5 = types.InlineKeyboardButton(text=f"Не тыкал новости", callback_data="groupbudb_news")
kb_groupbudb.add(groupbudb_b1,groupbudb_b2,groupbudb_b3,groupbudb_b4,groupbudb_b5)





class Question(StatesGroup):
    q_from_user = State()

class Poshelania(StatesGroup):
    ans = State()

class Days2message(StatesGroup):
    impression = State()

class WhatIsFail(StatesGroup):
    fail = State()

class FindIspoln(StatesGroup):
    who = State()
    describe = State()

class My(StatesGroup):
    what = State()
    who = State()
    describe = State()
    link2 = State()
    price = State()

class User(StatesGroup):
    name = State()
    spec = State()
    soclink = State()
    city = State()
    company = State()
    role = State()
    clever = State()
    q_help = State()

class AdminNews(StatesGroup):
    who = State()
    img = State()
    text = State()

class AdminNewsLast(StatesGroup):
    img = State()
    text = State()

class AdminNewsBest(StatesGroup):
    img = State()
    text = State()


class AdminAvent(StatesGroup):
    img = State()
    text = State()
class AdminMessage(StatesGroup):
    call = State()
    mess = State()

class AdminMessageGroup(StatesGroup):
    group = State()
    mess = State()

class AdminMessageAll(StatesGroup):
    mess = State()

class FromAdmin(StatesGroup):
    message = State()
    toadminmess = State()

class ForGroupByDb(StatesGroup):
    message = State()

class IIbot(StatesGroup):
    start = State()
    message = State()

###about
async def about(message:types.Message):
    await bot.send_message(message.chat.id,f"Майя – виртуальный ассистент и помощник для представителей модного бизнеса, цель которого упростить рутинные и трудоемкие процессы. Ей можно доверить любую задачу в профессиональном контексте и быть уверенным в качестве ее выполнения.")

async def contacts(message:types.Message):
    await bot.send_message(message.chat.id,f"По вопросам сотрудничества, рекламы – @maya_mono")

######### admin open
async def admin(message:types.Message,state: FSMContext):
    await bot.send_message(message.chat.id,f"Ты в Админке!\nВыбирай и действуй по инструкции",reply_markup=kb_for_admin())

async def adminCall1(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "stats":
        await bot.send_message(callback.from_user.id,f"Выбери, что хочешь узнать? ",reply_markup=kb_stats)
    if str == "news":
        await bot.send_message(callback.from_user.id,f"Нажми на нужную тебе кнопку про группу пользователей",reply_markup=kb_group)
        await AdminNews.who.set()
    if str == "avent":
        await bot.send_message(callback.from_user.id, f"Отправь картинку")
        await AdminAvent.img.set()
    if str == "answer":
        await bot.send_message(callback.from_user.id, f"Отправь callback пользователя ( хранится в бд в таблице users в столбике call)")
        await AdminMessage.call.set()
    if str == "group":
        await bot.send_message(callback.from_user.id,
                               f"Какую группу пользователей? Дизайнер или Стилист или и т.д.")
        await AdminMessageGroup.group.set()
    if str == "all":
        await bot.send_message(callback.from_user.id,
                               f"Выбери что хочешь?",reply_markup=kb_adminall)
        # await AdminMessageAll.mess.set()

    if str == "delNews":
        cur.execute("DELETE from adminNews")
        base.commit()
        await bot.send_message(callback.from_user.id,
                               f"Все новости удалены!",reply_markup=kb_for_admin())

    if str == "delAvent":
        cur.execute("DELETE from adminAvent")
        base.commit()
        await bot.send_message(callback.from_user.id,
                               f"Все мероприятия удалены!", reply_markup=kb_for_admin())

    if str == "lastNews":
        await bot.send_message(callback.from_user.id,
                               f"Отправь текст Новости")
        await AdminNewsLast.text.set()
    if str == "bestNews":
        await bot.send_message(callback.from_user.id,
                               f"Отправь текст Новости")
        await AdminNewsBest.text.set()
    if str == "groupdb":
        await bot.send_message(callback.from_user.id,f"Выбери группу юзеров",reply_markup=kb_groupbudb)

# async def AdminLastNewsPhoto(message:types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data['img'] = message.photo[0].file_id
#     await bot.send_message(message.chat.id,f"Окей, теперь отправь текст новости")
#     await AdminNewsLast.text.set()



async def AdminLastNewsText(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await sql_add_adminNewsLast(state)
    await bot.send_message(message.chat.id, f"Новость добавлена", reply_markup=kb_for_admin())
    await state.finish()


async def AdminBestNewsText(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await sql_add_adminNewsBest(state)
    await bot.send_message(message.chat.id, f"Новость добавлена", reply_markup=kb_for_admin())
    await state.finish()


async def adminWhoButtonNews(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "stylist":
        async with state.proxy() as data:
            data['who'] = "Стилист"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()
    if str == "designer":
        async with state.proxy() as data:
            data['who'] = "Дизайнер"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()
    if str == "ProductionOwner":
        async with state.proxy() as data:
            data['who'] = "Владелец производства"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "Marketing":
        async with state.proxy() as data:
            data['who'] = "Маркетолог, HR, консультант и т.п."
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "BrandOwner":
        async with state.proxy() as data:
            data['who'] = "Владелец бренда"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "constructor":
        async with state.proxy() as data:
            data['who'] = "Конструктор"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "bayer":
        async with state.proxy() as data:
            data['who'] = "Байер"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "boutiqueOwner":
        async with state.proxy() as data:
            data['who'] = "Владелец бутика"
        await bot.send_message(callback.from_user.id, f"Окей, теперь отправь картинку новости")
        await AdminNews.img.set()

    if str == "write":
        await bot.send_message(callback.from_user.id, f"Напиши группу пользователей:")


async def adminWhoNews(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['who'] = message.text
    await bot.send_message(message.chat.id,f"Окей, теперь отправь картинку новости")
    await AdminNews.img.set()

async def adminPhotoNews(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['img'] = message.photo[0].file_id
    await bot.send_message(message.chat.id,f"Окей, теперь отправь текст новости")
    await AdminNews.text.set()

async def adminTextNews(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await sql_add_adminNews(state)
    await bot.send_message(message.chat.id, f"Новость добавлена",reply_markup=kb_for_admin())
    await state.finish()

async def adminPhotoAvent(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['img'] = message.photo[0].file_id
    await bot.send_message(message.chat.id,f"Окей, теперь отправь текст мероприятия")
    await AdminAvent.text.set()

async def adminTextAvent(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await sql_add_adminAvent(state)
    await bot.send_message(message.chat.id, f"Мероприятие добавлено",reply_markup=kb_for_admin())
    await state.finish()
callAdmin = 0
messAdmin = 0
async def adminCallMess(message:types.Message,state: FSMContext):
    global callAdmin
    global messAdmin
    async with state.proxy() as data:
        data['call'] = message.text
        callAdmin = data['call']
    await bot.send_message(message.chat.id, f"Окей, а теперь отправь текст пользователю. Сюда ты можешь написать больше сообщение и добавить , к примеру ссылку. После того, как ты напишешь, сообщение отправится пользователю!")
    await AdminMessage.mess.set()
async def adminTextMess(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['mess'] = message.text
        messAdmin = data['mess']
        try:
            await bot.send_message(data['call'], f"{messAdmin}")
            await bot.send_message(message.chat.id, f"Отправлено", reply_markup=kb_for_admin())
            await state.finish()
        except:
            await bot.send_message(message.chat.id, f"Увы, но юзер заблокировал бота...", reply_markup=kb_for_admin())
            cur.execute(f"DELETE FROM users WHERE call = {data['call']}")
            base.commit()
            await state.finish()


async def adminTextAll(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['mess'] = message.text
        allmess = data['mess']
    for (ret,) in cur.execute(f"SELECT call FROM users"):
        try:
            await bot.send_message(ret,f"{allmess}\n\nОставь реакцию!",reply_markup=kb_like)
        except:
            cur.execute(f"DELETE FROM users WHERE call = {ret}")
            base.commit()
            continue


    await bot.send_message(message.chat.id, f"Отправлено", reply_markup=kb_for_admin())
    await state.finish()

async def adminTextGroup(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await bot.send_message(message.chat.id, f"Теперь введи сообщение для этой группы:")
    await AdminMessageGroup.mess.set()

async def adminTextGroupMess(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['mess'] = message.text
    async with state.proxy() as data:
        for (ret,) in cur.execute(f"SELECT call FROM users WHERE spec = '{data['group']}'"):
            try:
                await bot.send_message(ret, f"{data['mess']}")
            except:
                cur.execute(f"DELETE FROM users WHERE call = {ret}")
                base.commit()
                continue

    await bot.send_message(message.chat.id, f"Отправлено", reply_markup=kb_for_admin())
    await state.finish()

async def adminall(callback:types.CallbackQuery,state:FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "newslike":
        await bot.send_message(callback.from_user.id,f"Отправь текст новости")
        await AdminMessageAll.mess.set()
    if str == "quest":
        await bot.send_message(callback.from_user.id,f"Отправь текст сообщения")
        await FromAdmin.message.set()

async def fromadmin(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text
        for (ret,) in cur.execute(f"SELECT call FROM users WHERE call != '{message.chat.id}'"):
        #for (ret,) in cur.execute(f"SELECT call FROM users"):
            try:
                await bot.send_message(ret,f"{data['message']}")
                await FromAdmin.toadminmess.set()
            except:
                continue

async def toadminmess(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['toadminmess'] = message.text
        mes = data['toadminmess']
        await bot.send_message(message.chat.id,f"Спасибо, что ответили!",reply_markup=kb_answer1)
        await bot.send_message(CHAT_ID,f"Data: {datetime.date.today()}\n\nCallback: {message.chat.id}\n\nLink: @{message.from_user.username}\n\nFrom Admin Message: {data['message']}\n\nMessage From User: {mes}")
    await state.finish()



#for admin like and diss

async def calllike(callback:types.CallbackQuery,state:FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "like":
        await state.finish()
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.from_user.id,f"Поняла!\nЧем могу помочь?",reply_markup=kb_answer1)
        await bot.send_message(CHAT_ID,f"Data: {datetime.date.today()}\n\nCallback: {callback.from_user.id}\n\nLink: @{callback.from_user.username}\n\nSet: 👍")
    if str == "diss":
        await state.finish()
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.from_user.id, f"Поняла!\nЧем могу помочь?", reply_markup=kb_answer1)
        await bot.send_message(CHAT_ID,
                               f"Data: {datetime.date.today()}\n\nCallback: {callback.from_user.id}\n\nLink: @{callback.from_user.username}\n\nSet: 👎")



async def groupbudb(callback:types.CallbackQuery,state:FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "reg":
        async with state.proxy() as data:
            data['group'] = "reg"
        await bot.send_message(callback.from_user.id,f"Напиши сообщение для отправки")
        await ForGroupByDb.message.set()
    if str == "net":
        async with state.proxy() as data:
            data['group'] = "net"
        await bot.send_message(callback.from_user.id, f"Напиши сообщение для отправки")
        await ForGroupByDb.message.set()
    if str == "vac":
        async with state.proxy() as data:
            data['group'] = "vac"
        await bot.send_message(callback.from_user.id, f"Напиши сообщение для отправки")
        await ForGroupByDb.message.set()
    if str == "uslugi":
        async with state.proxy() as data:
            data['group'] = "uslugi"
        await bot.send_message(callback.from_user.id, f"Напиши сообщение для отправки")
        await ForGroupByDb.message.set()
    if str == "news":
        async with state.proxy() as data:
            data['group'] = "news"
        await bot.send_message(callback.from_user.id, f"Напиши сообщение для отправки")
        await ForGroupByDb.message.set()

async def messageforgroupbydb(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text
        if data['group'] == "reg":
            for (ret,) in cur.execute(f"SELECT call FROM users WHERE name IS NULL OR spec IS NULL"):
                try:
                    await bot.send_message(ret, f"{data['message']}")
                except:
                    cur.execute(f"DELETE FROM users WHERE call = {ret}")
                    base.commit()
                    continue
        if data['group'] == "net":
            for (ret,) in cur.execute(f"SELECT call FROM for_network WHERE kolnetwork IS NULL"):
                try:
                    await bot.send_message(ret, f"{data['message']}")
                except:
                    cur.execute(f"DELETE FROM for_network WHERE call = {ret}")
                    base.commit()
                    continue
        if data['group'] == "vac":
            for (ret,) in cur.execute(f"SELECT call FROM for_network WHERE kolvac IS NULL"):
                try:
                    await bot.send_message(ret, f"{data['message']}")
                except:
                    cur.execute(f"DELETE FROM for_network WHERE call = {ret}")
                    base.commit()
                    continue
        if data['group'] == "uslugi":
            for (ret,) in cur.execute(f"SELECT call FROM users WHERE call NOT IN (SELECT call FROM myResume)"):
                try:
                    await bot.send_message(ret, f"{data['message']}")
                except:
                    cur.execute(f"DELETE FROM users WHERE call = {ret}")
                    base.commit()
                    continue
        if data['group'] == "news":
            for (ret,) in cur.execute(f"SELECT call FROM for_network WHERE kolnews IS NULL"):
                try:
                    await bot.send_message(ret, f"{data['message']}")
                except:
                    cur.execute(f"DELETE FROM for_network WHERE call = {ret}")
                    base.commit()
                    continue
    await bot.send_message(message.chat.id,f"Отправлено!",reply_markup=kb_for_admin())
    await state.finish()



#########admin close
async def start(message:types.Message,state: FSMContext):
    # lora_bot.user(message.chat.id,'ru')
    # lora_bot.message("/start",message.chat.id,'ru')
    reg = cur.execute(f"SELECT call FROM users WHERE call = {message.chat.id}").fetchone()
    base.commit()
    print(reg)
    if reg == None:

        cur.execute(f"INSERT INTO for_network(call) VALUES('{message.chat.id}')")
        base.commit()
        await User.name.set()
        await bot.send_message(message.chat.id,
                               f"Привет {emojize(':heart_exclamation:')}\nМеня зовут Майя, я - твой личный ассистент и помощник в мире модного бизнеса.\nДавай познакомимся и я расскажу, чем буду полезна.\n\nКак тебя зовут? Напиши свое имя и фамилию")
        star_start = cur.execute(f"SELECT call FROM statistic_start WHERE call = {message.chat.id}").fetchone()
        print(star_start)
        if star_start == None:
            dat = datetime.date.today()
            cur.execute(f"INSERT INTO statistic_start(datatime,call,kol) VALUES('{dat}','{message.chat.id}',1)")
            base.commit()
        else:
            (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = '{message.chat.id}'").fetchone()
            cur.execute(f"UPDATE statistic_start SET kol = kol + 1 WHERE call = '{message.chat.id}'")
            base.commit()
            cur.execute(f"UPDATE statistic_start SET spec = '{spec}' WHERE call = '{message.chat.id}'")
            base.commit()
    else:
        star_start = cur.execute(f"SELECT call FROM statistic_start WHERE call = {message.chat.id}").fetchone()
        print(star_start)
        if star_start == None:
            dat = datetime.date.today()
            cur.execute(f"INSERT INTO statistic_start(datatime,call,kol) VALUES('{dat}','{message.chat.id}',1)")
            base.commit()
        else:
            (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = '{message.chat.id}'").fetchone()
            cur.execute(f"UPDATE statistic_start SET kol = kol + 1 WHERE call = '{message.chat.id}'")
            base.commit()
            cur.execute(f"UPDATE statistic_start SET spec = '{spec}' WHERE call = '{message.chat.id}'")
            base.commit()
        cur.execute(f"UPDATE for_network SET call ='{message.chat.id}' WHERE call = '{message.chat.id}'")
        base.commit()
        await main(message)





async def name(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
    async with state.proxy() as data:
        data['call'] = message.chat.id

    async with state.proxy() as data:
        data['link'] = message.from_user.username

    async with state.proxy() as data:
        data['name'] = message.text
    await bot.send_message(message.chat.id,f"Какое у тебя направление деятельности?",reply_markup=kb_spec)
    await User.spec.set()

async def spec(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "stylist":
        async with state.proxy() as data:
            data['spec'] = "Стилист"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                              # f"Чем ты можешь быть полезен другим?")
    if str == "designer":
        async with state.proxy() as data:
            data['spec'] = "Дизайнер"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")
    if str == "ProductionOwner":
        async with state.proxy() as data:
            data['spec'] = "Владелец производства"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                              # f"Чем ты можешь быть полезен другим?")

    if str == "Marketing":
        async with state.proxy() as data:
            data['spec'] = "Маркетолог, HR, консультант и т.п."
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")

    if str == "BrandOwner":
        async with state.proxy() as data:
            data['spec'] = "Владелец бренда"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")

    if str == "constructor":
        async with state.proxy() as data:
            data['spec'] = "Конструктор"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")

    if str == "bayer":
        async with state.proxy() as data:
            data['spec'] = "Байер"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")

    if str == "boutiqueOwner":
        async with state.proxy() as data:
            data['spec'] = "Владелец бутика"
        await sql_add_command(state)
        await state.finish()
        await bot.send_message(callback.from_user.id,
                               f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                               reply_markup=kb_answer1)
        #await User.write_about.set()
        #await bot.send_message(callback.from_user.id,
                               #f"Чем ты можешь быть полезен другим?")

    if str == "MyAnswer":
        await bot.send_message(callback.from_user.id,f"Напиши свой тип деятельности:")

async def MySpec(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['spec'] = message.text
    await sql_add_command(state)
    await state.finish()
    await bot.send_message(message.chat.id,
                           f"Вот основные направления, по которым мы будем взаимодействовать.\n\nВ каждом из них тебя ждет инструкция.\n\nС чего начнем?",
                           reply_markup=kb_answer1)
    #await User.write_about.set()
    #await bot.send_message(message.chat.id,f"Чем ты можешь быть полезен другим?")

async def WriteAbout(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['write_about'] = message.text

    await bot.send_message(message.chat.id,
                           f"Отлично!\nИз какого ты города?")
    await User.city.set()

async def city(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        cur.execute(f"UPDATE users SET city = '{data['city']}' WHERE call = '{message.chat.id}'")
        base.commit()

    await bot.send_message(message.chat.id,
                           f"Пришли ссылку на свой профиль в любой соц. сети, где есть более подробная информация о тебе 👩‍🚀.\n\n\
Так вы в паре сможете лучше узнать друг о друге до встречи.")
    await User.soclink.set()

async def soclink(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['soclink'] = message.text
        cur.execute(f"UPDATE users SET soclink = '{data['soclink']}' WHERE call = '{message.chat.id}'")
        base.commit()

    await bot.send_message(message.chat.id,
                     f"В какой компании ты работаешь и какова твоя роль?\n\nНапиши название и ссылку. \n\
Если на себя/строишь свой бизнес – это тоже считается)")
    await User.company.set()

async def company(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['company'] = message.text
        cur.execute(f"UPDATE users SET company = '{data['company']}' WHERE call = '{message.chat.id}'")
        base.commit()

    await bot.send_message(message.chat.id,
                           f"Чем можешь быть полезен собеседнику?")
    await User.clever.set()

# async def role(message:types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data['role'] = message.text
#
#     await bot.send_message(message.chat.id,
#                            f"Расскажи о своем опыте в двух предложениях:")
#     await User.clever.set()

async def clever(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['clever'] = message.text
        cur.execute(f"UPDATE users SET clever = '{data['clever']}' WHERE call = '{message.chat.id}'")
        base.commit()
    await state.finish()
    await bot.send_message(message.chat.id,
                           f"Получилось! 🙌\nТеперь ты — участник встреч ☕ \nКраткая инструкция:\n\n\
1. Свою пару для встречи ты будешь узнавать каждый понедельник — сообщение придет в этот чат.\n\
Напиши партнеру в Telegram, чтобы договориться о встрече или звонке.\n\n\
Время и место вы выбираете сами.",reply_markup=kb_go_next1)

async def gonext1(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,
                           f"2. В конце недели я спрошу: участвуешь ли ты на следующей неделе и как прошла твоя предыдущая встреча. (В любой момент сможешь взять паузу)\n\n3. Пиши в этот чат https://t.me/maya_mono, если партнер не отвечает (я подберу тебе новую пару для встречи), а также если захочешь отказаться от участия во встречах или у тебя есть вопросы или предложения.", reply_markup=kb_go_next2)

async def gonext2(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,f"Хороших встреч! ☕\n\nПойдем дальше?",reply_markup=kb_answer1)

async def gonext3(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,f"Какого сотрудника ищем?",reply_markup=kb_of_send_vack)
    await FindIspoln.who.set()

async def sendVack(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "shtat":
        async with state.proxy() as data:
            data['who'] = "В штат, на постоянку"
        await bot.send_message(callback.from_user.id,f"Поняла! Напиши описание вакансии в формате:\n#направление_деятельности\nНазвание должности в «Название компании»\nРазмер вознаграждения\nОбязанности:\nТребования:\nУсловия:\nКонтакты для отклика:")
        await FindIspoln.describe.set()
    if str == "project":
        async with state.proxy() as data:
            data['who'] = "На проектную деятельность"
        await bot.send_message(callback.from_user.id, f"Поняла! Напиши описание вакансии в формате:\n#направление_деятельности\nНазвание должности в «Название компании»\nРазмер вознаграждения\nОбязанности:\nТребования:\nУсловия:\nКонтакты для отклика:")
        await FindIspoln.describe.set()
    if str == "ones":
        async with state.proxy() as data:
            data['who'] = "На разовую услугу"
        await bot.send_message(callback.from_user.id, f"Поняла! Напиши описание вакансии в формате:\n#направление_деятельности\nНазвание должности в «Название компании»\nРазмер вознаграждения\nОбязанности:\nТребования:\nУсловия:\nКонтакты для отклика:")
        await FindIspoln.describe.set()

async def describeispoln(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['describe'] = message.text
        sqlite_insert = """INSERT INTO findispoln(datatime,call,link,who,describe) VALUES(?,?,?,?,?)"""
        data_insert = (datetime.date.today(),message.chat.id,message.from_user.username, data['who'],data['describe'])
        cur.execute(sqlite_insert, data_insert)
        base.commit()
    await state.finish()
    await bot.send_message(message.chat.id,f"Отлично, уже ищу! Я сама проведу первые встречи для проверки компетенций и передам тебе только подходящих кандидатов.",reply_markup=kb_thankyou)



async def helpMe(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['q_help'] = message.text

    await bot.send_message(message.chat.id,
                           f"Это здорово! Ты всегда можешь доверить мне решение любого профессионального вопроса.\n\nСейчас можешь ознакомиться с другими функциями:",reply_markup=kb_answer1)

    await sql_add_command(state)
    await state.finish()

async def main(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Чем могу помочь?",
                           reply_markup=kb_answer1)






async def networking(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "networks":
        # (dat,) = cur.execute(f"SELECT datatime FROM users WHERE call = {callback.from_user.id}").fetchone()
        # print(dat)
        #if (datetime.date.today() - datetime.timedelta(days=7)) > datetime.datetime.strptime(dat,"%Y-%m-%d").date():
        # (kolnet,) = cur.execute(f"SELECT kolnetwork FROM for_network WHERE call = '{callback.from_user.id}'").fetchone()
        # base.commit()
        kolnet = cur.execute(
            f"SELECT kolnetwork FROM for_network WHERE call = '{callback.from_user.id}'").fetchone()
        base.commit()
        print(kolnet)
        if kolnet == (None,):
            cur.execute(
                f"UPDATE for_network SET kolnetwork = 1 WHERE call = '{callback.from_user.id}'")
            base.commit()
            await bot.send_message(callback.from_user.id,
                                   f"Предлагаю стать участником удобного формата для знакомств, обмена контактами и опытом с коллегами по цеху.\n\nКаждую неделю я буду предлагать тебе для встречи интересного человека, случайно выбранного из других участников. О времени и месте вы договариваетесь самостоятельно.\n\nДля начала ответь на несколько вопросов и прочитай короткую инструкцию.",
                                   reply_markup=kb_ready_networking)

        elif datetime.datetime.today().weekday() == 4: #0
            # cur.execute(f"UPDATE for_network SET try_connect = 'open' WHERE call = {callback.from_user.id}")
            # base.commit()
            await bot.send_message(callback.from_user.id,
                                   f"Знакомства в нашем бизнесе очень важны, поэтому я решила предложить всем деятелям модной индустрии гибкий и удобный формат.\n\n"
                                   f"{emojize(':recycling_symbol:')} Каждый понедельник я буду предлагать тебе для встречи интересного человека, случайно выбранного из других участников сообщества. О времени и месте вы договариваетесь самостоятельно.\n\n"
                                   f"{emojize(':check_mark_button:')} В конце недели я спрошу: участвуешь ли ты на следующей неделе и как прошла предыдущая встреча.\n\n"
                                   f"{emojize(':cross_mark_button:')} Если партнер не отвечает – просто напиши мне и я подберу другого человека. Отказаться от участия или взять паузу можно в любой момент.\n\n"
                                   f"Участвуешь?", reply_markup=kb_answer2)




        elif(datetime.datetime.today().weekday() != 4 and kolnet!=None):
            await bot.send_message(callback.from_user.id,
                                   f"Твоя пара на неделю станет известна в понедельник. Немного терпения 🤏",
                                   reply_markup=kb_answer1)
            # call = cur.execute(f"SELECT call FROM nextgo WHERE call = '{callback.from_user.id}'").fetchone()
            # print(f"cal == {call}")
            # if call == None:
            #     scheduler.add_job(message2days, "cron", day_of_week='thu', hour=19, minute=59,
            #                       args=(callback.from_user.id, dp,))
            #     await bot.send_message(callback.from_user.id,
            #                            f"Твоя пара на неделю станет известна в понедельник. Немного терпения 🤏",
            #                            reply_markup=kb_answer1)
            # else:

            # cur.execute(f"UPDATE for_network SET try_connect = 'close' WHERE call = {callback.from_user.id}")
            # base.commit()

        # con1 = cur.execute(f"SELECT try_connect FROM for_network WHERE call = {callback.from_user.id}").fetchone()
        # base.commit()
        # con = ''
        # if con1 == None:
        #     con = None
        #     cur.execute(f"UPDATE for_network SET kolnetwork = 0 WHERE call = {callback.from_user.id}")
        #     base.commit()
        #
        # else:
        #     (con,) = con1
        #
        # if con == None or con == "open":
        #
        #     await bot.send_message(callback.from_user.id,
        #                            f"Знакомства в нашем бизнесе очень важны, поэтому я решила предложить всем деятелям модной индустрии гибкий и удобный формат.\n\n"
        #                            f"{emojize(':recycling_symbol:')} Каждый понедельник я буду предлагать тебе для встречи интересного человека, случайно выбранного из других участников сообщества. О времени и месте вы договариваетесь самостоятельно.\n\n"
        #                            f"{emojize(':check_mark_button:')} В конце недели я спрошу: участвуешь ли ты на следующей неделе и как прошла предыдущая встреча.\n\n"
        #                            f"{emojize(':cross_mark_button:')} Если партнер не отвечает – просто напиши мне и я подберу другого человека. Отказаться от участия или взять паузу можно в любой момент.\n\n"
        #                            f"Участвуешь?", reply_markup=kb_answer2)
        #     cur.execute(f"UPDATE users SET datatime = '{datetime.date.today()}' WHERE call = {callback.from_user.id}")
        #     base.commit()
        # if con == "close":
        #     await bot.send_message(callback.from_user.id,f"В неделю доступна только одна встреча. Дождись следующего понедельника",reply_markup=kb_answer1)


    if str == "news":
        call = cur.execute(f"SELECT call FROM for_network WHERE call = '{callback.from_user.id}'").fetchone()
        base.commit()
        if call == None:
            cur.execute(f"INSERT INTO for_network(call) VALUES('{callback.from_user.id}')")
            base.commit()
        (kolnews,) = cur.execute(f"SELECT kolnews FROM for_network WHERE CALL = '{callback.from_user.id}'").fetchone()
        base.commit()
        print(kolnews)
        if kolnews == None:
            await bot.send_message(callback.from_user.id,
                                   f"Хорошие новости ✨\n\nТеперь ты можешь отписаться от десятков профессиональных телеграм каналов, которые ты не успеваешь разбирать, и ни одна новость не пройдет мимо тебя, обещаю❗\n\n\
Я обрабатываю более 100 экспертных и новостных источников информации, сортирую их на основе специальностей, опыта и присылаю персональные подборки раз в день, неделю и месяц с основными мыслями и тезисами.\n\n\
Больше никакого стресса и завалов в мессенджере, только удовольствие и релевантная информация 😌",
                                   reply_markup=kb_greatmeropr)
            cur.execute(f"UPDATE for_network SET kolnews = 1 WHERE call = '{callback.from_user.id}'")
            base.commit()
        else:
            non = cur.execute(f"SELECT call FROM poshelania WHERE call = {callback.from_user.id}").fetchone()
            base.commit()
            if non == None:
                await bot.send_message(callback.from_user.id,
                                       f"Расскажи, какие новости и мероприятия в профессиональном контексте тебе интересны?")
                await Poshelania.ans.set()
            else:
                await bot.send_message(callback.from_user.id,
                                       f"Что хочется посмотреть?",
                                       reply_markup=kb_parser)





    if str == "ispoln":
        call = cur.execute(f"SELECT call FROM for_network WHERE CALL = '{callback.from_user.id}'").fetchone()
        base.commit()
        if call == None:
            cur.execute(f"INSERT INTO for_network(call) VALUES('{callback.from_user.id}')")
            base.commit()
        (kolvac,) = cur.execute(f"SELECT kolvac FROM for_network WHERE CALL = '{callback.from_user.id}'").fetchone()
        base.commit()
        print(kolvac)
        if kolvac == None:
            await bot.send_message(callback.from_user.id,f"Здесь ты можешь разместить вакансию для поиска исполнителя любого профиля. Я помогу найти подходящего сотрудника в штат, на проектную деятельность или разовую услугу.",reply_markup=kb_go_next3)
            cur.execute(f"UPDATE for_network SET kolvac = 1 WHERE call = '{callback.from_user.id}'")
            base.commit()
        else:
            await bot.send_message(callback.from_user.id, f"Какого сотрудника ищем?", reply_markup=kb_of_send_vack)
            await FindIspoln.who.set()

    if str == "my":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, какие услуги ты предоставляешь?")
        await My.what.set()

    if str == "helpme":
        (name,) = cur.execute(f"SELECT name FROM users WHERE call = '{callback.from_user.id}'").fetchone()
        base.commit()
        call = cur.execute(f"SELECT call FROM for_network WHERE CALL = '{callback.from_user.id}'").fetchone()
        base.commit()
        if call == None:
            cur.execute(f"INSERT INTO for_network(call) VALUES('{callback.from_user.id}')")
            base.commit()
        (kolhelp,) = cur.execute(f"SELECT kolhelp FROM for_network WHERE CALL = '{callback.from_user.id}'").fetchone()
        base.commit()
        print(kolhelp)
        if kolhelp == None:
            await bot.send_message(callback.from_user.id,
                                   f"Привет, {name}!\n\
Здесь ты можешь написать любой запрос, с которым тебе нужна помощь. Это может быть все, что связанно с профессиональной деятельностью, например:\n\
– Найти проверенное производство;\n\
– Найти стилиста для съемки;\n\
– Найти поставщика материалов;\n\
– и так далее.\nА я оперативно постараюсь помочь тебе с этим. Попробуем?",reply_markup=kb_helpMaya)
            cur.execute(f"UPDATE for_network SET kolhelp = 1 WHERE call = '{callback.from_user.id}'")
            base.commit()
        else:
            await bot.send_message(callback.from_user.id,f"Есть вопрос?",reply_markup=kb_helpMaya)

    if str == "AI":
        user = cur.execute(f"SELECT call FROM botGPT WHERE call = '{callback.from_user.id}'").fetchone() #None
        print(user)
        if user == None:
            sqlite_insert = """INSERT INTO botGPT(datatime,call,link,kol,dostup) VALUES(?,?,?,?,?)"""
            data_insert = (
                datetime.date.today(), callback.from_user.id, callback.from_user.username, 5,'test')
            cur.execute(sqlite_insert, data_insert)
            base.commit()
            await bot.send_message(callback.from_user.id,
                                   f"Здесь ты можешь задавать вопросы искуственному интеллекту!\n\n"
                                   f"– 5 запросов в день бесплатно\n– 20 запросов в день 349 руб/мес\n– 50 запросов в день 649 руб/мес\n– ∞ число запросов с день 1490 руб/мес\n\nНачинай прямо сейчас!\n\nУчти, что интеллект развивается и "
                                       f"может быть сильно загружен или долго отвечать. Для того, чтобы вернуться назад - нажми на /stop\n\nЗадай вопрос:")
            await IIbot.start.set()
        else:
            (dostup,) = cur.execute(f"SELECT dostup FROM botGPT WHERE call = '{callback.from_user.id}'").fetchone()
            if dostup == "test":
                (kol,) = cur.execute(f"SELECT kol FROM botGPT WHERE call = '{callback.from_user.id}'").fetchone()
                if int(kol) <= 0:
                    await bot.send_message(callback.from_user.id,f"Твое количество запросов на сегодня закончилось :(\n– 5 запросов в день бесплатно\n– 20 запросов в день 349 руб/мес\n– 50 запросов в день 649 руб/мес\n– ∞ число запросов с день 1490 руб/мес\n\nЗавтра твой доступ обновится согласно тарифу!\n\nДля того, чтобы увеличить количество запросов - обратись в поддержку - @maya_mono",reply_markup=kb_answer1)
                else:
                    await bot.send_message(callback.from_user.id,
                                           f"Здесь ты можешь задавать вопросы искуственному интеллекту!\n\nНачинай прямо сейчас!\n\nУчти, что интеллект развивается и "
                                       f"может быть сильно загружен или долго отвечать. Для того, чтобы вернуться назад - нажми на /stop\n\nЗадай вопрос:")
                    await IIbot.start.set()
            if dostup == "min":
                (kol,) = cur.execute(f"SELECT kol FROM botGPT WHERE call = '{callback.from_user.id}'").fetchone()
                if int(kol) <= 0:
                    await bot.send_message(callback.from_user.id,
                                           f"Твое количество запросов на сегодня закончилось :(\n– 5 запросов в день бесплатно\n– 20 запросов в день 349 руб/мес\n– 50 запросов в день 649 руб/мес\n– ∞ число запросов с день 1490 руб/мес\n\nЗавтра твой доступ обновится согласно тарифу!\n\nДля того, чтобы увеличить количество запросов - обратись в поддержку - @maya_mono",
                                           reply_markup=kb_answer1)
                else:
                    await bot.send_message(callback.from_user.id,
                                           f"Здесь ты можешь задавать вопросы искуственному интеллекту!\n\nНачинай прямо сейчас!\n\nУчти, что интеллект развивается и "
                                       f"может быть сильно загружен или долго отвечать. Для того, чтобы вернуться назад - нажми на /stop\n\nЗадай вопрос:")
                    await IIbot.start.set()
            if dostup == "med":
                (kol,) = cur.execute(f"SELECT kol FROM botGPT WHERE call = '{callback.from_user.id}'").fetchone()
                if int(kol) <= 0:
                    await bot.send_message(callback.from_user.id,
                                           f"Твое количество запросов на сегодня закончилось :(\n– 5 запросов в день бесплатно\n– 20 запросов в день 349 руб/мес\n– 50 запросов в день 649 руб/мес\n– ∞ число запросов с день 1490 руб/мес\n\nЗавтра твой доступ обновится согласно тарифу!\n\nДля того, чтобы увеличить количество запросов - обратись в поддержку - @maya_mono",
                                           reply_markup=kb_answer1)
                else:
                    await bot.send_message(callback.from_user.id,
                                           f"Здесь ты можешь задавать вопросы искуственному интеллекту!\n\nНачинай прямо сейчас!\n\nУчти, что интеллект развивается и "
                                       f"может быть сильно загружен или долго отвечать. Для того, чтобы вернуться назад - нажми на /stop\n\nЗадай вопрос:")
                    await IIbot.start.set()
            if dostup == "max":
                await bot.send_message(callback.from_user.id,
                                       f"Здесь ты можешь задавать вопросы искуственному интеллекту!\n\nНачинай прямо сейчас!\n\nУчти, что интеллект развивается и "
                                       f"может быть сильно загружен или долго отвечать. Для того, чтобы вернуться назад - нажми на /stop\n\nЗадай вопрос:")
                await IIbot.start.set()










async def readyNetworking(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,
                           f"Из какого ты города? {emojize(':cityscape:')}\n\n\
Вы с партнером можете оказаться в разных городах – тогда вам подойдет онлайн формат встречи 👨‍💻\n\n\
Если вы из одного города – сможете встретиться вживую 🤝",reply_markup=kb_back1)
    await User.city.set()


async def poshelaniaMessage(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
        data['call'] = message.chat.id
        data['poshelania'] = message.text
        data['link'] = message.from_user.url

    await bot.send_message(message.chat.id,
                           f"Поняла, спасибо! С чего начнем?",reply_markup=kb_parser)
    await sql_add_poshelania(state)
    await state.finish()




async def networkingAnswer(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "question":
        await bot.send_message(callback.from_user.id,
                               f"Напиши его сюда:")
        await Question.q_from_user.set()
    if str == "yes":
        # (name,) = cur.execute(f'SELECT name FROM users  WHERE call != "{callback.from_user.id}" ORDER BY RANDOM() LIMIT 1;').fetchone()
        # base.commit()
        # print(name)
        # (namecity,) = cur.execute(f'SELECT city FROM users WHERE name = "{name}"').fetchone()
        # (companyname,) = cur.execute(f'SELECT company FROM users WHERE name = "{name}"').fetchone()
        # (rolename,) = cur.execute(f'SELECT spec FROM users WHERE name = "{name}"').fetchone()
        # (aboutname,) = cur.execute(f'SELECT clever FROM users WHERE name = "{name}"').fetchone()
        # (link,) = cur.execute(f'SELECT link FROM users WHERE name = "{name}" ').fetchone()
        # print(link)
        # base.commit()

        #await bot.send_message(callback.from_user.id, f"Твоя пара на эту неделю:\n\n{name} - ({namecity})\nПрофиль - @{link}\nКомпания: {companyname}\nДолжность: {rolename}\nЧем может быть полезен партнер: {aboutname}\n\nНапиши собеседнику в Telegram – @{link}\nНе откладывай, договорись о встрече сразу 🙂 \n\nБудут вопросы, пиши в ответ.",reply_markup=kb_answer3)
        # scheduler.add_job(messageformonday, "cron", day_of_week='fri',hour=12,minute=30, args=(callback.from_user.id, dp,))
        await bot.send_message(callback.from_user.id,f"Отлично! Жди от меня сообщения в понедельник!",reply_markup=kb_answer1)





async def networkingMessage(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
        data['call'] = message.chat.id
        data['link'] = message.from_user.username
        data['name'] = message.text
        await bot.send_message(CHAT_ID,f"Data: {data['datatime']}\n\nCallback: {data['call']}\n\nLink: @{data['link']}\n\nQuestion: {data['name']}")
    await bot.send_message(message.chat.id,f"Поняла, уже решаю. Скоро вернусь с результатом")
    await sql_add_q(state)
    await main(message)
    await state.finish()

# async def message2days(callback,dp:Dispatcher):
#     await bot.send_message(callback,f"Привет!👋\n\n\
# Наши онлайн встречи продолжаются.\n\n\
# Участвуешь на следующей неделе?",reply_markup=kb_days2answer1)


# async def days2answer1(callback:types.CallbackQuery):
#     await bot.answer_callback_query(callback.id)
#     str = callback.data.split("_")[1]
#     if str == "yes":
#         await bot.send_message(callback.from_user.id, f"Расскажи о своих впечатлениях! Как все прошло?")
#         await Days2message.impression.set()
#     if str == "no":
#         await bot.send_message(callback.from_user.id,
#                                f"Почему?",reply_markup=kb_days2answer2) .

async def days2answer1(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id, f"Отлично! Учавствуешь на следующей недели?",reply_markup=kb_days2answer3)

    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Поняла :( \n\nПочему?",reply_markup=kb_days2answer2)

async def impression(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
        data['call'] = message.chat.id
        data['impression'] = message.text
        data['link'] = message.from_user.url
    await bot.send_message(message.chat.id,
                           f"Спасибо! Участвуешь на следующей неделе?",
                           reply_markup=kb_days2answer3)
    await sql_add_impression(state)
    await state.finish()

async def days2answer3(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        call = cur.execute(f"SELECT call FROM nextgo WHERE call = '{callback.from_user.id}'").fetchone()
        print(f"cal == {call}")
        if call == None:
            sqlite_insert = """INSERT INTO nextgo(datatime,call,name,answer) VALUES(?,?,?,?)"""
            data_insert = (
                datetime.date.today(), callback.from_user.id, callback.from_user.username, 1)
            cur.execute(sqlite_insert, data_insert)
            base.commit()
            await bot.send_message(callback.from_user.id, f"Отлично! Жди понедельника :)", reply_markup=kb_answer1)
            # scheduler.add_job(messageformonday, "cron", day_of_week='mon', hour=10, minute=30,
            #                   args=(callback.from_user.id, dp,))
        else:
            cur.execute(f"UPDATE nextgo SET answer = 1 WHERE call = '{callback.from_user.id}'")
            base.commit()
            await bot.send_message(callback.from_user.id, f"Отлично! Жди понедельника :)", reply_markup=kb_answer1)
            # scheduler.add_job(messageformonday, "cron", day_of_week='mon', hour=10, minute=30,
            #                   args=(callback.from_user.id, dp,))


        # (name,) = cur.execute(
        #     f'SELECT name FROM users  WHERE call != "{callback.from_user.id}" ORDER BY RANDOM() LIMIT 1;').fetchone()
        # base.commit()
        # print(name)
        # (link,) = cur.execute(f'SELECT link FROM users WHERE name = "{name}" ').fetchone()
        # print(link)
        # base.commit()
        # await bot.send_message(callback.from_user.id,
        #                        f"Твой собеседник на неделю: *{name}*\nСсылка - {link}\nГотов начать?",
        #                        reply_markup=kb_answer3)

    if str == "pause":
        call = cur.execute(f"SELECT call FROM nextgo WHERE call = '{callback.from_user.id}'").fetchone()
        print(f"cal == {call}")
        if call == None:
            sqlite_insert = """INSERT INTO nextgo(datatime,call,name,answer) VALUES(?,?,?,?)"""
            data_insert = (
                datetime.date.today(), callback.from_user.id, callback.from_user.username, 0)
            cur.execute(sqlite_insert, data_insert)
            base.commit()
            await bot.send_message(callback.from_user.id,
                                   f"Поняла :( Я спрошу еще раз на следующей неделе!", reply_markup=kb_answer1)
            # scheduler.add_job(message2days, "cron", day_of_week='fri', hour=12, minute=30,
            #                   args=(callback.from_user.id, dp,))

        else:
            cur.execute(f"UPDATE nextgo SET answer = 0 WHERE call = '{callback.from_user.id}'")
            base.commit()
            await bot.send_message(callback.from_user.id,
                                   f"Поняла :( Я спрошу еще раз на следующей неделе!", reply_markup=kb_answer1)
            # cheduler.add_job(message2days, "cron", day_of_week='fri', hour=12, minute=30,
            #                  args=(callback.from_user.id, dp,))



async def days2answer2(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,f"Спасибо, я поняла. Учавствуешь на следующей неделе?",reply_markup=kb_days2answer3)

async def networkingAnswer3(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "question":
        await bot.send_message(callback.from_user.id,
                               f"Напиши его сюда:")
        await Question.q_from_user.set()
    if str == "yes":
        await bot.send_message(callback.from_user.id,f"Удачи на встрече! Расскажи потом, как все прошло :)\nА пока что давай я помогу тебе с другими задачами?",reply_markup = kb_answer1)

        #scheduler.add_job(message2days, "interval",days = 2,args = (callback.from_user.id,dp,))
        #scheduler.add_job(message2days, "cron", day_of_week='thu',hour=19,minute=59, args=(callback.from_user.id, dp,))
        # user = cur.execute(f"SELECT call FROM for_network WHERE call = {callback.from_user.id}").fetchone()
        # print(user)
        # if user == None:
        #     cur.execute(f"INSERT INTO for_network(call,try_connect) VALUES({callback.from_user.id},'close')")
        #     base.commit()



async def parserButton(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "news":
        await bot.send_message(callback.from_user.id,f"Вот что я собрала для тебя:",reply_markup=kb_dop_parser(callback.from_user.id))
    if str == "meropri":
        for ret in cur.execute("SELECT img,text FROM adminAvent"):
            await bot.send_photo(callback.from_user.id, ret[0], f"\n{ret[1]}\n\nЧтобы вернуться назад нажми /start")

k = 1
async def dopParserButton(callback:types.CallbackQuery):
    global k
    k = 1
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "news":
        (count,)= cur.execute(f"SELECT count(text) FROM adminNewsBest").fetchone()
        base.commit()
        print("count news== ",count)
        if count == 1:
            for ret in cur.execute(f"SELECT img,text FROM adminNewsLast WHERE id = 1"):
                # await bot.send_photo(callback.from_user.id, ret[0],
                #                      f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start")
                await bot.send_message(callback.from_user.id,
                                     f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start")

        else:
            for ret in cur.execute(f"SELECT img,text FROM adminNewsLast WHERE id = 1"):
                # await bot.send_photo(callback.from_user.id, ret[0],
                #                      f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start",
                #                      reply_markup=kb_answer4)
                await bot.send_message(callback.from_user.id,
                                     f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start",reply_markup=kb_answer4)

    if str == "meropri":
        (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = '{callback.from_user.id}'").fetchone()
        print(spec)
        (minid,) = cur.execute(f"SELECT min(id) FROM adminNews WHERE who = '{spec}'").fetchone()
        for ret in cur.execute(f"SELECT img,text FROM adminNews WHERE who ='{spec}' AND id = {minid}"):
            await bot.send_photo(callback.from_user.id,ret[0],f"\n{ret[1]}")

    if str == "mounth":
        (count,) = cur.execute(f"SELECT count(text) FROM adminNewsBest").fetchone()
        base.commit()
        print("count mounth== ", count)
        if count == 1:
            for ret in cur.execute("SELECT img,text FROM adminNewsBest WHERE id = 1"):
                # await bot.send_photo(callback.from_user.id, ret[0],
                #                      f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start")
                await bot.send_message(callback.from_user.id,
                                     f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start")
        else:
            for ret in cur.execute("SELECT img,text FROM adminNewsBest WHERE id = 1"):
                # await bot.send_photo(callback.from_user.id, ret[0],
                #                      f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start",
                #                      reply_markup=kb_answer7)
                await bot.send_message(callback.from_user.id,
                                     f"\n{ret[1]}\n\nДля того, чтобы вернуться в начало - нажмите /start",reply_markup=kb_answer7)



async def Answer4(callback:types.CallbackQuery,state: FSMContext):
    global k
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,
                               f"Есть пожелания, как улучшить подборку?",
                               reply_markup=kb_answer5)

    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, что не так?")
        await WhatIsFail.fail.set()

    if str == "more":
        k+=1
        some = cur.execute(f"SELECT id FROM adminNewsLast WHERE id = {k}").fetchone()
        if some == None:
            k = 1
        for ret in cur.execute(f"SELECT img,text FROM adminNewsLast WHERE id = {k}"):
            # await bot.send_photo(callback.from_user.id, ret[0], f"\n{ret[1]}", reply_markup=kb_answer4)
            await bot.send_message(callback.from_user.id, f"\n{ret[1]}", reply_markup=kb_answer4)

async def Answer6(callback:types.CallbackQuery,state: FSMContext):
    global k
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,
                               f"Есть пожелания, как улучшить подборку?",
                               reply_markup=kb_answer5)

    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, что не так?")

        await WhatIsFail.fail.set()
    if str == "more":
        global n
        n+=1


        (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = '{callback.from_user.id}'").fetchone()
        print(spec)
        (k,) = cur.execute(f"SELECT min(id) FROM adminNews WHERE who = '{spec}'").fetchone()

        some = cur.execute(f"SELECT id FROM adminNews WHERE id = {k + n}").fetchone()

        if some == None:
            (k,) = cur.execute(f"SELECT min(id) FROM adminNews WHERE who = '{spec}'").fetchone()
            n = 0
        (spec,) = cur.execute(f"SELECT spec FROM users WHERE call = '{callback.from_user.id}'").fetchone()
        for ret in cur.execute(f"SELECT img,text FROM adminNews WHERE id = {k} AND who = '{spec}'"):
            await bot.send_photo(callback.from_user.id, ret[0], f"\n{ret[1]}", reply_markup=kb_answer6)

async def Answer7(callback:types.CallbackQuery,state: FSMContext):
    global k
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,
                               f"Есть пожелания, как улучшить подборку?",
                               reply_markup=kb_answer5)

    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, что не так?")
        await WhatIsFail.fail.set()

    if str == "more":
        k+=1
        some = cur.execute(f"SELECT id FROM adminNewsBest WHERE id = {k}").fetchone()
        if some == None:
            k = 1
        for ret in cur.execute(f"SELECT img,text FROM adminNewsBest WHERE id = {k}"):
            #await bot.send_photo(callback.from_user.id, ret[0], f"\n{ret[1]}", reply_markup=kb_answer7)
            await bot.send_message(callback.from_user.id, f"\n{ret[1]}", reply_markup=kb_answer7)

async def Answer8(callback:types.CallbackQuery,state: FSMContext):
    global k
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,
                               f"Есть пожелания, как улучшить подборку?",
                               reply_markup=kb_answer5)

    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, что не так?")
        await WhatIsFail.fail.set()

    if str == "more":
        k+=1
        some = cur.execute(f"SELECT id FROM adminAvent WHERE id = {k}").fetchone()
        if some == None:
            k = 1
        for ret in cur.execute(f"SELECT img,text FROM adminAvent WHERE id = {k}"):
            await bot.send_photo(callback.from_user.id, ret[0], f"\n{ret[1]}", reply_markup=kb_answer8)

async def whatIsFail(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
        data['call'] = message.chat.id
        data['link'] = message.from_user.url
        data['name'] = message.text

    await bot.send_message(message.chat.id,
                           f"Спасибо! Я стану лучше!")
    await sql_add_fail(state)
    await state.finish()
    await main(message)

async def Answer5(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,
                               f"Расскажи, что не так?")
        await WhatIsFail.fail.set()
    if str == "no":
        await bot.send_message(callback.from_user.id,
                               f"Спасибо, я стараюсь!")
        await bot.send_message(callback.from_user.id,
                               f"Чем могу помочь?",
                               reply_markup=kb_answer1)
#### 3 punct
# async def ispoln(message:types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data['datatime'] = datetime.date.today()
#         data['call'] = message.chat.id
#         data['link'] = message.from_user.url
#         data['who'] = message.text
#
#     await bot.send_message(message.chat.id,f"Какие сроки и бюджет?")
#     await FindIspoln.srok.set()

# async def srok(message:types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data['srok'] = message.text
#
#     await bot.send_message(message.chat.id,f"Спасибо, поняла! В ближайшее время пришлю рекомендации по исполнителям. У тебя остались вопросы?",reply_markup=kb_answer5)
#     await sql_add_ispoln(state)
#     await state.finish()
    # await main(message)
###4 punct

async def MyWhat(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['datatime'] = datetime.date.today()
        data['call'] = message.chat.id
        data['link'] = message.from_user.url
        data['what'] = message.text
    await bot.send_message(message.chat.id,f"Кому они могут быть полезны?")
    await My.who.set()

async def MyWho(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['who'] = message.text
    await bot.send_message(message.chat.id,
                           f"Опиши свой опыт в этой сфере?")
    await My.describe.set()

async def MyDescribe(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['describe'] = message.text
    await bot.send_message(message.chat.id,
                           f"Прикрепи ссылку на свое резюме/сайт:")
    await My.link2.set()

async def MyLink(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['link2'] = message.text

    await bot.send_message(message.chat.id,
                           f"Сколько стоят твои услуги?")
    await My.price.set()


async def MyPrice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await bot.send_message(message.chat.id,
                           f"Отлично! Я покажу твой профиль тем, кто будет интересоваться этими услугами.\nА пока вернемся в главное меню",reply_markup=kb_answer1)

    await sql_add_MyResume(state)
    await state.finish()

async def thankyou(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,f"Чем могу помочь?",reply_markup=kb_answer1)

async def greatmeropr(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,f"По такому же принципу я буду предлагать тебе релевантные и тематические встречи в твоем городе и онлайн формате.\n\n На понравившиеся – зарегистрирую и пришлю билет в этот же чатик 🎟",reply_markup=kb_greatgo)

async def greatgo(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id,
                           f"Договорились, пойдем смотреть следующие функции?",
                           reply_markup=kb_answer1)

async def helpMaya(callback:types.CallbackQuery,state: FSMContext):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "yes":
        await bot.send_message(callback.from_user.id,f"С чем нужна помощь?")
        await Question.q_from_user.set()
    if str == "no":
        await bot.send_message(callback.from_user.id,f"Приходи, когда появится! С удовольствием помогу",reply_markup=kb_answer1)

#user_analytics = {}

# async def lora(message:types.Message):
    # user_analytics[message.from_user.id] = {}
    # user_analytics[message.from_user.id]['start_date'] = datetime.date.today()
    # user_analytics[message.from_user.id]['end_date'] = datetime.date.today()
    #lora_bot.user(message.chat.id,"5454478500:AAEE7tWJYsdMbP7tFpMT-ktMW-wcH3Zpios")
    # #info = lora_bot.analyze_total(datetime.date.today(), datetime.date.today())
    # #await bot.send_message(message.chat.id, info,reply_markup=analytics_markup)
    # #photo, info = lora_bot.analyze_dau(datetime.date.today(), datetime.date.today())
    # #bot.send_message(message.chat.id, info)
    # #await bot.send_photo(message.chat.id, photo,info)
    # # Возвращает информацию о ежедневных активных пользователях(график + текст)
    # photo, info= lora_bot.analyze_new_user(None,None) #varchar разобраться поэксперементировать
    # print(info)
    # await bot.send_message(message.chat.id, info)
    # # buffer = io.BytesIO()
    # # photo.save(buffer, format='JPEG',quality=75)
    # # photo = buffer.getbuffer()
    # #mg_byte_arr = img_byte_arr.getvalue()
    # #photo = anvil.BlobMedia(content_type="image/jpeg", content=img_byte_arr)
    # await bot.send_photo(message.chat.id, photo)
    #
    # photo, info = lora_bot.analyze_dau(None,None)
    # await bot.send_message(message.chat.id, info)
    # await bot.send_photo(message.chat.id, photo)

# async def message2days(callback,dp:Dispatcher):
#     await bot.send_message(callback,f"Привет!👋\n\n\
# Наши онлайн встречи продолжаются.\n\n\
# Участвуешь на следующей неделе?",reply_markup=kb_days2answer1)


# async def days2answer1(callback:types.CallbackQuery):
#     await bot.answer_callback_query(callback.id)
#     str = callback.data.split("_")[1]
#     if str == "yes":
#         await bot.send_message(callback.from_user.id, f"Расскажи о своих впечатлениях! Как все прошло?")
#         await Days2message.impression.set()
#     if str == "no":
#         await bot.send_message(callback.from_user.id,
#                                f"Почему?",reply_markup=kb_days2answer2)
async def message2days():
    for (ret,) in cur.execute(f"SELECT call FROM users WHERE clever != 'NULL'"):
        try:
            await bot.send_message(ret,f"Привет! Участвуешь на следующей неделе в нетворкинге?",reply_markup=kb_days2answer3)
        except:
            cur.execute(f"DELETE FROM users WHERE call = {ret}")
            base.commit()
            continue


async def messageformonday():
    mass = []
    for (ret,) in cur.execute(f"SELECT call FROM nextgo WHERE answer = 1"):
        mass.append(ret)
    print(mass)
    for i in mass:
        (name,) = cur.execute(
            f'SELECT name FROM users  WHERE call != "{i}" ORDER BY RANDOM()').fetchone()
        base.commit()
        print(name)
        (namecity,) = cur.execute(f'SELECT city FROM users WHERE name = "{name}"').fetchone()
        (companyname,) = cur.execute(f'SELECT company FROM users WHERE name = "{name}"').fetchone()
        (rolename,) = cur.execute(f'SELECT spec FROM users WHERE name = "{name}"').fetchone()
        (aboutname,) = cur.execute(f'SELECT clever FROM users WHERE name = "{name}"').fetchone()
        (link,) = cur.execute(f'SELECT link FROM users WHERE name = "{name}" ').fetchone()
        print(link)
        base.commit()
        try:
            await bot.send_message(i,
                                f"Твоя пара на эту неделю:\n\n{name} - ({namecity})\nПрофиль - @{link}\nКомпания: {companyname}\nДолжность: {rolename}\nЧем может быть полезен партнер: {aboutname}\n\nНапиши собеседнику в Telegram – @{link}\nНе откладывай, договорись о встрече сразу 🙂 \n\nБудут вопросы, пиши в ответ.",
                                reply_markup=kb_answer3)
        except:
            continue

async def updateBotGPT():
    cur.execute(f"UPDATE botGPT SET kol = 5 WHERE dostup = 'test'")
    base.commit()
    cur.execute(f"UPDATE botGPT SET kol = 20 WHERE dostup = 'min'")
    base.commit()
    cur.execute(f"UPDATE botGPT SET kol = 50 WHERE dostup = 'med'")
    base.commit()
    for (ret,) in cur.execute(f"SELECT call FROM botGPT WHERE dostup != 'max'"):
        try:
            await bot.send_message(ret,f"Доступы обновлены согласно тарифам!\n\n– 5 запросов в день бесплатно\n– 20 запросов в день 349 руб/мес\n– 50 запросов в день 649 руб/мес\n– ∞ число запросов с день 1490 руб/мес\n\nПо вопросам тарифов обратитесь в поддержку - @maya_mono",reply_markup=kb_answer1)
            await state.finish()
        except:
            continue


    # scheduler.add_job(message2days, "cron", day_of_week='fri', hour=12, minute=30,
    #                   args=(callback, dp,))

#scheduler.add_job(messageformonday, "cron", day_of_week='mon', hour=10, minute=30,
                              #args=(callback.from_user.id, dp,))

        # mass = []
        # for (ret,) in cur.execute(f"SELECT call FROM nextgo WHERE answer = 1"):
        #     mass.append(ret)
        # print(mass)
        # for i in mass:
        #     (name,) = cur.execute(
        #         f'SELECT name FROM users  WHERE call != {i} ORDER BY RANDOM()').fetchone()  # LIMIT 1;
        #     base.commit()
        #     print(name)

#analitics start in admin and function is here
async def statistic(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "users":
        await bot.send_message(callback.from_user.id,f"Выбери период",reply_markup = kb_time1)
    if str == "start":
        await bot.send_message(callback.from_user.id,f"Выбери период",reply_markup = kb_time2)
    if str == "activate":
        await bot.send_message(callback.from_user.id,f"Выбери период",reply_markup = kb_time3)
    if str == "spec":
        await bot.send_message(callback.from_user.id,f"Выбери период",reply_markup = kb_time4)
    if str == "ottok":
        mounth = datetime.date.today() + relativedelta(months=-1) #2022-11-20

        print(mounth)
        mounth_str = mounth.strftime('%m')
        year_str = mounth.strftime('%y')
        print(mounth_str) #11
        print(year_str)
        kol_user = 0
        kol_all = 0
        for (ret,) in cur.execute(f"SELECT call FROM users"):
            kol_all +=1
        for (ret,) in cur.execute(f"SELECT call FROM users WHERE datatime <='20{year_str}-{mounth_str}-1'"):
            kol_user +=1
        novoreg = 0
        for (ret,) in cur.execute(f"SELECT call FROM users WHERE datatime <='20{year_str}-{mounth_str}-30' AND datatime >='20{year_str}-{mounth_str}-01'"):
            novoreg+=1
        print(novoreg)
        summa = math.fabs(kol_user + novoreg - kol_all)
        await bot.send_message(callback.from_user.id,f"Отток {summa} %",reply_markup=kb_for_admin())

async def time1(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "today":
        today = 0
        for ret in cur.execute(f"SELECT call FROM users WHERE datatime = '{datetime.date.today()}'"):
            today+=1
        await bot.send_message(callback.from_user.id,f"Количество пользователей за сегодня : {today}",reply_markup=kb_for_admin())
    if str == "week":
        week = 0
        dat = datetime.date.today() - datetime.timedelta(days=7)
        for ret in cur.execute(f"SELECT call FROM users WHERE datatime <='{datetime.date.today()}' AND datatime >= '{dat}'"):
            week+=1
        await bot.send_message(callback.from_user.id,f"Количество пользователей за неделю : {week}",reply_markup=kb_for_admin())
    if str == "mounth":
        mounth = 0
        dat = datetime.date.today() - datetime.timedelta(days=30)
        for ret in cur.execute(
                f"SELECT call FROM users WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            mounth += 1
        await bot.send_message(callback.from_user.id, f"Количество пользователей за месяц : {mounth}",
                               reply_markup=kb_for_admin())
async def time2(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "today":
        today = 0
        for ret in cur.execute(f"SELECT call FROM statistic_start WHERE datatime = '{datetime.date.today()}'"):
            today += 1
        (today_all,) = cur.execute(f"SELECT sum(kol) FROM statistic_start WHERE datatime = '{datetime.date.today()}'").fetchone()
        await bot.send_message(callback.from_user.id, f"Количество уникальных заходов за сегодня : {today}\n\nКоличество общих заходов за сегодня : {today_all}",
                               reply_markup=kb_for_admin())
    if str == "week":
        week = 0
        dat = datetime.date.today() - datetime.timedelta(days=7)
        for ret in cur.execute(
                f"SELECT call FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            week += 1
        (week_all,) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        await bot.send_message(callback.from_user.id,
                               f"Количество уникальных заходов за неделю : {week}\n\nКоличество общих заходов за неделю : {week_all}",
                               reply_markup=kb_for_admin())
    if str == "mounth":
        mounth = 0
        dat = datetime.date.today() - datetime.timedelta(days=30)
        for ret in cur.execute(
                f"SELECT call FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            mounth += 1
        (mounth_all,) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        await bot.send_message(callback.from_user.id,
                               f"Количество уникальных заходов за месяц : {mounth}\n\nКоличество общих заходов за месяц : {mounth_all}",
                               reply_markup=kb_for_admin())

async def time3(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "today":
        today = 0
        reg = 0
        for ret in cur.execute(f"SELECT call FROM statistic_start WHERE datatime = '{datetime.date.today()}'"):
            today += 1
        (today_all,) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE datatime = '{datetime.date.today()}'").fetchone()
        for ret in cur.execute(
            f"SELECT call FROM users WHERE datatime = '{datetime.date.today()}'"):
            reg+=1
        try:
            summunik = reg / today * 100
            summall = reg / today_all * 100
            await bot.send_message(callback.from_user.id,
                                   f"Процент уникальных активаций за сегодня : {summunik} %\n\nПроцент общих активаций за сегодня : {summall} %",
                                   reply_markup=kb_for_admin())
        except:
            await bot.send_message(callback.from_user.id,f"На данный момент в базе данных недостаточно информации для подсчета этого типа статистика",reply_markup=kb_for_admin())


    if str == "week":
        week = 0
        reg = 0
        dat = datetime.date.today() - datetime.timedelta(days=7)
        for ret in cur.execute(f"SELECT call FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            week += 1
        (week_all,) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        for ret in cur.execute(
                f"SELECT call FROM users WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            reg += 1
        try:
            summunik = reg / week * 100
            summall = reg / week_all * 100
            await bot.send_message(callback.from_user.id,
                                   f"Процент уникальных активаций за неделю : {summunik} %\n\nПроцент общих активаций за неделю : {summall} %",
                                   reply_markup=kb_for_admin())
        except:
            await bot.send_message(callback.from_user.id,
                                   f"На данный момент в базе данных недостаточно информации для подсчета этого типа статистика",
                                   reply_markup=kb_for_admin())


    if str == "mounth":
        mounth = 0
        reg = 0
        dat = datetime.date.today() - datetime.timedelta(days=30)
        for ret in cur.execute(f"SELECT call FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            mounth += 1
        (mounth_all,) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        for ret in cur.execute(
                f"SELECT call FROM users WHERE datatime <='{datetime.date.today()}' AND datatime >='{dat}'"):
            reg += 1
        try:
            summunik = reg / mounth * 100
            summall = reg / mounth_all * 100
            await bot.send_message(callback.from_user.id,
                                   f"Процент уникальных активаций за сегодня : {summunik} %\n\nПроцент общих активаций за сегодня : {summall} %",
                                   reply_markup=kb_for_admin())
        except:
            await bot.send_message(callback.from_user.id,
                                   f"На данный момент в базе данных недостаточно информации для подсчета этого типа статистика",
                                   reply_markup=kb_for_admin())

async def time4(callback:types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    str = callback.data.split("_")[1]
    if str == "today":
        dict_prof = {}
        (dict_prof['Стилист'],) = cur.execute(f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Стилист' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Дизайнер'],) = cur.execute(f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Дизайнер' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Владелец производства'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец производства' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Специалист по рекламе'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Специалист по рекламе' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Владелец бренда'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бренда' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Конструктор'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Конструктор' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Байер'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Байер' AND datatime = '{datetime.date.today()}'").fetchone()
        (dict_prof['Владелец бутика '],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бутика' AND datatime = '{datetime.date.today()}'").fetchone()
        await bot.send_message(callback.from_user.id,f"Активность по специальностям за сегодня: \n\n {dict_prof}",reply_markup=kb_for_admin())
    if str == "week":
        dict_prof = {}
        dat = datetime.date.today() - datetime.timedelta(days=7)
        (dict_prof['Стилист'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Стилист' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Дизайнер'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Дизайнер' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец производства'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец производства' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Специалист по рекламе'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Специалист по рекламе' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец бренда'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бренда' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Конструктор'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Конструктор' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Байер'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Байер' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец бутика '],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бутика' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        await bot.send_message(callback.from_user.id, f"Активность по специальностям за неделю: \n\n {dict_prof}",
                               reply_markup=kb_for_admin())
    if str == "mounth":
        dict_prof = {}
        dat = datetime.date.today() - datetime.timedelta(days=30)
        (dict_prof['Стилист'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Стилист' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Дизайнер'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Дизайнер' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец производства'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец производства' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Специалист по рекламе'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Специалист по рекламе' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец бренда'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бренда' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Конструктор'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Конструктор' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Байер'],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Байер' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        (dict_prof['Владелец бутика '],) = cur.execute(
            f"SELECT sum(kol) FROM statistic_start WHERE spec = 'Владелец бутика' AND datatime <='{datetime.date.today()}' AND datatime >='{dat}'").fetchone()
        await bot.send_message(callback.from_user.id, f"Активность по специальностям за месяц: \n\n {dict_prof}",
                               reply_markup=kb_for_admin())
#analitics close

#back1 back2 back3 back4 for networking
# async def back1(callback:types.CallbackQuery):
#     await bot.answer_callback_query(callback.id)
#     await bot.send_message(callback.from_user.id,f"Чем могу помочь?",reply_markup=kb_answer1)
#     await state.finish()

####DIALOG II###

class Test(StatesGroup):
    Wait = State()
    Open = State()

async def reqII(message,state:FSMContext):
    print("IN reqII")
    #await asyncio.sleep(1)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    print(response)
    async with state.proxy() as data:
        data['text'] = response['choices'][0]['text']
    #await bot.send_message(id,f"{response['choices'][0]['text']}")
    #await IIbot.start.set()
    print(response['choices'][0]['text'])
    return response['choices'][0]['text']

async def test(message,state:FSMContext):
    k = 0
    async with state.proxy() as data:
        while data['text'] is Null:
            global my_new_message
            k += 1
            if k == 1:
                my_new_message = await bot.send_message(message, 'Отвечаю.')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id=message, message_id=my_new_message.message_id,
                                            text='Отвечаю..')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id=message, message_id=my_new_message.message_id,
                                            text='Отвечаю...')
            else:
                await bot.edit_message_text(chat_id=message, message_id=my_new_message.message_id,
                                            text='Отвечаю.')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id=message, message_id=my_new_message.message_id,
                                            text='Отвечаю..')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id=message, message_id=my_new_message.message_id,
                                            text='Отвечаю...')
                await asyncio.sleep(1)






async def dialogII(message:types.Message,state:FSMContext):
    if message.text == "/stop":
        await state.finish()
        await start(message,state)
    else:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
        )
        #print("FINISH OTVET")


        (dostup,) = cur.execute(f"SELECT dostup FROM botGPT WHERE call = '{message.chat.id}'").fetchone()
        if dostup != 'max':
            (kol,) = cur.execute(f"SELECT kol FROM botGPT WHERE call = '{message.chat.id}'").fetchone()
            if int(kol) <= 0:
                await bot.send_message(message.chat.id,
                                       f"Твое количество запросов на сегодня закончилось :(\n\nЗавтра твой доступ обновится согласно тарифу!\n\nДля того, чтобы увеличить количество запросов - обратись в поддержку - @maya_mono",
                                       reply_markup=kb_answer1)
                await state.finish()
            else:
                await bot.send_message(message.chat.id,
                                       f"{response['choices'][0]['text']}\n\nДля того чтобы завершить диалог и вернуться в главное меню - нажмите /stop")
                cur.execute(f"UPDATE botGPT SET kol = kol - 1 WHERE call = '{message.chat.id}'")
                base.commit()
                await IIbot.start.set()

        else:
            await bot.send_message(message.chat.id,
                                   f"{response['choices'][0]['text']}\n\nДля того чтобы завершить диалог и вернуться в главное меню - нажмите /stop")
            await IIbot.start.set()










    #my_thread = threading.Thread(target=reqII(message.text,state))
    #my_thread.start()
    #async with state.proxy() as data:
        #print(data['text'])
    # if message.text == "/stop":
    #     await state.finish()
    #     await start(message, state)
    # task = asyncio.create_task(reqII(message.text, message.chat.id, state))
    # k = 0
    # while True:
    #     if task.done():
    #         break
    #     global my_new_message
    #     k+=1
    #     if k == 1:
    #         my_new_message = await bot.send_message(message.chat.id, 'Отвечаю.')
    #         await asyncio.sleep(1)
    #         await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                     text='Отвечаю..')
    #         await asyncio.sleep(1)
    #         await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                     text='Отвечаю...')
    #     else:
    #         await asyncio.sleep(1)
    #         await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                     text='Отвечаю.')
    #         await asyncio.sleep(1)
    #         await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                     text='Отвечаю..')
    #         await asyncio.sleep(1)
    #         await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                     text='Отвечаю...')




        # await task
        # my_new_message = await bot.send_message(message.chat.id, 'Отвечаю.')
        # await asyncio.sleep(1)
        # await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
        #                             text='Отвечаю..')
        # await asyncio.sleep(1)
        # await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
        #                             text='Отвечаю...')

    # if task.done():
    #     my_new_message = await bot.send_message(message.chat.id, 'Отвечаю.')
    #     await asyncio.sleep(1)
    #     await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                 text='Отвечаю..')
    #     await asyncio.sleep(1)
    #     await bot.edit_message_text(chat_id=message.chat.id, message_id=my_new_message.message_id,
    #                                 text='Отвечаю...')
    #
    # else:
    #     await bot.send_message(message.chat.id,
    #                            f"{task}\n\nДля того чтобы завершить диалог и вернуться в главное меню - нажмите /stop")  # {response['choices'][0]['text']}


    # await test(message.chat.id)
    # await task()
    #
    #
    # await bot.send_message(message.chat.id,
    #                            f"{await task()}\n\nДля того чтобы завершить диалог и вернуться в главное меню - нажмите /stop")#{response['choices'][0]['text']}
    # await IIbot.start.set()








            # await bot.send_message(message.chat.id, f"Отвечаю.{message.message_id}")
            # print(".",message.message_id)
            # await asyncio.sleep(2)
            # await bot.delete_message(message.chat.id, message.message_id + 1)
            # await bot.send_message(message.chat.id, f"Отвечаю..{message.message_id}")
            # print("..",message.message_id)
            # await asyncio.sleep(2)
            # await bot.delete_message(message.chat.id, message.message_id + 2)
            # await bot.send_message(message.chat.id, f"Отвечаю...{message.message_id}")
            # print("...",message.message_id)
            # await asyncio.sleep(2)
            # await bot.delete_message(message.chat.id, message.message_id + 3)
            # await bot.send_message(message.chat.id, f"Отвечаю.")
            # print(message.message_id)
            # await asyncio.sleep(2)
            # await bot.send_message(message.chat.id, f"Отвечаю..")
            # print(message.message_id)
            # await asyncio.sleep(2)
            # await bot.send_message(message.chat.id, f"Отвечаю...")
            # print(message.message_id)
            # break
            # await bot.send_message(message.chat.id, f"Отвечаю.")
            # await asyncio.sleep(1)
            # await bot.delete_message(message.chat.id, message.message_id + 1)
            # await asyncio.sleep(1)
            # await bot.send_message(message.chat.id, f"Отвечаю..")
            # await bot.delete_message(message.chat.id, message.message_id + 2)
            # await asyncio.sleep(1)
            # await bot.send_message(message.chat.id, f"Отвечаю...")
            # await bot.delete_message(message.chat.id, message.message_id + 3)

    # if message.text == "/stop":
    #     await state.finish()
    #     await start(message,state)
    # else:
    #     response = openai.Completion.create(
    #         model="text-davinci-003",
    #         prompt=message.text,
    #         temperature=0.9,
    #         max_tokens=1000,
    #         top_p=1.0,
    #         frequency_penalty=0.0,
    #         presence_penalty=0.6,
    #         stop=["You:"]
    #     )
    #     if response:
    #         print("!!!!TRUE!!!")
    #     await bot.send_message(message.chat.id,
    #                            f"{response['choices'][0]['text']}\n\nДля того чтобы завершить диалог и вернуться в главное меню - нажмите /stop")
    #     await IIbot.start.set()


def shedl():
    scheduler.add_job(messageformonday, "cron", day_of_week='mon', hour=10, minute=30)
    scheduler.add_job(message2days, "cron", day_of_week='fri', hour=12, minute=30)
    scheduler.add_job(updateBotGPT, "cron", hour=00, minute=00)


if __name__ == "__main__":
    shedl()
    dp.register_callback_query_handler(spec, Text(startswith='spec_'),state=User.spec)
    dp.register_callback_query_handler(networking, Text(startswith='answer_'),state=None)
    dp.register_callback_query_handler(networkingAnswer, Text(startswith='answer2_'),state=None)
    dp.register_callback_query_handler(networkingAnswer3, Text(startswith='answer3_'), state=None)
    dp.register_callback_query_handler(parserButton, Text(startswith='parser_'),state=None)
    dp.register_callback_query_handler(dopParserButton, Text(startswith='dop_'))
    dp.register_callback_query_handler(Answer4, Text(startswith='answer4_'), state=None)
    dp.register_callback_query_handler(Answer5, Text(startswith='answer5_'), state=None)
    dp.register_callback_query_handler(Answer6, Text(startswith='answer6_'), state=None)
    dp.register_callback_query_handler(Answer7, Text(startswith='answer7_'), state=None)
    dp.register_callback_query_handler(Answer8, Text(startswith='answer8_'), state=None)
    dp.register_callback_query_handler(days2answer1, Text(startswith='days2answer1_'), state=None)
    dp.register_callback_query_handler(days2answer2, Text(startswith='days2answer2_'))
    dp.register_callback_query_handler(days2answer3, Text(startswith='days2answer3_'))
    dp.register_callback_query_handler(adminCall1, Text(startswith='admin_'),state=None)
    dp.register_callback_query_handler(adminWhoButtonNews, Text(startswith='group_'), state=AdminNews.who)
    dp.register_callback_query_handler(readyNetworking, Text(startswith='readyNetworking'), state=None)
    dp.register_callback_query_handler(gonext1, Text(startswith='gonext1'), state=None)
    dp.register_callback_query_handler(gonext2, Text(startswith='gonext2'), state=None)
    dp.register_callback_query_handler(gonext3, Text(startswith='gonext3'), state=None)
    dp.register_callback_query_handler(sendVack, Text(startswith='sendVack_'), state=FindIspoln.who)
    dp.register_callback_query_handler(thankyou, Text(startswith='thankyou'), state=None)
    dp.register_callback_query_handler(greatmeropr, Text(startswith='greatmeropr'), state=None)
    dp.register_callback_query_handler(greatgo, Text(startswith='greatgo'), state=None)
    dp.register_callback_query_handler(helpMaya, Text(startswith='helpMaya_'), state=None)
    dp.register_callback_query_handler(adminall, Text(startswith='adminall_'), state=None)
    dp.register_callback_query_handler(calllike, Text(startswith='like_'), state=None)
    dp.register_callback_query_handler(groupbudb, Text(startswith='groupbudb_'), state=None)

    dp.register_callback_query_handler(statistic, Text(startswith='stats_'), state=None)
    dp.register_callback_query_handler(time1, Text(startswith='time1_'), state=None)
    dp.register_callback_query_handler(time2, Text(startswith='time2_'), state=None)
    dp.register_callback_query_handler(time3, Text(startswith='time3_'), state=None)
    dp.register_callback_query_handler(time4, Text(startswith='time4_'), state=None)

    #dp.register_callback_query_handler(back1, Text(startswith='back1_1'), state=None)

    dp.register_message_handler(start, commands=['start'], state=None)
    dp.register_message_handler(admin, commands=['themono'], state=None)
    dp.register_message_handler(about, commands=['about'])
    dp.register_message_handler(contacts, commands=['contacts'])
    # dp.register_message_handler(lora, commands=['lora'])

    dp.register_message_handler(name,state=User.name)
    dp.register_message_handler(MySpec, state=User.spec)
    dp.register_message_handler(soclink, state=User.soclink)
    dp.register_message_handler(city, state=User.city)
    dp.register_message_handler(company, state=User.company)
    #dp.register_message_handler(role, state=User.role)
    dp.register_message_handler(clever, state=User.clever)
    dp.register_message_handler(helpMe, state=User.q_help)
    dp.register_message_handler(main)
    dp.register_message_handler(networkingMessage,state = Question.q_from_user)
    dp.register_message_handler(poshelaniaMessage, state=Poshelania.ans)
    dp.register_message_handler(whatIsFail, state=WhatIsFail.fail)
    dp.register_message_handler(impression, state=Days2message.impression)
    scheduler.start()
    #dp.register_message_handler(ispoln, state=FindIspoln.who)
    dp.register_message_handler(describeispoln, state=FindIspoln.describe)

    #dp.register_message_handler(AdminLastNewsPhoto, content_types=['photo'],state=AdminNewsLast.img)
    dp.register_message_handler(AdminLastNewsText, state=AdminNewsLast.text)
    #dp.register_message_handler(AdminBestNewsPhoto, content_types=['photo'], state=AdminNewsBest.img)
    dp.register_message_handler(AdminBestNewsText, state=AdminNewsBest.text)
    dp.register_message_handler(adminWhoNews, state=AdminNews.who)
    dp.register_message_handler(adminPhotoNews,content_types=['photo'], state=AdminNews.img)
    dp.register_message_handler(adminTextNews, state=AdminNews.text)
    dp.register_message_handler(adminPhotoAvent, content_types=['photo'], state=AdminAvent.img)
    dp.register_message_handler(adminTextAvent, state=AdminAvent.text)
    dp.register_message_handler(adminCallMess,state=AdminMessage.call)
    dp.register_message_handler(adminTextMess, state=AdminMessage.mess)
    dp.register_message_handler(adminTextAll, state=AdminMessageAll.mess)
    dp.register_message_handler(adminTextGroup, state=AdminMessageGroup.group)
    dp.register_message_handler(adminTextGroupMess, state=AdminMessageGroup.mess)
    dp.register_message_handler(MyWhat, state=My.what)
    dp.register_message_handler(MyWho, state=My.who)
    dp.register_message_handler(MyDescribe, state=My.describe)
    dp.register_message_handler(MyLink, state=My.link2)
    dp.register_message_handler(MyPrice, state=My.price)
    dp.register_message_handler(fromadmin, state=FromAdmin.message)
    dp.register_message_handler(toadminmess, state=FromAdmin.toadminmess)
    dp.register_message_handler(messageforgroupbydb, state=ForGroupByDb.message)
    #II
    dp.register_message_handler(dialogII, state=IIbot.start)



    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)