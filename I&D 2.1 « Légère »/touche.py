import keyboard

while True:
	touche = keyboard.read_event(suppress = True)
	if touche.event_type == keyboard.KEY_DOWN:
		print("Caractère saisi :", touche.name)

		if touche.name == 'q':
			break
