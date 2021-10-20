from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, Updater,MessageHandler,CommandHandler,Filters
from function import *
import time
from ast import literal_eval
def inbtn(type, t_kate=None, t_brend=None):
    if type=='main':
        btn=[]
        d=forkate()
        for i in range(0,4,2):
            a=[InlineKeyboardButton(d[i][1],callback_data=d[i][0]),InlineKeyboardButton(d[i+1][1],callback_data=d[i+1][0])]
            btn.append(a)
        btn.append([InlineKeyboardButton(d[4][1],callback_data=d[4][0])]) 
          
        return InlineKeyboardMarkup(btn)
    elif type=='brend':
        btn=[]
        d=forbrend()
        for i in range(0,6,2):
            a=[InlineKeyboardButton(d[i][1],callback_data=f"{t_kate}_{d[i][0]}"),InlineKeyboardButton(d[i+1][1],callback_data=f"{t_kate}_{d[i+1][0]}")]
            btn.append(a)
        btn.append([InlineKeyboardButton(d[6][1],callback_data=f"{t_kate}_{d[6][0]}")])    
        return InlineKeyboardMarkup(btn)
def keybtn(type):
    if type=='main':
        a=[[KeyboardButton("Mahsulot qo'shish"),KeyboardButton("Mahsulot olib tashlash")],
        [KeyboardButton("Bosh sahifa")]]
    elif type=='kate':
        a=[]
        d=get_kate()
        for i in range(0,len(d)-1,2):
            s=[KeyboardButton(d[i][1]),KeyboardButton(d[i+1][1])]
            a.append(s)
        if len(d)%2==1:
           a.append([KeyboardButton(d[-1][1])])
        a.append([KeyboardButton('orqaga')])
    elif type=='brend':
        a=[]
        d=get_brend()
        for i in range(0,len(d)-1,2):
            s=[KeyboardButton(d[i][1]),KeyboardButton(d[i+1][1])]
            a.append(s)
        if len(d)%2==1:
           a.append([KeyboardButton(d[-1][1])])
        a.append([KeyboardButton('orqaga')])




    return ReplyKeyboardMarkup(a,resize_keyboard=True)










def start(update, context):
    user = update.message.from_user
    add_user(user.id)
    qadam=get_step(user.id)
    if qadam[0]==None:
        upd_step(user.id, {'qadam': 1})
        update.message.reply_text('Assalomu aleykum Nout.uz sayti botiga xush kelibsiz\nBotdan foydalanish uchun Registratsiyadan o`tishingiz kerak!')
        time.sleep(3)
        update.message.reply_text('Iltimos ismingizni kiriting:')
    elif literal_eval(qadam[0]).get('qadam', 0)==4:
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=inbtn('main'))

