from nicegui import ui
ui.label("DebugShip")
ui.button('Debug', on_click=lambda: ui.notify('Debugging...'), open("ShipFramework.sh"))
