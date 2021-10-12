from firebird.driver import connect, DESCRIPTION_NAME, DESCRIPTION_DISPLAY_SIZE

TABLE_NAME = 'events'
SELECT = f'select num from {TABLE_NAME}'

con = connect('train.fdb', user='sysdba', password='masterkey')

cur = con.cursor()
cur.execute(SELECT)


fieldIndices = range(len(cur.description))
for row in cur:
    for fieldIndex in fieldIndices:
        fieldValue = str(row[fieldIndex])
        fieldMaxWidth = cur.description[fieldIndex][DESCRIPTION_DISPLAY_SIZE]

        print(fieldValue.ljust(fieldMaxWidth), end='')

    print() # Finish the row with a newline