import flet as ft

def main(page):
    candles = []
    selected_index = None  # Variable para rastrear el índice seleccionado

    def add_clicked(e):
        if new_candle.value:
            candles.append(new_candle.value)
            update_candle_list()
            new_candle.value = ""
            new_candle.focus()
            new_candle.update()

    def modify_clicked(e):
        if selected_index is not None and new_candle.value:
            candles[selected_index] = new_candle.value
            update_candle_list()
            new_candle.value = ""
            new_candle.focus()
            new_candle.update()

    def delete_clicked(e):
        nonlocal selected_index  # Usar la variable externa
        if selected_index is not None:
            candles.pop(selected_index)  # Eliminar la vela seleccionada
            selected_index = None  # Reiniciar el índice seleccionado
            update_candle_list()
            new_candle.value = ""  # Limpiar el campo de texto después de eliminar
            new_candle.update()

    def update_candle_list():
        candle_list.controls.clear()
        for i, candle in enumerate(candles):
            checkbox = ft.Checkbox(label=candle, value=False)
            checkbox.on_change = lambda e, index=i: candle_list_select(index)
            candle_list.controls.append(checkbox)
        candle_list.update()

    def candle_list_select(index):
        nonlocal selected_index  # Usar la variable externa
        selected_index = index  # Actualizar el índice seleccionado
        new_candle.value = candles[selected_index]  # Llenar el campo de texto con la vela seleccionada
        new_candle.update()

    new_candle = ft.TextField(hint_text="Añade tu vela aromática", width=300)

    logo = ft.Image(src="img/cafe.png", width=150, height=150)
    header_text = ft.Text("BIENVENIDOS A LA TIENDA DE VELAS AROMÁTICAS", size=20, weight=ft.FontWeight.BOLD)
    header = ft.Column(
        controls=[logo, header_text],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los elementos del encabezado
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alineación horizontal centrada
    )

    candle_list = ft.Column()  # Para listar las velas

    page.add(
        ft.Column(
            controls=[
                header,
                ft.Divider(height=20),
                ft.Row(
                    controls=[new_candle, ft.ElevatedButton("Agregar", on_click=add_clicked)],
                    alignment=ft.MainAxisAlignment.CENTER  # Centrar la fila del campo de texto y botón
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Modificar", on_click=modify_clicked),
                        ft.ElevatedButton("Eliminar", on_click=delete_clicked)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centrar la fila de botones
                ),
                candle_list
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar la columna principal
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alineación horizontal centrada
        )
    )

    # Establecer tamaño de la página
    page.window_width = 600
    page.window_height = 400
    page.update()

ft.app(main)
