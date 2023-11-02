# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ IMPORT ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
import sys
import time
import turtle
import pygame

# Um Funktionen Parallel laufen zu lassen, erstelle ich ein Thread
from threading import Thread

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ VARIABLEN ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
GOLD_STERNE_GESAMT = 3


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ FUNKTIONEN ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def musik(musik_name):
    if musik_name == "wait":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/warten_auf_antwort.mp3")
        pygame.mixer.music.play(-1, 0.0)

    elif musik_name == "take":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/take.mp3")
        pygame.mixer.music.play(0, 0.0)
        time.sleep(7)

    elif musik_name == "win":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/win.mp3")
        pygame.mixer.music.play(0, 0.0)
        time.sleep(7)

    elif musik_name == "next":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/next.mp3")
        pygame.mixer.music.play(0, 0.0)
        time.sleep(4)

    elif musik_name == "false":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/false.mp3")
        pygame.mixer.music.play(0, 0.0)
        time.sleep(3)

    elif musik_name == "lose_game":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/lose_game.mp3")
        pygame.mixer.music.play(0, 0.0)

    elif musik_name == "start":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/start.mp3")
        pygame.mixer.music.play(0, 0.0)

    elif musik_name == "win_game":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/win_game.mp3")
        pygame.mixer.music.play(0, 0.0)

    elif musik_name == "tipp":
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/tipp.mp3")
        pygame.mixer.music.play(0, 0.0)


def regeln():
    """
    Diese Funktion ruft die Spielregeln formatiert auf.
    """
    print("\n❗<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ ❗ REGELN ❗ ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>❗\n")
    print(" Zum Start haben sie 3 Sterne. Wenn sie keine Sterne mehr haben ist das Spiel zu Ende\n"
          " Eingabe muss wie in einer Prüfung 100 % korrekt sein, so als müsste man es auf ein Blatt papier Schreiben\n"

          "     - Jede richtig beantwortete Frage gibt +3 Sterne.\n"
          "     - Wenn du eine Frage überspringst Kostet es -2 Stern. \n"
          "     - Wenn du ein Tipp aufrufst Kostet es dich -1 Sterne \n"
          "     - Für jede Falsch gemachte Eingabe, wird auch -1 Stern abgezogen. \n"
          "     - Die Groß und Kleinschreibung muss nicht beachtet werden.\n"

          "    !!!Ziel ist es den Quiz komplett bis ende durch zu gehen, ohne das einem die Sterne ausgehen!!!")
    print("❗" + "_" * 100 + "❗")


def menu():
    """
    __________________________________________________________________________________________________
    Diese Funktion ruft den Infokasten für das Menü auf.
    __________________________________________________________________________________________________
    """
    print("\n🚹<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[🚹 MENÜ 🚹]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>🚹\n")
    print("[T] Tipps Anzeigen           ❇\n"
          "[N] Next/Frage Überspringen  ❇\n"
          "[B] Programm sofort Beenden  ❇")
    print("_" * 100, "\n")


def stern_kontrolle(operator, gold_menge):
    """
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[FUNKTIONSBESCHREIBUNG]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    GOLDSTERNE Summieren oder Subtrahieren.
    Gleichzeitig Prüfen wie viele Sterne das sind, wenn 0 dann System Ende
    Par.1 = operator(+, /, - oder *).
    Par.2 = GOLDSTERN Menge.
    Protokolliert die gerechnete Menge.
    Gibt die gesamtanzahl der GOLDSTERNE.
    ___________________________________________________________________________________________________________________
    """

    global GOLD_STERNE_GESAMT

    if operator == "+":
        GOLD_STERNE_GESAMT += gold_menge
        print("Verdient:", operator, gold_menge, gold_menge * "🌟")
        print("💫 GESAMT GOLDSTERNE:", GOLD_STERNE_GESAMT, GOLD_STERNE_GESAMT * "🌟")

    elif operator == "-":
        GOLD_STERNE_GESAMT -= gold_menge
        print("Kostet:", operator, gold_menge, gold_menge * "🌟")
        print("💫 GESAMT GOLDSTERNE:", GOLD_STERNE_GESAMT, GOLD_STERNE_GESAMT * "🌟")

    if GOLD_STERNE_GESAMT <= 0:
        musik("lose_game")
        print("🏳🏳🏳 GAME OVER 🏳🏳🏳")
        time.sleep(7)
        sys.exit("PROGRAMM ENDE")


