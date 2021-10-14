import fdb
import time
from datetime import datetime


con = fdb.connect(dsn='127.0.0.1:C:/Electra/El-Ac/train.fdb',
                  user='SYSDBA',
                  password='masterkey',
                  charset='WIN1251')

default = None
action = 'open_door, 0'



def add_event(name_id):
    try:
        cur = con.cursor()
        cur.execute(f"insert into events (system_type, event_type, param1, param2) values ({int(2)}, {int(400)}, {int(38)}, {int(name_id)})")
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()
        # pass


def cond():
    cond = con.event_conduit(['d_new_command'])
    cond.begin()
    res = cond.wait()
    print(res)
    cond.close()
    con.close()


def open_door():
    try:
        cur = con.cursor()
        select = "select max(id) +1 as ID from d_commands"
        cur.execute(select)

        cur.execute(f"insert into d_commands (executor, text, phis_addr) values ({int(1)}, '{str(action)}', {int(-1062731554)})")
        con.commit()

    except Exception as e:
        print(e)
        # pass

    finally:
        con.close()


add_event(5118)
# open_door()
# cond()

