import sqlite3

poem = '''누구를 위해 누군가
        기도하고 있나 봐
        숨죽여 쓴 사랑시가
        낮게 들리는 듯해
        너에게로 선명히 날아가
        늦지 않게 자리에 닿기를'''

con,cur=None,None
onechar,count="",0

con = sqlite3.connect("C:\\Users\\User\\Desktop\\sangilDB")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS poemTB")
cur.execute("CREATE TABLE poemTB(onechar char(1), count INT)")

for ch in poem:
    if 'ㄱ' <= ch <= '힣':
        cur.execute("SELECT * FROM poemTB WHERE onechar = '" + ch + "'")
        row = cur.fetchone()

        if row == None:
            cur.execute("INSERT INTO poemTB VALUES ('" + ch + "'," + str(1) + ")")
        else:
            cnt = row[1]
            cur.execute("UPDATE poemTB SET count = " + str(cnt + 1) + " WHERE ONECHAR = '" + ch +"'")
con.commit()

cur.execute("SELECT * FROM poemTB ORDER BY count DESC")
print("원문\n", poem)
print("-" * 10)
print("문자\t 빈도수")
print("-" * 10)

while(True):
    row = cur.fetchone()
    if row == None:
        break
    ch = row[0]
    cnt = row[1]
    print("%4s %5d" %(ch, cnt))

con.close()