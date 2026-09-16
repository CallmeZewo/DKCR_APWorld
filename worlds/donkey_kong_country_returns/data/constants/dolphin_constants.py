from enum import StrEnum

class DolphinStatus(StrEnum):
    CONNECTION_REFUSED_GAME_STATUS = \
        "Dolphin failed to connect. Please load a compatible ROM for 'Donkey Kong Country Returns'. Trying again in 5 seconds..."

    CONNECTION_REFUSED_SAVED_STATUS = \
        "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."

    CONNECTION_LOST_STATUS = \
        "Dolphin connection was lost. Please restart your emulator and make sure Donkey Kong Country Returns is running."

    CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
    CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."