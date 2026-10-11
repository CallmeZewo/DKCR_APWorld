import dolphin_memory_engine as dme

from ..data.constants.addresses.general import GeneralAddresses
from ..data.constants.dkcr_version import DKCRVersion


class Dolphin:
    def connect(self) -> bool:
        if self.is_connected():
            return True

        dme.hook()
        return self.is_connected()

    def disconnect(self) -> None:
        if self.is_connected():
            dme.un_hook()

    def is_connected(self) -> bool:
        return dme.is_hooked()

    def get_version(self) -> DKCRVersion | None:
        game_id = dme.read_bytes(GeneralAddresses.GAME_ID, 6)

        if game_id == b"SF8E01":
            return DKCRVersion.NTSC_U_REV_1

        if game_id == b"SF8P01":
            return DKCRVersion.PAL

        return None

    def read_byte(self, address: int) -> int:
        return dme.read_byte(address)

    def read_bytes(self, address: int, size: int) -> bytes:
        return dme.read_bytes(address, size)

    def read_word(self, address: int) -> int:
        return dme.read_word(address)

    def write_byte(self, address: int, value: int) -> None:
        dme.write_byte(address, value)

    def write_bytes(self, address: int, value: bytes) -> None:
        dme.write_bytes(address, value)

    def write_word(self, address: int, value: int) -> None:
        dme.write_word(address, value)

    def read_add_write_word(self, address: int, increment_value: int) -> None:
        """Adding a word to the specified address"""
        base_value = self.read_word(address)
        self.write_word(address, base_value + increment_value)

    def read_add_write_byte(self, address: int, increment_value: int) -> None:
        """Adding a byte to the specified address"""
        base_value = self.read_byte(address)
        self.write_byte(address, base_value + increment_value)

    def read_add_write_bytes(self, address: int, size: int , increment_value: int) -> None:
        """Adding to bytes at the specified address"""
        base_value = int.from_bytes(self.read_bytes(address, size))
        result = (base_value + increment_value).to_bytes(size)
        self.write_bytes(address, result)

    def read_or_write_word(self, address: int, operation_value: int) -> None:
        """And a word with a value and save it to a specified address"""
        base_value = self.read_word(address)
        self.write_word(address, base_value | operation_value)

    def read_or_write_byte(self, address: int, operation_value: int) -> None:
        """And a byte with a value and save it to a specified address"""
        base_value = self.read_byte(address)
        self.write_byte(address, base_value | operation_value)

    def read_or_write_bytes(self, address: int, size: int , operation_value: bytes) -> None:
        """And bytes with a value and save it to a specified address"""
        base_value = self.read_bytes(address, size)
        if len(base_value) != len(operation_value):
            raise ValueError("Current bitfield and operation value must have the same length.")
        result = bytes(a | b for a, b in zip(base_value, operation_value))
        self.write_bytes(address, result)