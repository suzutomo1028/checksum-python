#!/usr/bin/env python3

from typing import Literal

def checksum8(init_value: int, src: bytes) -> int:
    """ バイト列の8ビット幅チェックサムを算出する
    """
    sum = init_value
    for b in src:
        sum += b
    return int(sum & 0xFF)

def checksum16(init_value: int, src: bytes, byteorder: Literal['big', 'little']) -> int:
    """ バイト列の16ビット幅チェックサムを算出する
    """
    sum = init_value
    it = iter(src)
    for b0, b1 in zip(it, it):
        sum += int.from_bytes([b0, b1], byteorder=byteorder)
    return int(sum & 0xFFFF)

def checksum32(init_value: int, src: bytes, byteorder: Literal['big', 'little']) -> int:
    """ バイト列の32ビット幅チェックサムを算出する
    """
    sum = init_value
    it = iter(src)
    for b0, b1, b2, b3 in zip(it, it, it, it):
        sum += int.from_bytes([b0, b1, b2, b3], byteorder=byteorder)
    return int(sum & 0xFFFFFFFF)

if __name__ == '__main__':
    pass