def for_message(update, context):
    user = update.message.from_user
    msg = update.message.text
    qadam = get_step(user.id)

    if literal_eval(qadam[0]).get('qadam', 0) == 1:
        upd_step(user.id, {'qadam': 2, 'ism': msg})
        update.message.reply_text('telefon raqamingizni kiriting',
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Telefon raqamni yuborish', request_contact=True)]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 2:
        upd_step(user.id, {'qadam':3, 'ism':literal_eval(qadam[0]).get('ism',''), 'tel': msg })
        update.message.reply_text('Manzilingizni kiriting(viloyat, tuman yoki shaxar')

    elif literal_eval(qadam[0]).get('qadam', 0) == 3:
        qadam = upd_step(user.id, {'qadam': 4, 'ism': literal_eval(qadam[0]).get('ism', ''),
                                'tel': literal_eval(qadam[0]).get('tel', ''), 'locatsiya': msg})
        for_inform(user, literal_eval(qadam[0]))
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=inbtn('main'))
    
    elif msg=='admin':
        upd_step(user.id,{'qadam':5})
        update.message.reply_text('Parolni kiriting')
    
    elif literal_eval(qadam[0]).get('qadam', 0) == 5 and msg=='9798':
        upd_step(user.id,{'qadam':6})
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=keybtn('main'))    
    
    elif literal_eval(qadam[0]).get('qadam', 0) == 6 and msg=='Bosh sahifa':
        upd_step(user.id,{'qadam':4})
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=inbtn('main'))
    
    elif literal_eval(qadam[0]).get('qadam', 0) == 6 and msg=="Mahsulot qo'shish":
        upd_step(user.id,{'qadam':7})
        update.message.reply_text('Kategorya tanlang',reply_markup=keybtn('kate'))
   
    elif literal_eval(qadam[0]).get('qadam', 0) == 7 and msg=='orqaga':
        upd_step(user.id,{'qadam':6})
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=keybtn('main'))
    
    elif literal_eval(qadam[0]).get('qadam', 0) == 7:
        upd_step(user.id,{'qadam':8})
        kate_insert(msg)
        update.message.reply_text('brand nomini tanlang',  reply_markup=keybtn('brend'))

    elif literal_eval(qadam[0]).get('qadam', 0) == 8 and msg=='orqaga':
        upd_step(user.id,{'qadam':7})
        del_last()
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=keybtn('kate'))
    
    elif literal_eval(qadam[0]).get('qadam', 0) == 8:
        brend_update(msg)
        upd_step(user.id,{'qadam':9})
        update.message.reply_text("""Siz endi quydagilarni kiritishingiz kerak\nMahsulot nomi#\nMahsulot haraktiristikasi#\nMahsulot narxi#\nMahsulot rasmining nomi farmati bilan#\n(bu yerda # belgisi har bir kiritilayotgan ma'lumotdan keyin bo'lishi shart  """ ,reply_markup=ReplyKeyboardMarkup([[KeyboardButton('orqaga')]], resize_keyboard=True))
   
    elif  literal_eval(qadam[0]).get('qadam', 0) == 9 and msg=='orqaga':
        upd_step(user.id,{'qadam':8})
        brend_update_del()
        update.message.reply_text('brand nomini tanlang',  reply_markup=keybtn('brend'))
    
    elif  literal_eval(qadam[0]).get('qadam', 0) == 9:
        upd_step(user.id,{'qadam':10})
        data_sp=msg.split('#')
        mahsulot_4(data_sp)
        update.message.reply_text("Ma'lumotlar to'g'rimi", reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Ha'),KeyboardButton("yo'q")]],resize_keyboard=True))

    elif literal_eval(qadam[0]).get('qadam', 0) == 10 and msg=='Ha':
        upd_step(user.id,{'qadam':4})
        update.message.reply_text("Mahsulot ramini jo'natig")
        
    elif literal_eval(qadam[0]).get('qadam', 0) == 10 and msg=="yo'q":
        upd_step(user.id,{'qadam':6})
        update.message.reply_text('Quydagilardan birini tanlang', reply_markup=keybtn('main'))    
        del_last()


def for_image(update,  context):
    file = update.message.photo[-1].file_id
    
    obj = context.bot.get_file(file)
    obj.download()
    context.bot.send_photo(caption='nimadir',chat_id=update.message.chat_id , photo=open('file_3.jpg','rb'))







def for_contact(update, context):
    user = update.message.from_user
    qadam = get_step(user.id)
    msg = update.message.contact.phone_number
    if literal_eval(qadam[0]).get('qadam', 0) == 2:
        upd_step(user.id, {'qadam':3, 'ism':literal_eval(qadam[0]).get('ism',''), 'tel': msg })
        update.message.reply_text('Manzilingizni kiriting(viloyat, tuman yoki shaxar)')
def for_inline(update,context):
    user=update.callback_query.from_user
    d=update.callback_query.data
    data_sp=d.split('_')
    print(data_sp)
    if len(data_sp)>1:
        if len(data_sp)>2:
            ras=for_tarif(int(data_sp[0]),int(data_sp[1]),int(data_sp[2]))
            a=for_buyirtma(int(data_sp[0]),int(data_sp[1]),int(data_sp[2]))
            context.bot.send_photo(caption=f'{ras[0]}\nnarxi: {a[1]}',chat_id=update.callback_query.message.chat_id,photo=open(f"{ras[1]}",'rb'),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('sotib olish',
                    callback_data=f'{data_sp[0]}_{data_sp[1]}_{data_sp[2]}_sotib olish'),InlineKeyboardButton('Bosh sahifa ',
                    callback_data=f'{data_sp[0]}_{data_sp[1]}_{data_sp[2]}_ortga')]]))

            if len(data_sp)>3:
                if data_sp[3]=='ortga':
                    context.bot.delete_message(message_id=update.callback_query.message.message_id,chat_id=update.callback_query.message.chat_id)
                    context.bot.send_message(text='Quydagilardan birini tanlang',chat_id=update.callback_query.message.chat_id, reply_markup=inbtn('main'))
                elif data_sp[3]=='sotib olish':
                    a=user_olish(user.id)
                    b=for_buyirtma(int(data_sp[0]),int(data_sp[1]),int(data_sp[2]))
                    
                    context.bot.send_message(text=f"""user:{a[0]}\nism:{a[1]}\ntel:{a[2]}\njoylashuv:{a[3]}\nbuyirtma:{b[0]}\nnarx:{b[1]}.""",chat_id='1157247305')
                    context.bot.delete_message(message_id=update.callback_query.message.message_id,chat_id=update.callback_query.message.chat_id)
                    context.bot.send_message(text="Buyurtmangiz qabul qilindi siz bilan operatorimiz bog'lanishini kuting",chat_id=update.callback_query.message.chat_id)



        else:
            a=for_id(int(data_sp[0]),int(data_sp[1]))
            btn=[]
            if len(a)%2==0:
                for i in range(0,len(a),2):
                    db=[InlineKeyboardButton(f'{i+1}',callback_data=f"{data_sp[0]}_{data_sp[1]}_{a[i][0]}") , InlineKeyboardButton(f'{i+2}',callback_data=f"{data_sp[0]}_{data_sp[1]}_{a[i+1][0]}")]  
                    btn.append(db)
                re=InlineKeyboardMarkup(btn)
                nomi_n=for_malumot(int(data_sp[0]),int(data_sp[1]))
                s=''
                for i in  range(len(nomi_n)):
                    s+=f'{i+1}'+nomi_n[i][1]+'\n'

                update.callback_query.message.edit_text(f'{s}', reply_markup=re)
            else:
                for i in range(0,len(a)-1,2):
                    db=[InlineKeyboardButton(f'{i+1}',callback_data=f"{data_sp[0]}_{data_sp[1]}_{a[i][0]}") , InlineKeyboardButton(f'{i+2}',callback_data=f"{data_sp[0]}_{data_sp[1]}_{a[i+1][0]}")]  
                    btn.append(db)
                btn.append([InlineKeyboardButton(f'{len(a)}',callback_data=f"{data_sp[0]}_{data_sp[1]}_{a[-1][0]}")])
                re=InlineKeyboardMarkup(btn)
                nomi_n=for_malumot(int(data_sp[0]),int(data_sp[1]))
                s=''
                d=1
                for i in  range(len(nomi_n)):
                    s+=f'{i+1}'+nomi_n[i][1]+'\n'
                update.callback_query.message.edit_text(f'{s}', reply_markup=re)

    else:
        update.callback_query.message.edit_text('Brend nomini tanlang', reply_markup=inbtn('brend',t_kate=data_sp[0]))

def main():
    Token = "1969862768:AAFqut0F_CnMQYr4S-c7Q7qTZgFqqqMRASc"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, for_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, for_image))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, for_contact))
    updater.dispatcher.add_handler(CallbackQueryHandler(for_inline))



    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()