from CommonClient import ClientCommandProcessor, CommonContext, logger


class DKCRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    def _cmd_squawks(self) -> None:
        """
        Toggling Squawks once you unlocked him.
        """
        self.ctx.toggle_squawks()