# =========================
# INFO O PROJEKCIE
# =========================

INFO = {
    "version": "2.0",
    "date": "25-12-2025",
    "author": "Grzegorz",
    "level": "Gold"
}


# =========================
# DANE (z Silver)
# =========================

LESSON_TOPIC = {
    "Wyrazenia warunkowe": "Zaliczone",
    "If / elif / else": "Poprawka",
    "Funkcje": "Zaliczone",
    "Konwersje typow": "Poprawka",
    "Petla for / while": "Poprawka",
    "Listy": "Zaliczone",
    "Slownik": "Zaliczone",
    "Obliczenia arytmetyczne": "Zaliczone",
    "Logika boolowska": "Zaliczone"
}


# =========================
# FUNKCJE
# =========================

def podziel_tematy(dane):
    """Dzieli tematy na zaliczone i do poprawki"""
    zaliczone = []
    poprawka = []

    for temat, status in dane.items():
        if status == "Zaliczone":
            zaliczone.append(temat)
        elif status == "Poprawka":
            poprawka.append(temat)

    return zaliczone, poprawka


def oblicz_procent(zaliczone, wszystkie):
    """Liczy procent zaliczenia"""
    if wszystkie == 0:
        return 0
    return (zaliczone / wszystkie) * 100


def sprawdz_status_kursu(procent):
    """Decyduje czy kurs zaliczony"""
    if procent < 30:
        return "❌ Kurs NIE zaliczony"
    else:
        return "✅ Kurs ZALICZONY"


def raport(dane):
    """Główna funkcja raportu"""
    zaliczone, poprawka = podziel_tematy(dane)

    liczba_wszystkich = len(dane)
    liczba_zaliczonych = len(zaliczone)

    procent = oblicz_procent(liczba_zaliczonych, liczba_wszystkich)
    status = sprawdz_status_kursu(procent)

    print("\n===== RAPORT NAUKI =====")
    print(f"Tematy ogółem: {liczba_wszystkich}")
    print(f"Zaliczone: {liczba_zaliczonych}")
    print(f"Do poprawki: {len(poprawka)}")
    print(f"Procent zaliczenia: {procent:.2f}%")
    print(status)

    print("\n✔ ZALICZONE:")
    for t in zaliczone:
        print(" -", t)

    print("\n✏ DO POPRAWKI:")
    for t in poprawka:
        print(" -", t)


# =========================
# START PROGRAMU
# =========================

if __name__ == "__main__":
    print("Learning Tracker – GOLD")
    print(INFO)
    raport(LESSON_TOPIC)
