import flet as ft


def main(page):

    text1 = (ft.Text("Привет!"))
    pole1 = ft.TextField(label="First name", autofocus=True)
    

    page.add(
        text1,
        pole1,
        ft.ElevatedButton("напиши какой нибудь смайлик"),
    )







ft.app(target=main, view=ft.WEB_BROWSER)