import flet as ft


def main(page):

    text1 = (ft.Text("Привет!"))
    pole1 = ft.TextField(label="First name", autofocus=True)
    greetings = ft.Column()
    row = ft.Row(spacing=0)
    def btn_click(e):
        greetings.controls.append(ft.Text(f"{pole1.value}"))
        pole1.value = ""

        page.update()
        pole1.focus()

    page.add(
        text1,
        pole1,
        ft.ElevatedButton("😁", on_click=btn_click),
        ft.ElevatedButton("😂", on_click=btn_click),
        ft.ElevatedButton("😊", on_click=btn_click),
        ft.ElevatedButton("😒", on_click=btn_click),
        ft.ElevatedButton("😉", on_click=btn_click),
        ft.ElevatedButton("😍", on_click=btn_click),
        ft.ElevatedButton("😘", on_click=btn_click),
        ft.ElevatedButton("👌", on_click=btn_click),
        ft.ElevatedButton("👍", on_click=btn_click),
        ft.ElevatedButton("🤦‍♀️", on_click=btn_click),
        ft.ElevatedButton("🤦‍♂️", on_click=btn_click),
        ft.ElevatedButton("🤷‍♀️", on_click=btn_click),
        ft.ElevatedButton("🤷‍♂️", on_click=btn_click),
        ft.ElevatedButton("😢", on_click=btn_click),
        ft.ElevatedButton("😜", on_click=btn_click),
        ft.ElevatedButton("😎", on_click=btn_click),
        ft.ElevatedButton("👏", on_click=btn_click),
        ft.ElevatedButton("😃", on_click=btn_click),
        row
    )







ft.app(target=main, view=ft.WEB_BROWSER)