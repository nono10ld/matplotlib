import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import keyboard

# Charger l'image à partir d'un fichier
image_path = "image.png"
image = plt.imread(image_path)

# Créer une figure et afficher l'image
fig, ax = plt.subplots()
im = ax.imshow(image)

# Créer un cercle initial
circle = patches.Circle((400, 200), 25, color='red', alpha=0.5)
circle2 = patches.Circle((450, 400), 25, color='red', alpha=0.5)
ax.add_artist(circle)
ax.add_artist(circle2)

# Variables de couleur du cercle
red = np.array([1, 0, 0, 0.5])
green = np.array([0, 1, 0, 0.5])

# Fonction pour mettre à jour la couleur du cercle
def update_circle():
    current_color = circle.get_facecolor()
    if np.array_equal(current_color, red):
        circle.set_facecolor(green)
        circle2.set_facecolor(green)
    else:
        circle.set_facecolor(red)
        circle2.set_facecolor(red)
    ax.draw_artist(circle)
    ax.draw_artist(circle2)
    fig.canvas.blit(ax.bbox)

# Fonction pour détecter l'appui sur la touche 'espace'
def on_space(event):
    if event.name == 'space':
        update_circle()

# Connecter la fonction on_space à l'événement d'appui sur la touche 'espace'
keyboard.on_press(on_space)

plt.show()
