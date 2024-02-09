# import aiogram 
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token= '6639475058:AAHmDuOp-HMsWZcmnJygviAr5Z-_5vXhCoY')
dp = Dispatcher(bot)
######################################################################
###
### КНОПКА ОТМЕНЫ
###
cancellationKB = InlineKeyboardMarkup(row_width=1)
cancellationbtn = InlineKeyboardButton(text='❌Отмена', callback_data='Отмена')
cancellationKB.add(cancellationbtn)
#####################################################################
###
### КНОПКИ ВПЕРЕД И НАЗАД
###
forwardKB = InlineKeyboardMarkup(resize_keyboard= True,row_width=1)
forwardbtn = InlineKeyboardButton(text ='⏩Вперед', callback_data='Вперед')
forwardKB.insert(forwardbtn)
backKB = InlineKeyboardMarkup(resize_keyboard= True,row_width=1)
backbtn = InlineKeyboardButton(text = '⏪Назад', callback_data='Назад')
backKB.insert(backbtn)
####################################################################
# BUTTONS
mainKB = ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
buybtn = KeyboardButton(text = '📲Купить')
profilebtn = KeyboardButton(text = '🙆Профиль')
multiservicebtn = KeyboardButton(text = '☎️Мультисервис')
rentbtn = KeyboardButton(text = '⏰Аренда')
infobtn = KeyboardButton(text = '🪪Инфо')
proectsbtn = KeyboardButton(text = '🫀Наши проекты')
chatbtn = KeyboardButton(text = '👋Наш чат услуг')
mainKB.add(buybtn,profilebtn,multiservicebtn,rentbtn,infobtn,proectsbtn,chatbtn)
######################################################################
#####
##### КУПИТЬ 
#####
avitobtn = InlineKeyboardButton(text = 'Avito', callback_data='Avito')
vkontaktebtn = InlineKeyboardButton(text = 'Вконтакте', callback_data='VK')
telegrambtn = InlineKeyboardButton(text = 'Telegram', callback_data='Telegram')
viberbtn = InlineKeyboardButton(text = 'Viber', callback_data='Viber')
googlebtn = InlineKeyboardButton(text = 'Google', callback_data='Google')
uberbtn = InlineKeyboardButton(text = 'Uber', callback_data='Uber')
instagrambtn = InlineKeyboardButton(text = 'Instagram', callback_data='Instagram')
odnoklasnikibtn = InlineKeyboardButton(text = 'Одноклассники', callback_data='OK')
mailrubtn = InlineKeyboardButton(text = 'Mailru', callback_data='Mailru')
search1btn = InlineKeyboardButton(text='🔍Поиск', callback_data='Search')
cancellationMainbtn = InlineKeyboardMarkup(row_width=2)
cancellationbtn = InlineKeyboardButton(text = '❌Отмена', callback_data='Cancellation')
buyKB = InlineKeyboardMarkup(row_width=4)
buyKB.add(avitobtn,vkontaktebtn).add(telegrambtn, googlebtn).add(uberbtn,instagrambtn).add(odnoklasnikibtn,mailrubtn).add(search1btn).add(forwardbtn)
cancellationMainbtn.add(cancellationbtn)
###############################################################################
###
### Купить вторая страница
###
buyKB2 = InlineKeyboardMarkup(row_width=2)
twitter = InlineKeyboardButton(text = 'Twitter', callback_data='Twitter')
steam = InlineKeyboardButton(text='Steam', callback_data='Steam')
qiwi = InlineKeyboardButton(text='Qiwi', callback_data='Qiwi')
ebay = InlineKeyboardButton(text='eBay', callback_data='eBay')
buyKB2.add(twitter,steam,qiwi,ebay).add(search1btn).add(backbtn)
###############################################################################
###
### КНОПКИ АВИТО
###
listAvitoKB = InlineKeyboardMarkup(row_width=2)
russian = InlineKeyboardButton(text = '🇷🇺Россия', callback_data='Russian')
listAvitoKB.add(russian).add(cancellationbtn)
##############################################################################
###
### КНОПКИ ПРОФИЛЯ
###
mainprofileKB = InlineKeyboardMarkup(row_width=1)
balancebtn = InlineKeyboardButton(text = '💵Пополнить баланс', callback_data='Пополнить баланс')
referalbtn = InlineKeyboardButton(text = '👨‍🦰🤝👧Реферальная система', callback_data='Реферальная система')
transferbalancebtn = InlineKeyboardButton(text = '🎟️Передать баланс',callback_data='Передать баланс')
salehistorybtn = InlineKeyboardButton(text = '🛒История покупок', callback_data='История покупок')
adOFF = InlineKeyboardButton(text = '🔕Отключить рекламу', callback_data='Отключить рекламу')
mainprofileKB.add(balancebtn,referalbtn,transferbalancebtn,salehistorybtn,adOFF)
#######################################################
###
### Мультисервис
###
multiKB = InlineKeyboardMarkup(row_width=1)
avitoMulti = InlineKeyboardButton(text = 'Avito', callback_data='Avito')
vkontakteMulti = InlineKeyboardButton(text = 'Вконтакте', callback_data='VK')
telegramMulti = InlineKeyboardButton(text = 'Telegram', callback_data='Telegram')
viberMulti = InlineKeyboardButton(text = 'Viber', callback_data='Viber')
googleMulti = InlineKeyboardButton(text = 'Google', callback_data='Google')
uberMulti = InlineKeyboardButton(text = 'Uber', callback_data='Uber')
instagramMulti = InlineKeyboardButton(text = 'Instagram', callback_data='Instagram')
odnoklasnikiMulti = InlineKeyboardButton(text = 'Одноклассники', callback_data='OK')
mailruMulti = InlineKeyboardButton(text = 'Mailru', callback_data='Mailru')
multiKB.add(avitoMulti, vkontakteMulti, telegramMulti, googleMulti, uberMulti, viberMulti, instagramMulti, odnoklasnikiMulti, mailruMulti)
################################################################
###
### Аренда
###
rentaKB = InlineKeyboardMarkup(row_width = 1)
rentanumberbtn = InlineKeyboardButton(text = '⏰Арендовать номер', callback_data='Арендовать номер')
activenumberbtn = InlineKeyboardButton(text='📞Активные номера', callback_data='Активные номера')
historynumberbtn = InlineKeyboardButton(text='🛒История', callback_data='История')
rentaKB.add(rentanumberbtn, activenumberbtn, historynumberbtn)
####################################################################
###
### Инфо
###
infoKB = InlineKeyboardMarkup(row_width=1)
supportbtn = InlineKeyboardButton(text='🆘Тех. Поддержка',  callback_data='Тех. Поддержка')
instructionsbtn = InlineKeyboardButton(text='🛠️Иструкция', callback_data='Иструкция')
rulesbtn = InlineKeyboardButton(text = '🧠Правила', callback_data='Правила')
infoKB.add(supportbtn,instructionsbtn,rulesbtn)
#####################################################################
###
### При нажатии на товар
###



