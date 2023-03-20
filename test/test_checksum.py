#!/usr/bin/env python3

import sys, os
import unittest

sys.path.append(os.pardir)
import src.checksum as test_module

class Test_checksum(unittest.TestCase):

    def test_checksum8(self) -> None:

        result = test_module.checksum8(0x00, b'')
        self.assertEqual(result, int(0x00 & 0xFF))

        result = test_module.checksum8(0xFF, b'')
        self.assertEqual(result, int(0xFF & 0xFF))

        result = test_module.checksum8(0xFF, b'0123')
        self.assertEqual(result, int((0xFF + 0x30 + 0x31 + 0x32 + 0x33) & 0xFF))

        result = test_module.checksum8(0xFF, b'01234')
        self.assertEqual(result, int((0xFF + 0x30 + 0x31 + 0x32 + 0x33 + 0x34) & 0xFF))

    def test_checksum16(self) -> None:

        result = test_module.checksum16(0x0000, b'', byteorder='big')
        self.assertEqual(result, int(0x0000 & 0xFFFF))

        result = test_module.checksum16(0xFFFF, b'', byteorder='big')
        self.assertEqual(result, int(0xFFFF & 0xFFFF))

        result = test_module.checksum16(0xFFFF, b'0123', byteorder='big')
        self.assertEqual(result, int((0xFFFF + 0x3031 + 0x3233) & 0xFFFF))

        result = test_module.checksum16(0xFFFF, b'01234', byteorder='big')
        self.assertEqual(result, int((0xFFFF + 0x3031 + 0x3233) & 0xFFFF))

        result = test_module.checksum16(0xFFFF, b'01234', byteorder='little')
        self.assertEqual(result, int((0xFFFF + 0x3130 + 0x3332) & 0xFFFF))

        with self.assertRaises(ValueError):
            result = test_module.checksum16(0xFFFF, b'01234', byteorder='hoge')

    def test_checksum32(self) -> None:

        result = test_module.checksum32(0x00000000, b'', byteorder='big')
        self.assertEqual(result, int(0x00000000 & 0xFFFFFFFF))

        result = test_module.checksum32(0xFFFFFFFF, b'', byteorder='big')
        self.assertEqual(result, int(0xFFFFFFFF & 0xFFFFFFFF))

        result = test_module.checksum32(0xFFFFFFFF, b'01234567', byteorder='big')
        self.assertEqual(result, int(0xFFFFFFFF + 0x30313233 + 0x34353637) & 0xFFFFFFFF)

        result = test_module.checksum32(0xFFFFFFFF, b'012345678', byteorder='big')
        self.assertEqual(result, int(0xFFFFFFFF + 0x30313233 + 0x34353637) & 0xFFFFFFFF)

        result = test_module.checksum32(0xFFFFFFFF, b'012345678', byteorder='little')
        self.assertEqual(result, int(0xFFFFFFFF + 0x33323130 + 0x37363534) & 0xFFFFFFFF)

        with self.assertRaises(ValueError):
            result = test_module.checksum32(0xFFFFFFFF, b'012345678', byteorder='hoge')

if __name__ == '__main__':
    unittest.main(verbosity=2)