def tipp_anzeigen(tipp):
    stern_kontrolle("-", 1)
    musik("tipp")
    print("\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<🏴 TIPP 🏴>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(tipp)
    print("-"*100)
    print()
    time.sleep(10)


def fragestellung_formatiert(frage_nr, frage_stellung):
    """
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[FUNKTIONSBESCHREIBUNG]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Diese Funktion erspart uns das Formatieren der Fragestellung bei jeder neuen Frage.
    Andernfalls müsste man bei jeder Fragestellung den in dieser Funktion definierten CODE wiederholen.
    ___________________________________________________________________________________________________________________
    """
    # Fragestellung
    musik("wait")
    print(f"_" * 41, f"✭ Farge Nr. {frage_nr} ✭ ", "_" * 41)
    for zeile in frage_stellung:
        print(f"❓ {zeile:98} ❓")
    print("-"*103, "\n")


def eingabe_annehmen():
    """
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[FUNKTIONSBESCHREIBUNG]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Diese Funktion erleichtert die Eingabe dem Nutzer.
    - eingabe.upper() = Eingabe in Großbuchstaben umwandeln, um die klein-groß-schreibung aus acht zu lassen.
    - eingabe.strip() = Alle Leerzeichen am Anfang und am Ende der Eingabe entfernen
    - Eingabe Protokollieren
    ___________________________________________________________________________________________________________________
    """
    eingabe = input("➥ Eingabe hier: ")
    eingabe = eingabe.upper()
    eingabe = eingabe.strip()
    print("Ihre Eingabe ist:", eingabe)
    return eingabe


def antwort_check(eingabe, losungen):
    """
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[FUNKTIONSBESCHREIBUNG]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Diese Funktion überprüft, ob die Eingabe richtig oder falsch war.
    ___________________________________________________________________________________________________________________
    """

    if eingabe in losungen:
        print("🥳🥳🥳 Das ist Korrekt! 🥳🥳🥳\n")
        stern_kontrolle("+", 3)
        musik("win")
        return False

    else:
        print("_" * 100)
        stern_kontrolle("-", 1)
        print("\n😬 Leider Falsch! 😬\n")
        print("_" * 100)
        musik("false")
        return True


def play(nr, fragestellung, tipp, losungen):
    signal = True
    while signal:
        fragestellung_formatiert(nr, fragestellung)
        eingabe = eingabe_annehmen()
        if eingabe == "T":
            tipp_anzeigen(tipp)
            signal = True

        elif eingabe == "N":
            stern_kontrolle("-", 1)
            musik("next")
            signal = False

        elif eingabe == "B":
            best = input("Der Fortschritt geht dabei verloren möchten sie dennoch beenden? [Y] or [N]: ")
            if best == "Y" or best == "y":
                sys.exit("Programm beendet")
            else:
                pass

        else:
            musik("take")
            signal = antwort_check(eingabe, losungen)


def belohnung():
    wn = turtle.Screen()
    wn.bgcolor("black")
    astroid = turtle.Turtle()
    astroid.speed(0)
    triad = turtle.Turtle()
    triad.speed(0)
    triad.up()
    triad.goto(-120, 120)
    triad.down()
    squad = turtle.Turtle()
    squad.speed(0)
    squad.up()
    squad.goto(120, 120)
    squad.down()
    pentago = turtle.Turtle()
    pentago.speed(0)
    pentago.up()
    pentago.goto(-120, -120)
    pentago.down()
    octago = turtle.Turtle()
    octago.speed(0)
    octago.up()
    octago.goto(120, -120)
    octago.down()
    colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]

    for i in range(50):
        triad.color(random.choice(colors))
        triad.forward(i * 3)
        triad.left(120)

    for i in range(50):
        squad.color(random.choice(colors))
        squad.forward(i * 2)
        squad.left(90)

    for i in range(50):
        pentago.color(random.choice(colors))
        pentago.forward(i * 2)
        pentago.left(72)

    for i in range(75):
        octago.color(random.choice(colors))
        octago.forward(i)
        octago.left(60)

    for i in range(50):
        astroid.color(random.choice(colors))
        astroid.forward(i * 3)
        astroid.left(144)

    triad.up()
    triad.goto(-110, 200)
    triad.down()
    triad.write("Triad")
    triad.hideturtle()

    squad.up()
    squad.goto(120, 180)
    squad.down()
    squad.write("Squad")
    squad.hideturtle()

    pentago.up()
    pentago.goto(-140, -20)
    pentago.write("Pentago")
    pentago.hideturtle()

    octago.up()
    octago.goto(120, -40)
    octago.down()
    octago.write("Hex")
    octago.hideturtle()

    astroid.up()
    astroid.goto(0, 60)
    astroid.down()
    astroid.write("Astroid")
    astroid.hideturtle()


