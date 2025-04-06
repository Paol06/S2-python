import tkinter as tk
import json

color1 = "black"
color2 = "#ff1b2d"
taille_carre = 10
larg, haut = 900, 700
nb_fourmis = 2
x, y = 33, 33
pos_x = [33, 45]
pos_y = [33, 45]
posx_init = [33, 45]
posy_init = [33, 45]
indice = 0
speed = 10
itération = 0
direction1 = "n"
direction2 = "n"
direction = ["n", "n"]
direction_init = ["n", "n"]

pauses = True
cases = []
couleur = []
fourmis = []


window = tk.Tk()
window.title("Fourmi de Langton")
window.config(bg="#0a0a0a")
canva = tk.Canvas(window, width=larg, height=haut, bd=0, highlightthickness=0)


# Création du quadrillage avec un répertoire pour les cases. (liste cases)
for i in range(larg // taille_carre):
    colonnes = []
    colonnes_couleur = []
    for j in range(haut // taille_carre):
        x0 = i * 10
        y0 = j * 10
        x1 = (i+1) * 10
        y1 = (j+1) * 10
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="#251F33",
                                       fill=color1, width=1)
        colonnes.append(carre)
        colonnes_couleur.append(0)
    cases.append(colonnes)
    couleur.append(colonnes_couleur)

# Liste permettant de vérifier la couleur de la case.
couleur[x][y] = 0


def fleche(dir):
    """Oriente la fourmi selon la direction souhaitée"""
    global x, y
    if dir == "w":
        coor = (x * 10 + 2, y * 10 + 5, x * 10 + 8, y * 10 + 2,
                x * 10 + 6, y * 10 + 5, x * 10 + 8, y * 10 + 8)
    elif dir == "e":
        coor = (x * 10 + 8, y * 10 + 5, x * 10 + 2, y * 10 + 2,
                x * 10 + 4, y * 10 + 5, x * 10 + 2, y * 10 + 8)
    elif dir == "n":
        coor = (x * 10 + 5, y * 10 + 2, x * 10 + 2, y * 10 + 8,
                x * 10 + 5, y * 10 + 6, x * 10 + 8, y * 10 + 8)
    elif dir == "s":
        coor = (x * 10 + 5, y * 10 + 8, x * 10 + 2, y * 10 + 2,
                x * 10 + 5, y * 10 + 4, x * 10 + 8, y * 10 + 2)
    return coor


def fleche_init(dir, x, y):
    """Oriente la fourmi selon la direction souhaitée"""
    if dir == "w":
        coor = (x * 10 + 2, y * 10 + 5, x * 10 + 8, y * 10 + 2,
                x * 10 + 6, y * 10 + 5, x * 10 + 8, y * 10 + 8)
    elif dir == "e":
        coor = (x * 10 + 8, y * 10 + 5, x * 10 + 2, y * 10 + 2,
                x * 10 + 4, y * 10 + 5, x * 10 + 2, y * 10 + 8)
    elif dir == "n":
        coor = (x * 10 + 5, y * 10 + 2, x * 10 + 2, y * 10 + 8,
                x * 10 + 5, y * 10 + 6, x * 10 + 8, y * 10 + 8)
    elif dir == "s":
        coor = (x * 10 + 5, y * 10 + 8, x * 10 + 2, y * 10 + 2,
                x * 10 + 5, y * 10 + 4, x * 10 + 8, y * 10 + 2)
    return coor


for i in range(nb_fourmis):
    fleches = canva.create_polygon(fleche_init(direction[i], posx_init[i],
                                   posy_init[i]), width=0,
                                   fill="lightblue")
    fourmis.append(fleches)


def passage_mural(k):
    """permet une meilleur lecture du programme
       pour faire passer la bordure à la fourmis"""
    global pos_x, pos_y, x, y
    if pos_y[k] > haut // taille_carre - 1:
        pos_y[k] = 0
    elif pos_x[k] > larg // taille_carre - 1:
        pos_x[k] = 0
    elif pos_y[k] < 0:
        pos_y[k] = haut // taille_carre - 1
    elif pos_x[k] < 0:
        pos_x[k] = larg // taille_carre - 1


def droite(k):
    global direction2, pos_x, pos_y, direction
    if direction2 == "s":
        direction[k] = "w"
        pos_x[k] -= 1
    elif direction2 == "w":
        direction[k] = "n"
        pos_y[k] -= 1
    elif direction2 == "n":
        direction[k] = "e"
        pos_x[k] += 1
    elif direction2 == "e":
        direction[k] = "s"
        pos_y[k] += 1


def gauche(k):
    global direction2, pos_x, pos_y, direction
    if direction2 == "s":
        direction[k] = "e"
        pos_x[k] += 1
    elif direction2 == "w":
        direction[k] = "s"
        pos_y[k] += 1
    elif direction2 == "n":
        direction[k] = "w"
        pos_x[k] -= 1
    elif direction2 == "e":
        direction[k] = "n"
        pos_y[k] -= 1


def pause():
    """Met en pause et restart lorsqu'on appuis une deuxiemme fois"""
    global pauses
    if itération == 0:
        pauses = True
    if pauses is False:
        pauses = True
    elif pauses is True:
        pauses = False

    deplacement()


def pause_reverse():
    """Met en pause et restart la fonction reverse"""
    global pauses
    if pauses is True:
        pauses = False
    elif pauses is False:
        pauses = True

    reversse()


def deplacement():
    """Programme le mouvement de la fourmi"""
    global x, y, direction2, itération, fourmis, indice
    global pos_x, pos_y, direction
    if pauses is False:
        for i in range(nb_fourmis):
            indice = i
            x = pos_x[i]
            y = pos_y[i]
            direction2 = direction[i]
            canva.delete(fourmis[i])
            if couleur[x][y] == 0:
                canva.itemconfig(cases[x][y], fill=color2)
                couleur[x][y] = 1
                droite(indice)
            elif couleur[x][y] == 1:
                canva.itemconfig(cases[x][y], fill=color1)
                couleur[x][y] = 0
                gauche(indice)
            fourmis[i] = canva.create_polygon(fleche(direction[i]), width=0,
                                              fill="lightblue")
            passage_mural(indice)
        canva.after(speed, deplacement)
        itération += 1
        nmb.config(text=f"Itération: {itération}")


def reversse():
    """Retourne aux étapes précédentes"""
    global x, y, direction2, itération, fourmis, pos_x, pos_y
    if pauses is False and itération >= 1:
        for i in range(nb_fourmis):
            indice = i
            x = pos_x[i]
            y = pos_y[i]
            direction2 = direction[i]
            canva.delete(fourmis[i])
            if direction2 == "n":
                pos_y[i] += 1
                passage_mural(indice)
                y = pos_y[i]
                if couleur[x][y] == 0:
                    canva.itemconfig(cases[x][y], fill=color2)
                    couleur[x][y] = 1
                    direction[i] = "e"
                elif couleur[x][y] == 1:
                    canva.itemconfig(cases[x][y], fill=color1)
                    couleur[x][y] = 0
                    direction[i] = "w"
            elif direction2 == "w":
                pos_x[i] += 1
                passage_mural(indice)
                x = pos_x[i]
                if couleur[x][y] == 0:
                    canva.itemconfig(cases[x][y], fill=color2)
                    couleur[x][y] = 1
                    direction[i] = "n"
                elif couleur[x][y] == 1:
                    canva.itemconfig(cases[x][y], fill=color1)
                    couleur[x][y] = 0
                    direction[i] = "s"
            elif direction2 == "e":
                pos_x[i] -= 1
                passage_mural(indice)
                x = pos_x[i]
                if couleur[x][y] == 0:
                    canva.itemconfig(cases[x][y], fill=color2)
                    couleur[x][y] = 1
                    direction[i] = "s"
                elif couleur[x][y] == 1:
                    canva.itemconfig(cases[x][y], fill=color1)
                    couleur[x][y] = 0
                    direction[i] = "n"
            elif direction2 == "s":
                pos_y[i] -= 1
                passage_mural(indice)
                y = pos_y[i]
                if couleur[x][y] == 0:
                    canva.itemconfig(cases[x][y], fill=color2)
                    couleur[x][y] = 1
                    direction[i] = "w"
                elif couleur[x][y] == 1:
                    canva.itemconfig(cases[x][y], fill=color1)
                    couleur[x][y] = 0
                    direction[i] = "e"
            fourmis[i] = canva.create_polygon(fleche(direction[i]), width=0,
                                              fill="lightblue")
        canva.after(speed, reversse)
        itération -= 1
        nmb.config(text=f"Itération: {itération}")


def skipe():
    """Avance le programme d'une itération"""

    global pauses

    for i in range(1):
        pauses = False
        deplacement()
    pauses = True


def undoo():
    """Retourne à l'itération précédente"""
    global pauses
    for i in range(1):
        pauses = False
        reversse()
    pauses = True


def reset():
    """Fonction qui reconfigure la grille, dans la situation initiale"""
    global pauses, x, y, direction2, itération, speed, pos_y, pos_x
    global direction, fourmis, fleches
    print(direction_init)
    for b in range(nb_fourmis):
        canva.delete(fourmis[b])
    for m in range(nb_fourmis):
        fourmis[m] = canva.create_polygon(fleche_init(direction_init[m],
                                          posx_init[m], posy_init[m]), width=0,
                                          fill="lightblue")
    for i in range(len(cases)):
        for j in range(len(cases[0])):
            canva.itemconfig(cases[i][j], fill=color1)
            couleur[i][j] = 0
    x, y = 33, 33
    pos_x = [33, 45]
    pos_y = [33, 45]
    direction = ["n", "n"]
    print(pos_x, posx_init)
    pauses = True
    itération = 0
    speed = 10
    direction2 = direction1
    nmb.config(text=f"Itération: {itération}")
    vitesse.config(text=f"Tps/Itérations: {speed}")


def moins():
    """Réduit la vitesse de la fourmi"""

    global speed, itération
    if speed >= 2:
        speed -= 1
    else:
        speed == speed
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def plus():
    """Augmente la vitesse de la fourmi"""
    global speed, itération
    speed += 1
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def sauvegarde():
    """permet de sauvegarder la grille """
    global pauses, etat_fourmis
    pauses = True
    etat_fourmis = {"couleurs_bg": color1, "couleurs_cases": color2,
                    "coord_x": pos_x, "coord_y": pos_y,
                    "itérations": itération,
                    "direction1": direction1, "direction": direction,
                    "vitesse": speed, "couleur_cases2": couleur}

    fichier = open('donnee_grille.json', 'w')

    json.dump(etat_fourmis, fichier)
    print("sauvegarde de la grille ")
    fichier.close()


def charger():
    """permet de recharger la grille """
    global etat_fourmis, color1, color2, x, y, itération, pos_x, pos_y
    global direction1, direction, speed, couleur, cases
    global fourmis, pauses
    pauses = True
    for k in range(nb_fourmis):
        canva.delete(fourmis[k])


    fichier = open('donnee_grille.json', 'r')
    # données = fichier.read()
    etat_fourmis = json.load(fichier)
    fichier.close()

    color1 = etat_fourmis["couleurs_bg"]
    color2 = etat_fourmis["couleurs_cases"]
    pos_x = etat_fourmis["coord_x"]
    pos_y = etat_fourmis["coord_y"]
    itération = etat_fourmis["itérations"]
    direction1 = etat_fourmis["direction1"]
    direction = etat_fourmis["direction"]
    speed = etat_fourmis["vitesse"]
    couleur = etat_fourmis["couleur_cases2"]

    for z in range(nb_fourmis):
        fourmis[z] = canva.create_polygon(fleche_init(direction[z],
                                          pos_x[z], pos_y[z]), width=0,
                                          fill="lightblue")




    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")
    for i in range(len(cases)):

        for m in range(len(cases[i])):
            if couleur[i][m] == 0:
                canva.itemconfig(cases[i][m], fill=color1)
            else:
                canva.itemconfig(cases[i][m], fill=color2)

    print("chargement de la grille")

# play = tk.Button(window, text="Start", bg="grey", font=("Impact", 14),
#                 bd=0, highlightthickness=0, command=deplacement)


# Reset de la grille
resset = tk.Button(window, text="Reset", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=reset)

# Boutons PLAY/PAUSE et reverse
pausse = tk.Button(window, text="Play/pause", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=pause)
reverse = tk.Button(window, text="Reverse", bg="#251F33",
                    fg=color2, font=("Impact", 14), bd=1,
                    highlightthickness=0, activeforeground="#251F33",
                    activebackground=color2, command=pause_reverse)

# Boutons skip et undo
skip = tk.Button(window, text="Skip", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=skipe)
undo = tk.Button(window, text="Undo", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=undoo)

# Vitesse de la clock
vitesse = tk.Label(text=f"Tps/itération: {speed}ms",
                   bg="#251F33", fg=color2, width=15)
nmb = tk.Label(text=f"Itération: {itération}",
               bg="#251F33", fg=color2, width=15)
vit_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                     font=("Arial", 14), activeforeground="#251F33",
                     activebackground=color2,
                     width=1, height=1, command=plus)
vit_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                      font=("Arial", 14), width=1, height=1,
                      activeforeground="#251F33",
                      activebackground=color2, command=moins)


# Affichage des labels et boutons ci-dessus

resset.grid(row=0, column=1)

skip.grid(row=3, column=0, sticky="n")
undo.grid(row=3, column=0, sticky="s")

pausse.grid(row=2, column=0)
reverse.grid(row=3, column=0, sticky="s", pady=36)

vitesse.grid(row=1, column=0, sticky="s", pady=50, padx=10)
nmb.grid(row=1, column=0, sticky="s", pady=70, padx=10)
vit_moins.grid(row=1, column=0, sticky="s", padx=10)
vit_plus.grid(row=1, column=0, sticky="sw", padx=30)


# afficher un menu en haut à gauche de l'écran

menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="Save", command=sauvegarde)
menu_bar.add_command(label="Load", command=charger)
menu_bar.add_command(label="Quit", command=window.destroy)  # commande

menui.add_cascade(label="File", menu=menu_bar)  # nom du menu

window.config(menu=menui)

canva.grid(column=1, row=1, rowspan=4)
window.mainloop()
