import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) -1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) +1)
        page.update()

    def button_clicked(e):
        page.add(ft.Row([
            ft.Text('Clicked!'),
            ],
            alignment=ft.MainAxisAlignment.CENTER),
        )

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.TextField(label="Name:"),
            ft.ElevatedButton(text="Say my name!", on_click=button_clicked),
        ],
        alignment= ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)
