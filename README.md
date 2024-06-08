# LinearRegresion_Sprawozdania
Nazwa programu: Regresja liniowa z niepewnościami

Autor: [Krzysztof Bezubik]

Opis:
Program wykonuje regresję liniową na zestawie danych wejściowych, które składają się z par wartości $(X, Y)$. Program może uwzględniaćniepewności zarówno dla wartości $X$, jak i $Y$, co umożliwia bardziej dokładne obliczenie współczynników regresji.

Instrukcja obsługi:
1. Upewnij się, że masz zainstalowane niezbędne biblioteki: matplotlib, numpy, scikit-learn.
2. Wprowadź swoje dane wejściowe w formie tablic numpy dla $X$ i $Y$.
3. Uruchom program w środowisku Python.

Wymagania:
- Python 3.x
- Biblioteki: matplotlib, numpy, scikit-learn

Program wykonuje regresję liniową na zestawie danych wejściowych, które składają się z par wartości $(X, Y)$. Celem regresji liniowej jest znalezienie najlepszego dopasowania liniowego do tych danych. W przypadku tego programu, dodatkowo uwzględniane są niepewności zarówno dla wartości $X$, jak i $Y$, co umożliwia bardziej dokładne obliczenie współczynników regresji.

Działanie programu można podzielić na kilka kroków:

1)Inicjalizacja danych: Wartości $X$ i $Y$ są wczytywane jako tablice numpy. Każda para $(X, Y)$ reprezentuje punkt danych na wykresie.
2)Inicjalizacja modelu: Program inicjalizuje model regresji liniowej, który zostanie użyty do dopasowania liniowego do danych.
3)Trenowanie modelu: Model jest trenowany na dostępnych danych za pomocą metody najmniejszych kwadratów, aby znaleźć najlepsze dopasowanie.
4)Predykcja wartości Y: Na podstawie dopasowania modelu do danych wejściowych, program przewiduje wartości $Y$ dla danych $X$.
5)Obliczanie współczynników regresji: Program oblicza współczynniki regresji, takie jak współczynnik nachylenia ($A$) i wyraz wolny ($B$), a także ich niepewności ($\Delta A$ i $\Delta B$) na podstawie wyników regresji.
6) Wyświetlanie wyników: Wyniki są wyświetlane w konsoli, a także na wykresie, gdzie dane wejściowe są reprezentowane przez niebieskie punkty z odpowiednimi niepewnościami, a dopasowanie modelu jest reprezentowane przez czerwoną linię.
