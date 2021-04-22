import sqlite3
'''
con = sqlite3.connect("C:\\Users\\User\\Python")

cur = con.cursor()

cur.execute("CREATE TABLE studentTB (id char(5), name char(15), email char(15), birthyear int)")
cur.execute("INSERT INTO studentTB VALUES('30201','Anne','30201@naver.com',2003)")
cur.execute("INSERT INTO studentTB VALUES('30202','Rachel','30202@naver.com',2004)")
cur.execute("INSERT INTO studentTB VALUES('30203','James','30203@naver.com',2005)")
cur.execute("INSERT INTO studentTB VALUES('30204','Cindy','30204@naver.com',2006)")

con.commit()
con.close()

'''

con = sqlite3.connect("C:\\Users\\User\\Python")

cur = con.cursor()

while(True):
    data1 = input("학번 입력 :")
    if data1 == "":
        break
    data2 = input("이름 입력 :")
    data3 = input("e-mail 입력 :")
    data4 = input("출생년도 입력 :")

    sql = "INSERT INTO studentTB VALUES(" + data1 + "','" + data2 + "','"+ data3 + "','" + data4 +")"
    
    cur.execute(sql)
con.commit()
con.close()
