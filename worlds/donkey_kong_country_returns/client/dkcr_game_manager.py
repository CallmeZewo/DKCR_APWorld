def create_game_manager(base_ui):
    class DKCRGameManager(base_ui):
        base_title = "Donkey Kong Country Returns"

        def build(self):
            from kivy.uix.boxlayout import BoxLayout
            from kvui import MDLabel

            container = super().build()

            dkcr_tab = BoxLayout(orientation="vertical")

            dkcr_tab.add_widget(
                MDLabel(text="DEMO [WIP]")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Puzzle Pieces: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Jungle Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Beach Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Ruins Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Cave Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Forest Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Cliff Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Factory Kong Letters: 0/60")
            )

            dkcr_tab.add_widget(
                MDLabel(text="Volcano Kong Letters: 0/60")
            )

            self.add_client_tab("DKCR", dkcr_tab)

            return container
    return DKCRGameManager