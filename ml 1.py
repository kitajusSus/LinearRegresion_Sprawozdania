import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dane Y i X
X = np.array([[43.4], [39], [53.6], [47.4],[17.4]])  # Wartości X (L)
Y = np.array([ 1.75, 1.54,2.17,1.92,0.71])  # Wartości Y  (T^2)

# Inicjalizacja modelu regresji liniowej
model = LinearRegression()

# Trenowanie modelu na danych
model.fit(X, Y)

# Predykcja wartości Y dla danych X
Y_pred = model.predict(X)



# Obliczanie współczynników regresji
A = model.coef_[0]
Delta_A = np.sqrt(np.mean((model.predict(X) - Y) ** 2)) / np.sqrt(len(X)) / np.std(X, ddof=1)
B = model.intercept_
Delta_B = np.sqrt(np.mean((model.predict(X) - Y) ** 2)) * np.sqrt(1 / len(X) + np.mean(X ** 2)) / np.std(X, ddof=1)

# Wyświetlanie współczynników regresji
print("Współczynniki regresji:")
print("Współczynnik nachylenia (A):", A)
print("Niepewność współczynnika nachylenia A (Delta_A):", Delta_A)
print("Wyraz wolny (B):", B)
print("Niepewność wyrazu wolnego B (Delta_B):", Delta_B)

#Wstawianie niepewności
#Delta_Y = np.array([0.00] * len(Y))  # Niepewność Y
#Delta_X = np.array([0.0001, 0.0001, 0.0001, 0.0003, 0.0002, 0.0001, 0.0003, 0.0003, 0.00021, 0.0003])  # Niepewność X
# Rysowanie wykresu
plt.errorbar(X.flatten(), Y, fmt='o', color='blue', label='Dane z niepewnościami')
plt.plot(X.flatten(), Y_pred, color='red', linewidth=2, label='Regresja liniowa')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title('Regresja liniowa z niepewnościami')
plt.legend()
plt.grid(True)
plt.show()