######################################################################
###
### При пополнении баланса
###
replenishmentKB = InlineKeyboardMarkup(row_width=1)
qiwiRFbtn = InlineKeyboardButton(text='💳QIWI или Карты РФ', callback_data='QIWI или Карты РФ')
qiwiRF2btn = InlineKeyboardButton(text='💳QIWI или Карты РФ 2 ',callback_data='QIWI или Карты РФ 2')
payeerbtn =  InlineKeyboardButton(text='💳Payeer', callback_data='Payeer')
umoneybtn = InlineKeyboardButton(text='🟣ЮNMoney', callback_data='ЮNMoney')
cryptobtn = InlineKeyboardButton(text='💶Crypto', callback_data='Crypto')
replenishmentKB.add(qiwiRFbtn, qiwiRF2btn, payeerbtn, umoneybtn, cryptobtn)
###########################################################################




@dp.message_handler(commands=['start'])
async def first_start(message: types.Message, state=None):
    try:
        await message.answer_sticker("CAACAgIAAxkBAAEDDlJlsTnYaBaFaK8gnK267P-HxhSLwAACKAADMoj7L1sZCPbgp_zoNAQ")
        text='<b>Привет, мой дорогой друг!\nПереходи в мой канал - @MakichOFF\nПриятного просмотра!</b>'
        await message.answer(text, reply_markup=mainKB, parse_mode='HTML')
    except:
        None

