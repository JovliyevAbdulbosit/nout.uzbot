import sqlite3

con = sqlite3.connect('nout_baza.db', check_same_thread=False)
cur = con.cursor()

def add_user(user_id):
    try:
        sql = f"""
        insert into users(user_id) values({user_id})
        """
        cur.execute(sql)
        con.commit()
    except:
        pass

def get_step(user_id):
    sql = f"""
    select qadam from users where user_id = {user_id}
"""
    cur.execute(sql)
    return cur.fetchone()

def upd_step(user_id, qadam):
    sql = f"""
    update users set qadam = "{qadam}" where user_id = {user_id} 
"""
    cur.execute(sql)
    con.commit()
    return get_step(user_id)

def for_inform(user, qadam):
    try:
        sql = f"""
        insert into inform(user_id, username, ism, phone_number, joylashuv)
        values({user.id}, "{user.username}", "{qadam.get('ism', '')}","{qadam.get('tel', '')}","{qadam.get('locatsiya', '')}")
    """
        cur.execute(sql)
        con.commit()
    except:
        pass    

def forkate():
    sql=f"""SELECT * FROM kategorya1 """
    cur.execute(sql)
    return cur.fetchall()

def forbrend():
    sql=f"""SELECT * FROM brend2 """
    cur.execute(sql)
    return cur.fetchall()

def for_id(id1,id2):
    sql=f"""SELECT id FROM def2 
WHERE kate_id={id1} and brend_id={id2} """
    cur.execute(sql)
    return cur.fetchall()
def for_malumot(id1,id2):
    sql=f"""SELECT id,name3 FROM def2 
WHERE kate_id={id1} and brend_id={id2} """
    cur.execute(sql)
    return cur.fetchall()    

def for_tarif(id1,id2,id3):
    sql=f"""SELECT tarif,rasm FROM def2 
WHERE kate_id={id1} and brend_id={id2} and id={id3}"""
    cur.execute(sql)
    return cur.fetchone() 
def user_olish(user_id):
    sql=f"""SELECT username,ism,phone_number,joylashuv FROM inform
WHERE user_id={user_id}""" 
    cur.execute(sql)
    return cur.fetchone()
print(user_olish(242324710))
def for_buyirtma(id1,id2,id3):
    sql=f"""SELECT name3,narx FROM def2 
WHERE kate_id={id1} and brend_id={id2} and id={id3}"""
    cur.execute(sql)
    return cur.fetchone()     

def get_kate():
    sql=f"""select * from kategorya1"""  
    cur.execute(sql) 
    return cur.fetchall()
def get_brend():
    sql=f"""select * from brend2"""  
    cur.execute(sql) 
    return cur.fetchall()



def last_element():
    sql=f"""select id from def2 """
    cur.execute(sql)
    return cur.fetchall()
def kate_insert(msg):
    sql=f"""select * from kategorya1 where name1="{msg}" """
    cur.execute(sql)
    a=cur.fetchone()
    sql1=f"""insert into def2(kate_id)values({a[0]})"""
    cur.execute(sql1)
    con.commit()
def del_last():
    last=last_element()
    sql=f"""delete from def2 where id={last[-1][0]} """
    cur.execute(sql)
    con.commit()
def brend_update(msg):
    sql=f"""select * from brend2 where name2="{msg}" """
    cur.execute(sql)
    a=cur.fetchone()
    last=last_element()
    sql1=f"""update def2 set brend_id={a[0]} where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def brend_update_del():
    
    last=last_element()
    sql1=f"""update def2 set brend_id=NULL where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def product_insert(msg):
    last=last_element()
    sql1=f"""update def2 set name3="{msg}" where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def product_harak(msg):
    last=last_element()
    sql1=f"""update def2 set tarif="{msg}" where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def product_prace(msg):
    last=last_element()
    sql1=f"""update def2 set narx={msg} where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def product_image(msg):
    last=last_element()
    sql1=f"""update def2 set rasm="{msg}" where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()
def mahsulot_4(data):
    last=last_element()
    sql1=f"""update def2 set tarif="{data[1]}" , narx={int(data[2])} , rasm="media/{data[3]}" , name3="{data[0]}" where id={last[-1][0]} """
    cur.execute(sql1)
    con.commit()

print(mahsulot_4(['hetbook','zor',8000,'rasin.jpg']))    
