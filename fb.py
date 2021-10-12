from datetime import datetime
import fdb
import time


default = None
action = 'open_door, 0'

start = time.time()
con = fdb.connect(dsn='127.0.0.1:C:/Electra/El-Ac/train.fdb',
                  user='SYSDBA',
                  password='masterkey',
                  charset='WIN1251')
end = time.time() - start
print(f'Коннект за {end}')

cur = con.cursor()
select = "select max(id) +1 as ID from d_commands"
cur.execute(select)
num = cur.fetchone()[0]
date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

cur.execute(f"insert into d_commands (executor, text, phis_addr) values ({int(1)}, {str(action)}, {int(-1062731554)})")

cur.execute(f"insert into d_commands values {(num, date_and_time, 1, 'open_door,0', -1062731554)}")


con.commit()
