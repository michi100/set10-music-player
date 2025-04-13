import pyxel


class App:
    def __init__(self):
        pyxel.init(500, 360)
        pyxel.mouse(True)
        self.x = 0
        pyxel.load("assets/my_resource.pyxres")

        pyxel.images[0].load(0, 0, "assets/TFT10_Jhin.TFT_Set10.png")
        pyxel.images[1].load(0, 0, "assets/TFT10_Lulu.TFT_Set10.png")
        pyxel.images[2].load(0, 0, "assets/TFT10_Ahri.TFT_Set10.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.stop()
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            if 30 <= mx <= 150 and 30 <= my <= 150:
                pyxel.play(0, [0, 1, 2, 3], loop=False)
            if 180 <= mx <= 300 and 30 <= my <= 150:
                pyxel.play(1, [16], loop=False)
            if 330 <= mx <= 450 and 30 <= my <= 150:
                pyxel.play(2, [32, 33, 34, 35], loop=False)

    def draw(self):
        pyxel.cls(9)
        pyxel.blt(30, 30, 0, 120, 0, 120, 120)
        pyxel.blt(180, 30, 1, 120, 0, 120, 120)
        pyxel.blt(330, 30, 2, 120, 0, 120, 120)
        pyxel.text(30, 160, "Maestro", 0)
        pyxel.text(180, 160, "Hyperpop", 0)
        pyxel.text(330, 160, "K/DA", 0)
        if (
            isinstance(pyxel.play_pos(0), tuple)
            or isinstance(pyxel.play_pos(1), tuple)
            or isinstance(pyxel.play_pos(2), tuple)
        ):
            pyxel.text(180, 240, "Playing...", 0)
        else:
            pyxel.text(180, 240, "Click icon!", 0)


App()