def finale():
    a = 0
    while a < 3:
        a += 1
        print(
            "🌟🌟🌟 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ GRATULIERE ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 🌟🌟🌟")
        print()
        print(
            "🥳🥳🥳 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ DU HAST DEN QUIZ ÜBERLEBT ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 🥳🥳🥳")
        print()

    take_gif = input("☟☟☟<<<<<<<<<<<<<<<<<<< DRÜCKE BELIEBIGE TASTE UM DEIN GESCHENK ZU ÖFFNEN >>>>>>>>>>>>>>>>>>>☟☟☟")
    if take_gif == "":
        pass


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ HAUPTPROGRAMM ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
regeln()
menu()
musik("start")
input("Drücken sie Enter wenn sie Starten möchten: ")
print()

print("💫 GESAMT GOLDSTERNE:", GOLD_STERNE_GESAMT, GOLD_STERNE_GESAMT * "🌟")


# 1.1 Datenbank anlegen_____________________________________________________________________________________________
NR = [1]
FRAGESTELLUNG = ["Mit welchen Befehl kann man eine Datenbank mit dem Namen 'ASD' erstellen?"]

TIPP = ["Was heist Erstellen auf Englisch? Was wollen wir machen, eine Datenbank erstellen."]

LOSUNGEN = ["CREATE DATABASE ASD;", "CREATE DATABASE ASD ;", " CREATE DATABASE ASD;"]
play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 1.2 Existierende Datenbanken anzeigen_____________________________________________________________________________
NR = [2]
FRAGESTELLUNG = ["Mit welchem Befehl werden alle existierenden Datenbanken angezeigt?"]

TIPP = ["Was heist Zeigen auf Englisch? Wir möchten die Datenbanken anzeigen lassen. ****  DATABASES;"]

