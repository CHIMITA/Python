
def showMenu():
    print("----------2022 Starbucks menu-----------")
    print("0. 주문 종료")
    print("1. %s : %s원" % (menu1, price1))
    print("2. %s : %s원"% (menu2, price2))
    print("사이즈 : Tall +%d원, Grande +%d원, Venti +%d원" % (tall, grande, venti))


def selectMenu():
    global coffee
    global breakFlag
    global continueFlag

    menu = int(input("메뉴를 입력하세요 : "))

    if menu == 1:
        print("%s를 선택하셨습니다." % (menu1))
        coffee += price1
    elif menu == 2:
        print("%s를 선택하셨습니다." % (menu2))
        coffee += price2
    elif menu == 0:
        print("주문을 종료합니다.")
        breakFlag = True
    else:
        print("잘못 입력하셨습니다.")
        continueFlag = True

def selectSize():
    global total_price
    global coffee

    size = int(input("사이즈를 선택하세요. (1.tall 2.grande 3.venti) : "))

    if size == 1: #tall
        coffee += tall
        total_price += coffee
    elif size == 2: #grande
        coffee += grande
        total_price += coffee
    elif size == 3: #venti
        coffee += grande
        total_price += coffee
    else:
        print("잘 못 입력하셨습니다.")
    
    print("현재 주문 금액 : %d원 \n" % total_price)

    
def payment():

    cash = int(input("현금을 넣어주세요 : "))

    change = cash - total_price
    print("잔돈 %d입니다. 안녕히 가십시오." % change)

if __name__ == "__main__":
    menu1 = "아메리카노"
    menu2 = "카페라떼"

    price1 = 4100
    price2 = 4600

    tall = 0
    grande = 500
    venti = 1000

    total_price = 0

    breakFlag = False


while True:
    continueFlag = False
    coffee = 0

    showMenu()
    selectMenu()

    if breakFlag == True:
        break
    if continueFlag == True:
        continue
    selectSize()
    
payment()