from nicegui import ui
import os
# Create a label
ui.label("DebugShip")

# Create a button with an action
ui.button('Debug', on_click=lambda: [ui.notify('Debugging...'), open ("openkitty.sh")])
# Start the NiceGUI application
ui.run()