@dp.message_handler(content_types=['animation'])
async def get_id(message: types.Message):
    print(message.animation.file_id)


##################################################################################
###
### РАЗДЕЛ КУПИТЬ
###

@dp.message_handler(text='📲Купить')
async def get_name(message: types.Message):
    try:
        await message.answer_animation('CgACAgIAAxkBAANlZb-IdRLr_212xL5ySydHlw12BtIAAjdAAAJe1flJtPgC1HDEL1Y0BA', 
                                    caption='👇Выберите необходимый сервис:', 
                                    parse_mode='HTML', 
                                    reply_markup=buyKB)
    except:
        None

################# КУПИТЬ 
@dp.callback_query_handler(text='Search')
async def search1(call: CallbackQuery):
        await call.message.answer('Введите название сервиса', reply_markup=cancellationMainbtn)

###################### ОПЛАТА АВИТО
@dp.callback_query_handler(text='Avito')
async def avito(call: CallbackQuery):
    await call.message.answer_animation('CgACAgIAAxkBAANlZb-IdRLr_212xL5ySydHlw12BtIAAjdAAAJe1flJtPgC1HDEL1Y0BA', 
                                        caption='🌏👇 Выберите страну, номера которой вы хотите использовать:',
                                        parse_mode='html',
                                        reply_markup=listAvitoKB)

############################ КНОПКИ ВПЕРЕД И НАЗАД
@dp.callback_query_handler(text='Вперед')
async def forward_kb(call: CallbackQuery):
    await call.message.answer_animation('CgACAgIAAxkBAANlZb-IdRLr_212xL5ySydHlw12BtIAAjdAAAJe1flJtPgC1HDEL1Y0BA')
    await call.message.answer(text='Выберите необходимый сервис:', reply_markup=buyKB2)

@dp.callback_query_handler(text='Назад')
async def back_kb(call: CallbackQuery):
    await call.message.answer_animation('CgACAgIAAxkBAANlZb-IdRLr_212xL5ySydHlw12BtIAAjdAAAJe1flJtPgC1HDEL1Y0BA', 
                                        caption='Выберите необходимый сервис:',
                                        parse_mode='html', reply_markup=buyKB)

###################################################
###
### ПРОФИЛЬ
###
@dp.message_handler(text='🙆Профиль')
async def gif_prof(message: types.Message):
    await message.answer_animation('CgACAgIAAxkBAAIBMmXDrJArqol7Q8dEniW1TI9kKFdVAAIWRgACYkUhSqaY1x06mmdsNAQ', 
                                caption='🏦Ваш баланс:\n🪪Ваш Id - \n🛍️Количество покупок:', 
                                reply_markup=mainprofileKB)

@dp.callback_query_handler(text='Пополнить баланс')
async def upBalance(call: CallbackQuery):
    await call.message.answer(text='Выберите способ пополнения:', reply_markup=replenishmentKB)

@dp.callback_query_handler(text='Реферальная система')
async def referal(call: CallbackQuery):
    await call.message.answer_animation('CgACAgIAAxkBAAIBQmXDsiot9kMR3oa4FZdsBLTU5wNgAAJeRgACYkUhSr_f-ILc2mVjNAQ', 
                                        caption='⛓️Реферальная ссылка: <code>https://vk.com/al_feed.php</code>\n💰Заработано на рефералах:\n💻Количество рефералов:\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n<u>Вы будете получать на баланс 5% от пополнений ваших рефералов</u>', 
                                        parse_mode='html', )

###############################################################
###
### ПЕРЕДАТЬ БАЛАНС
###
@dp.callback_query_handler(text='Передать баланс')
async def sendBalance(call: CallbackQuery):
    await call.message.answer_animation('CgACAgIAAxkBAAIBWmXDtpfN5kUpPH2s35sekkynlBEGAAKvRgACYkUhSgvkuPW-trMqNAQ', caption='Введите ник пользователя, которому нужно отправить деньги\n\n<i>Пожалуйста, вводите имя пользователя верно, иначе средства пропадут и возвращены не будут</i>', 
                                        reply_markup=cancellationKB, parse_mode='html')
    # await call.message.answer(text='Выберите необходимый сервис:', reply_markup=replenishmentKB)




























executor.start_polling(dp, skip_updates=True)