### Színmodellek

-  **RGB**: Vörös, Zöld, Kék modell, amely színes képek megjelenítésére szolgál. A színek kombinációja révén széles spektrumot fed le.
-  **HSV**: Színárnyalat, Telítettség és Fényerő modell, amely a színek jellemzésére szolgál a következőképpen:
   -  **H (Színárnyalat)**: A szín körüli pozíciója a színkörön, 0-360° között.
   -  **S (Telítettség)**: A szín intenzitásának mértéke, amely megmutatja, mennyire közel van a szín a szürkéhez.
   -  **V (Fényerő)**: A szín világosságának mértéke, amely a szín fényességét jelzi.

### Kép Dimenziók

-  **Színes Képek**: 3D mátrix (szélesség, magasság, színcsatornák), ahol minden pixel három színcsatorna (R, G, B) értékét tárolja.
-  **Szürke Képek**: 2D mátrix (szélesség, magasság), ahol minden pixel egy szürkeértéket tárol.

### Szűrők

-  **Cél**: Képminőség javítása, élesítés, homályosítás és zajszűrés.
-  **Típusok**:
   -  **Box Szűrő**: Egyszerű átlagoló szűrő, amely a környező pixelek átlagát használja a pixel értékének kiszámításához.
   -  **Gauss Szűrő**: A Gauss eloszlást használja homályosításhoz, ahol a középső pixelhez közelebb eső pixelek nagyobb súlyt kapnak.
      -  **Sigma**: A Gauss-görbe élességét határozza meg; minél nagyobb a sigma, annál erősebb a homályosítás.
   -  **Median Szűrő**: Nem-lineáris szűrő, amely a szomszédos pixelek mediánját használja, így hatékonyan eltávolítja a véletlenszerű zajokat.

### Szűrők Jellemzői

-  **Box és Gauss Szűrők**: Lineáris szűrők, ahol a pixel értékének kiszámítása aritmetikai műveletek alapján történik.
-  **Median Szűrő**: Nem-lineáris, statisztikai művelet, amely a pixelek értékeinek középértékét használja, ezáltal csökkentve a zaj hatását.
-  **Kernel Mérete**:
   -  **Box Szűrő**: Lehet páros a dimenziója, de általában páratlan méretet alkalmazunk a középpont kiemelésére.
   -  **Gauss Szűrő**: Nem lehet páros a dimenziója, hogy a kernel középpontja jól meghatározott legyen.

### Zajcsökkentés

-  Minden szűrő célja a zaj csökkentése:
   -  **Gauss Szűrő**: Jobban megőrzi az éleket a homályosítás során, mivel a szomszédos pixelek súlyozott átlagát veszi figyelembe.
   -  **Box Szűrő**: Gyengébb minőséghez vezethet, mivel minden pixel egyenlő súlyt kap.
   -  **Median Szűrő**: Hatékony a véletlenszerű zaj eltávolításában, különösen a só-és-bors zaj esetén.

### Logikai Műveletek

-  **Bitwise Műveletek**:
   -  **AND**: Két kép közös pixeleinek megtartása.
   -  **OR**: Két kép egyesítése, a nem null értékű pixelek megtartása.
   -  **NOT**: A kép inverzének létrehozása.

### Küszöbölési Technikák

-  **Típusok**:
   -  **Sima**: Kézi küszöbölés, ahol a felhasználó választja ki a küszöbértéket.
   -  **Automatikus**:
      -  **Otsu-módszer**: Globális küszöbölési technika, amely az osztályok közötti variancia maximalizálására törekszik.
   -  **Adaptív**:
      -  Lokális küszöbölés, amely a kép különböző területein eltérő küszöbértékeket használ a változó fényviszonyok miatt.

### Képmanipulációs Technikák

-  **Forgatás**: A kép elforgatása egy meghatározott szögben.
-  **Méretezés**: A kép méretének megváltoztatása (növelés vagy csökkentés).
-  **Elforgatás és Elmozdulás**: A kép elmozdítása vízszintesen vagy függőlegesen.

### További Szűrők

-  **Képkontraszt Növelése**: A kép kontrasztjának javítása a színek közötti eltérés fokozásával.
-  **Élesítés**: A kép részleteinek kiemelése a pixel értékek növelésével, hogy a kép élesebbnek tűnjön.



### Plusz info:
Dilatáció: vastagítás
Erózió: vékonyítás
Nyitás: erózió aztán dilatáció 
Zárás: dilatáció aztán erózió 

Hisztogram: bal oldalon vannak, akkor sotet, jobb oldalon akkor vilagos, ha kozepen akkor kiegyensúlyozott

Custom Kernel használata (például élesítés):
- Ha saját kernel mátrixot akarsz megadni, használhatod a cv2.filter2D függvényt. Például élesítéshez:
"""
import numpy as np

3x3-as élesítő kernel:
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

Custom kernel alkalmazása:
sharpened_image = cv2.filter2D(image, -1, kernel)
"""