LOSUNGEN = ["SHOW DATABASES;", "SHOW  DATABASES;", "SHOW  DATABASES;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 1.3 Datenbank löschen_____________________________________________________________________________________________
NR = [3]
FRAGESTELLUNG = ["Um eine Datenbank namens ASD zu löschen, benötigen Sie den Befehl..."]

TIPP = ["Wir möchten die Datenbanken löschen(DROP)"]

LOSUNGEN = ["DROP DATABASE ASD;", "DROP  DATABASE ASD;", "DROP DATABASE  ASD;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 1.3.1 Datenbank löschen___________________________________________________________________________________________
NR = [4]
FRAGESTELLUNG = ["Um vor dem Löschen sicherzustellen dass die Datenbank existiert,"
                 "sollten Sie folgenden Befehl verwenden..."]

TIPP = ["Da Hilft dir IF EXISTS"]

LOSUNGEN = ["DROP DATABASE IF EXISTS ASD;", "DROP  DATABASE IF EXISTS", "DROP DATABASE  IF EXISTS;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 1.4 Datenbank auswählen___________________________________________________________________________________________
NR = [5]
FRAGESTELLUNG = ["Um mit einer Datenbank zu arbeiten, muss diese erst mit *** ausgewählt werden.",
                 "Wählen sie die Datenbank ASD"]

TIPP = ["Um mit einer Datenbank zu arbeiten, muss diese erst mit USE ausgewählt werden."]

LOSUNGEN = ["USE ASD;", "USE  ASD;", "USE  ASD;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 2.1 Tabelle anlegen_________________________________________________________________________________________________
NR = [6]
FRAGESTELLUNG = ["Eine Tabelle ist mit den Namen TAB anzulegen. Zusätzlich zu diesem Befehl müssen der Tabellenname",
                 "und die benötigten Spalten mit den jeweiligen Datentypen angegeben werden."]

TIPP = ["Eine Tabelle kann man mit dem Befehl CREATE TABLE anlegen. Zusätzlich zu diesem Befehl müssen der",
        "Tabellenname und die benötigten Spalten mit den jeweiligen Datentypen angegeben werden.",
        "CREATE TABLE ASD (ID INT NOT NULL, SPALTE1 VARCHAR(50));"]

LOSUNGEN = ["CREATE TABLE ASD (ID INT NOT NULL, SPALTE1 VARCHAR(50));"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 2.2 Existierende Tabellen anzeigen _______________________________________________________________________________
NR = [7]
FRAGESTELLUNG = ["Mit welchen Befehl werden alle existierenden Tabellen von der Datenbank ASD angezeigt."]

TIPP = ["Was heist Zeigen auf Englisch? **** TABLES FROM tabellennamen"]

LOSUNGEN = ["SHOW TABLES FROM ASD;", "SHOW  TABLES FROM ASD ; SHOW TABLES  FROM ASD;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 2.3 Tabelle löschen_______________________________________________________________________________________________
NR = [8]
FRAGESTELLUNG = ["Um eine Tabelle namens ASD zu löschen, benötigen Sie den Befehl..."]

TIPP = ["Genau so wie bei Löschen von Datenbanken. Stichwort: Drop"]

LOSUNGEN = ["DROP TABLES ASD;", "DROP  TABLES ASD; DROP TABLES  ASD;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 2.3.1 Tabelle löschen, wenn Existiert_____________________________________________________________________________
NR = [9]
FRAGESTELLUNG = ["Die Tabelle namens ASD soll nur gelöscht werden, wenn sie Existiert..."]

TIPP = ["Wie bei dem Befehl DROP DATABASE gibt es auch hier die Option IF EXISTS. "]

LOSUNGEN = ["DROP TABLE IF EXISTS ASD;", "DROP  TABLE IF EXISTS ASD;", "DROP TABLE  IF EXISTS ASD;"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# 2.4 Spalte hinzufügen_______________________________________________________________________________________________
NR = [10]
FRAGESTELLUNG = ["Wenn nachträglich noch eine Spalte in eine Tabelle eingefügt werden soll, benötigen Sie den Befehl",
                 "ALTER TABLE mit der Option ADD COLUMN. "]

TIPP = ["SO ist Korrekt: ALTER TABLE asd ADD COLUMN (SPALTE2 CHAR(50));"]

LOSUNGEN = ["ALTER TABLE ASD ADD COLUMN (SPALTE2 CHAR(50));"]

play(NR, FRAGESTELLUNG, TIPP, LOSUNGEN)


# Finale_____________________________________________________________________________________________________________

# Um Funktionen Parallel laufen zu lassen, erstelle ich ein Thread
MUSIK = Thread(target=musik("win_game"))
MUSIK.start()

finale()

FINALE = Thread(target=belohnung)
FINALE.start()

time.sleep(30)
sys.exit("Programm Ende")
