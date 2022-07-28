import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()

x = [[1900], [2600], [2200], [2900], [2400], [2300], [2100]]
y = [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]

regr.fit(x, y) #학습

y_pred = regr.predict(x) #x를 입력값으로 하여 예측

#1. 총중량이 2,500kg일 때, 연비를 예측해보세요.
pred =  regr.predict([[2500]])

print("총 중량 2500일 때, 예측값 :", pred)

#총 중량 2500일 때, 예측 값 마커로 표시
plt.scatter(2500, pred, marker='^', color='orange')


#2. matplotlib 라이브러리 사용하여 학습데이터와 결과값을 산포도로 그리세요.
plt.scatter(x, y, color='red')


#3. 학습 데이터와 예측값으로 선그래프를 그리세요.
plt.plot(x, y_pred, color='black') 

plt.show()