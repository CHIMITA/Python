
class Car:
    speed = 0
    def upspeed(self,value):
        self.speed += value
        print("현재 속도(Car 클래스) : %d" %self.speed)

class Sedan(Car):
    seat = 5

    def upspeed(self,value): #메소드 오버라이딩(재정의)
        self.speed += value 

        if self.speed > 150:
            self.speed = 150

        print("현재 속도(Sedan 클래스) : %d" %self.speed)

    def getseat(self):
        return self.seat

class Truck(Car):
    freight = 1000
    def getfrg(self):
        return self.freight

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭-->", end="")
truck1.upspeed(200)
print("  적재량 :", truck1.getfrg())

print("승용차-->", end="")
sedan1.upspeed(200)
print("  좌석수 :", sedan1.getseat())