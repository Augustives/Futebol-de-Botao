
class Gol:
    def verifica_gol(self, bola):
        x, y = bola.body.position
        if x > 440 and x <443 and y > 255 and y < 510:
            return 1
        elif x > 1270 and x < 1273 and y > 255 and y < 510:
            return 2