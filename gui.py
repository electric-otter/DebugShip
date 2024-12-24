from nicegui import ui

# Create a label
ui.label("DebugShip")

# Create a button with an action
ui.button('Debug', on_click=lambda: [ui.notify('Debugging...'), open("ShipFramework.sh")])
# Start the NiceGUI application
ui.run()
