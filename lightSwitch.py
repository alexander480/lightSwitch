from guizero import App, Window, PushButton, Slider
from lifxlan import *

lifx = LifxLAN(2)
lights = lifx.get_lights()

def info():
    color = lights[0].get_color()
    info = {"HUE": color[0], "SATURATION": color[1], "BRIGHTNESS": color[2], "KELVIN": color[3]}
    return info

def openToggle():
    app.hide()
    toggleWindow = Window(app, title="Toggle", width=125, height=225, layout="auto")

    def brightness(value):
        for light in lights:
            light.set_brightness(value)
        print("BRIGHTNESS UPDATED: " + str(info()["BRIGHTNESS"]))

    def toggle():
        state = lights[0].get_power()
        if state > 0:
            for light in lights:
                light.set_power("off")
            print("STATE UPDATED: OFF")
            toggleButton.text = "ON"
        else:
            for light in lights:
                light.set_power("on")
                light.set_brightness(float(slider.value))
            print("STATE UPDATED: ON")
            toggleButton.text = "OFF"

    def openMenu():
        toggleWindow.hide()
        app.show()

    slider = Slider(toggleWindow, start=65535, end=0, command=brightness, horizontal=False, width="20", height="fill", align="left")
    toggleButton = PushButton(toggleWindow, text="POWER", width="50", height="fill", align="right", command=toggle)
    ## menuButton = PushButton(toggleWindow, text="Menu", align="right", command=openMenu)

app = App(title="Welcome Window", width=100, height=100)
toggleButton = PushButton(app, text="Toggle", command=openToggle)

## colorButton = PushButton(app, command=open_color)
app.display()
