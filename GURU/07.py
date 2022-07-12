def updateQty(age):
    global fare_qty

    if age >= 65:
        fare_qty[0] += 1
    elif age >= 18:
        fare_qty[1] += 1
    elif age >= 8:
        fare_qty[2] += 1
    else:
        fare_qty[3] += 1


def showQty():
    for i in range(0, num_type):
        print("%s %d원 : %d명" % (fare_type[i], fare[i], fare_qty[i]))


if __name__ == "__main__":

    fare_type = ["경로", "성인", "청소년", "아동"]
    num_type = len(fare_type)

    fare = [3000, 5000, 2000, 1000]
    fare_qty = [0, 0, 0, 0]

    total_fare = 0

    print("======= 입장료 =======")
    for i in range(0, num_type):
        print("%s : %d원" % (fare_type[i], fare[i]))
    print("====================\n")

while True:
    age = int(input("\n나이를 입력하세요 (종료 버튼 -1) : "))

    if age == -1:
        break

    updateQty(age)
    showQty()

for i in range(0, num_type):
    total_fare += fare[i] * fare_qty[i]

print("총 금액은 %d원 입니다. \n" % total_fare)