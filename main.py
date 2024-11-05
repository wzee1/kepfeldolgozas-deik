from opencvFunctions import *

def main():
    path = input("Adja meg a kép teljes elérési útvonalát: ")

    # 1. Kép beolvasása és megjelenítése
    load_and_display_image(path, rgb=True)  # RGB módban

    # 2. Kép tulajdonságainak lekérdezése
    get_image_properties(path, rgb=True)

    # 3. Színtér átalakítása és érték módosítása
    color_space_conversion_and_modify_values(path)

    # 4. Sötét kép világosítása
    brighten_image(path)

    # 5. Színkorrekció
    color_correction(path)

    # 6. Szaturáció beállítása felhasználói input alapján
    saturation_modifier = int(input("Adja meg a szaturáció módosításának százalékos értékét (0-100): "))
    color_adjustment_with_user_input(path, saturation_modifier)

    # 7. Hisztogram egyenlősítés
    histogram_equalization(path)

    # 8. Kép szerkesztése felhasználói input alapján
    edit_image_with_user_input()

    # 9. Otsu-féle küszöbölés
    otsu_thresholding()

    # 10. Adaptív küszöbölés
    adaptive_thresholding(path)

    # 11. Morfológiai műveletek
    morphological_operations(path)

    # 12. Canny élkeresés
    canny_edge_detection(path)

    # 13. Tophat és Blackhat transzformációk
    tophat_blackhat_operations(path)

    # 14. Kontúrok felismerése és megjelenítése
    contour_detection(path)

    # 15. Unsharp masking
    unsharp_masking(path)

if __name__ == "__main__":
    main()
