import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Kép beolvasása és megjelenítése
def load_and_display_image(path, rgb):
    if (rgb): img = cv2.imread(path, 1)  # 1 --> RGB
    else: img = cv2.imread(path, 0)

    cv2.imshow("picture", img)
    cv2.waitKey()

# 2. Kép tulajdonságainak lekérdezése
def get_image_properties(path, rgb):
    if (rgb): img = cv2.imread(path, 1)  # 1 --> RGB
    else: img = cv2.imread(path, 0)

    print(f"Kép szélessége: {img.shape[0]}")
    print(f"Kép magassága: {img.shape[1]}")
    print(f"Kép csatornák száma: {img.shape[2]}")
    print(f"Kép típusa: {img.dtype}")

# NOTE: Innentől csak rgb-ben fogja megnyitni a képeket

# 3. Színtér átalakítása és érték módosítás: HSV színtérben a színezet (Hue), szaturáció (Saturation) és világosság (Value) értékeket módosítjuk.
def color_space_conversion_and_modify_values(path):
    image = cv2.imread(path, 1)
    hsvImg = cv2.cvtColor(image, cv2.COLOR_RGB2HSV) # RGB TO HSV CONVERT

    newHvalue = int(input("Add meg az új H értéket: "))  
    newSvalue = int(input("Add meg az új S értéket: "))  
    newVvalue = int(input("Add meg az új V értéket: "))  

    h, s, v = cv2.split(hsvImg)
    h = cv2.add(h, newHvalue)
    s = cv2.add(s, newSvalue)
    v = cv2.add(v, newVvalue)

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB) # CONVERT BACK
    cv2.imshow("picture", img)
    cv2.waitKey()

# 4. Sötét kép világosítása
def brighten_image(path, brightnessIncreaseAmount=50):
    image = cv2.imread(path, 1)
    hsvImg = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    h, s, v = cv2.split(hsvImg)
    v = cv2.add(v, brightnessIncreaseAmount)
    final_hsv = cv2.merge((h, s, v))

    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)
    cv2.imshow("picture", img)
    cv2.waitKey()

# 5. Színkorrekció: HSV finomhangolás
def color_correction(path, newHue=10, newSaturation=50, newValue=20):
    image = cv2.imread(path, 1)
    hsvImg = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    h, s, v = cv2.split(hsvImg)
    h = cv2.add(h, newHue)
    s = cv2.subtract(s, newSaturation)
    v = cv2.subtract(v, newValue)

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)
    cv2.imshow("picture", img)
    cv2.waitKey()

# 6. Szaturáció beállítása felhasználói input alapján: A szaturációt módosítjuk, hogy a kép telítettebb vagy fakóbb legyen. ("szürkearányt hány %-ban módosítsa")
def color_adjustment_with_user_input(path, saturation_modifier=50):
    image = cv2.imread(path, 1)

    # Jó értéket biztosítjuk:
    if saturation_modifier < 0: saturation_modifier = 0
    elif saturation_modifier > 100: saturation_modifier = 100

    hsv_img = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv_img)
    modified_s = s * (saturation_modifier / 100)
    modified_s = np.clip(modified_s, 0, 255).astype(np.uint8)

    final_hsv = cv2.merge((h, modified_s, v))
    final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

# 7. Hisztogram egyenlősítés: A kontraszt növelésére szolgál, különösen hasznos, ha a kép szürkeárnyalatos.
def histogram_equalization(path):
    img = cv2.imread(path, 0)
    img_equalized = cv2.equalizeHist(img)

    res = np.hstack((img, img_equalized))
    hist = cv2.calcHist([img_equalized], [0], None, [256], [0, 256])
    
    plt.figure()
    plt.title('Szürkeárnyalatos hisztogram')
    plt.xlabel('Bin-ek')
    plt.ylabel('# pixel')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.ylim([0, 2000])
    plt.show()

# 8. Kép szerkesztése felhasználói input alapján
def edit_image_with_user_input():
    path = input("Adja meg a kép teljes elérési útvonalát: ")
    image = cv2.imread(path, 1)

    # Képkorrekció: Zajcsökkentés + élesítés
    filtered = cv2.GaussianBlur(image, (5, 5), 1.5)
    filtered = cv2.medianBlur(filtered, 5)

    # Küszöbölés: Küszöbértékes bináris maszk létrehozása
    threshold_value = int(input("Adja meg a küszöbölési értéket (0-255): "))
    _, mask = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 0], threshold_value, 255, cv2.THRESH_BINARY)

    # Hue, Saturation, Value
    hue = int(input("Adja meg a színezet változtatási értéket (-180 és 180 között): "))
    saturation = int(input("Adja meg a színtelítettség változtatási értéket (-255 és 255 között): "))
    value = int(input("Adja meg a világosság változtatási értéket (-255 és 255 között): "))

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv[:, :, 0] = cv2.add(image_hsv[:, :, 0], hue)
    image_hsv[:, :, 1] = cv2.add(image_hsv[:, :, 1], saturation)
    image_hsv[:, :, 2] = cv2.add(image_hsv[:, :, 2], value)

    result = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    output_path = input("Adja meg a mentési útvonalat (például result.jpg): ")
    cv2.imwrite(output_path, result, [cv2.IMWRITE_JPEG_QUALITY, 92])
    print(f"A szerkesztett képet elmentettük: {output_path}")

