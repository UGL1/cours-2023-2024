import flet as ft
from game import *


def main(page: ft.Page):
    def play(element: ft.ControlEvent):
        value = int(element.control.text) - 1
        if value in possibilites:
            button_list[value].disabled = True
            liste_nombres_restants.remove(value)



        page.update()

    rows = []
    button_list = []
    for i in range(10):
        row = []
        for j in range(10):
            label = str(10 * i + j + 1)
            button = ft.OutlinedButton(text=label, width=75, on_click=play)
            row.append(button)
            button_list.append(button)
        rows.append(ft.Row(controls=row))
    page.add(*rows)
    page.title = "Juniper Green"
    page.update()




ft.app(target=main)
