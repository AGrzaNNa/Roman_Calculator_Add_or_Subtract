OPIS ROZWIĄZANIA

Do rozwiązania tego zadania użyłem słownika o nazwie romans, który przechowuje wartości symboli rzymskich wraz z ich odpowiednikiem w zapisie arabskim do M: 1000 .

Działanie programu rozpoczyna się od pobrania ciągu tekstu jako values i podzielenia go za pomocą .split() na trzy wartości: romans_1, romans_2 oraz znak_działania(values[1]). Następnie, w zależności od znak_działania(values[1]), program przechodzi do odpowiedniej pętli: Add (dodawanie) lub Subtraction (odejmowanie).

W obu pętlach, iterujemy po poszczególnych znakach liczb za pomocą pętli for, przez długość tych liczb
(len(romans_1) - 1). Dla każdego znaku sprawdzamy, czy kolejny znak jest większy od obecnego. Jeśli tak, odejmujemy wartość obecnego znaku od wyniku. W przeciwnym razie, dodajemy wartość znaku do wyniku.

Przykład CXL :
result = 100
i++
XL X<L
result-=10 //90
result+=50 //140

Następnie, wynik działania jest przekazywany do funkcji convert_to_roman, która przekształca zapis arabski na zapis rzymski. W tej funkcji znajduje się pętla, która iteruje przez pary wartość-symbol w słowniku roman_numerals. Dla każdej pary, pętla sprawdza, czy podana liczba jest większa lub równa wartości. Jeśli tak, dodaje odpowiedni symbol do łańcucha roman i odejmuje wartość od liczby. Pętla wykonuje się tak długo, jak długo liczba jest większa lub równa aktualnej wartości.

Na koniec, funkcja convert_to_roman zwraca ostateczny wynik w zapisie rzymskim. W przypadku błędnego znaku działania, próby odejmowania większej liczby od mniejszej lub wyniku równego zero, program zwraca odpowiednie komunikaty błędu.

W ten sposób, program przeprowadza dodawanie i odejmowanie liczb w zapisie rzymskim, dostarczając wynik w tym samym formacie.