# 9. Otsu-féle küszöbölés (globális)
def otsu_thresholding():
    image = cv2.imread("10-28/pic.jpg", 0)

    # Otsu-féle küszöbölés alkalmazása az optimális küszöbérték meghatározására
    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("Eredeti kép", image)
    cv2.imshow("Otsu-féle küszöbölés", thresholded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 10. Adaptív küszöbölés: akkor hasznos, ha a kép különböző részein eltérő megvilágítási viszonyok vannak. Itt minden rész külön kerül küszöbölésre.
def adaptive_thresholding(path):
    img = cv2.imread(path, 0)  # Szürkeárnyalatos kép betöltése

    # Adaptív küszöbölés alkalmazása helyi fényviszonyokhoz igazodva
    adaptive_thresh = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )

    cv2.imshow("Adaptív küszöbölés", adaptive_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 11. Morfológiai műveletek: dilatáció és erózió
def morphological_operations(path):
    img = cv2.imread(path, 0)  # Szürkeárnyalatos kép betöltése
    kernel = np.ones((5, 5), np.uint8)

    # Dilatáció az objektumok kiterjesztéséhez
    # Dilatáció: egy kép fehér (vagy világos) objektumainak területét növeli
    # Mire használjuk?
    #   - Objektumok összekapcsolására, amelyek között kis távolság van (például megszakadt vonalak vagy határok összefűzésére).
    #   - Kisebb lyukak eltávolítására egy objektumon belül.
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Erózió az objektumok összenyomásához
    # Erózió: a sötét (vagy fekete) területek kibővítése a világosak rovására. Az erózió során a struktúraelem minden fehér pixelt, amelyet teljesen körülvesznek fekete pixelek, feketévé változtat
    eroded = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Eredeti kép", img)
    cv2.imshow("Dilatáció", dilated)
    cv2.imshow("Erózió", eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 12. Élkeresés: Canny élkeresés egy hatékony élkeresési módszer, amelyet körvonalak és élek megtalálásához használhatunk.
def canny_edge_detection(path):
    img = cv2.imread(path, 0)  # Szürkeárnyalatos kép betöltése
    edges = cv2.Canny(img, 100, 200)

    cv2.imshow("Eredeti kép", img)
    cv2.imshow("Canny élkeresés", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 13. Tophat és Blackhat transzformációk: Ezek a műveletek segíthetnek az objektumok csúcspontjainak és mélyedéseinek felismerésében.
def tophat_blackhat_operations(path):
    img = cv2.imread(path, 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

    # Tophat transzformáció a világos csúcspontok kiemelésére
    # Tophat: kiemeli azokat a világos részeket egy képen, amelyek kisebbek vagy keskenyebbek, mint az alkalmazott struktúraelem. A tophat transzformáció a kép és annak nyitott (erózió, majd dilatáció) változatának különbségeként jön létre.
    # Mire használjuk?
    #   - Világos csúcsok és keskeny objektumok kiemelésére, mint például a kép kisebb, kiemelkedő részei.
    #   - Háttérből kiugró, világos objektumok keresésére.
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    # Blackhat transzformáció a sötét mélyedések kiemelésére
    # Blackhat: sötét területeket emel ki a világos háttérrel szemben. A blackhat transzformáció a kép és annak zárt (dilatáció, majd erózió) változatának különbségeként jön létre.
    # Mire használjuk?
    #   - Sötét részek kiemelésére világos háttérrel szemben.
    #   - Mélyedések, árnyékos vagy sötét területek keresésére világos részek között.
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow("Eredeti kép", img)
    cv2.imshow("Tophat transzformáció", tophat)
    cv2.imshow("Blackhat transzformáció", blackhat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 14. Kontúrok felismerése és megjelenítése: Ez a művelet hasznos lehet objektumok körvonalainak azonosítására és vizuális megjelenítésére.
def contour_detection(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Kontúrok felismerése és kirajzolása
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv2.imshow("Kontúrok", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 15. Unsharp masking (élesítés): Ez a módszer a kép részleteinek kiemelésére szolgál.
def unsharp_masking(path):
    img = cv2.imread(path, 0)

    # Homályosítás Gaussian Blur használatával az élesítéshez
    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)

    # Eredeti kép és homályosított változat kombinálása az élesítéshez
    sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

    cv2.imshow("Eredeti kép", img)
    cv2.imshow("Élesített kép", sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Itt kell meghívni a függvényeket
    pass


if __name__ == "__main__":
    main()