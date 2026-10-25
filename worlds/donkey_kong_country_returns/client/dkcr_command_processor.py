from CommonClient import ClientCommandProcessor, CommonContext, logger


class DKCRCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_squawks(self) -> None:
        """
        Toggling Squawks once you unlocked him.
        """
        self.ctx.squawks_state = 1 if self.ctx.squawks_state == 0 else 0
        logger.info("Squawks toggled!")

    def _cmd_zero_asked(self) -> None:
        """
        If Zero asks or if you want to report a bug.
        This will give you the custom RAM values currently in your game.
        """
        self.ctx.ram_requested = True