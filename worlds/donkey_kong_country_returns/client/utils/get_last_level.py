from ...client.dkcr_game import DKCRGame

async def get_last_level(dkcr: DKCRGame):
    return dkcr.get_current_world(), dkcr.get_current_level()