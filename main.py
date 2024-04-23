import sys
from lib.helpers import *
from lib.armor import *
import json


ArmorList = []


def SearchContainer():
    _container = RequestTarget()
    # _container = 0x42FC0327
    UseObject(_container)
    Wait(250)
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_container], True):
        _items = GetFindedList()
        for _item in _items:
            _a = Armor(_item)
            ArmorList.append(_a)
    _message = f'Container searched, {len(ArmorList)} items found.'
    print(_message)


def WriteToFile():
    ArmorFilePath = "armor.json"
    _file = open(ArmorFilePath, 'w')
    _file.write("[")
    _i = 0
    for _item in ArmorList:
        _file.write(json.dumps((_item.Encoder())))
        if _i != (len(ArmorList) - 1):
            _file.write(',')
            _file.write('\n')
        _i += 1
    _file.write("]")
    _message = f'Exported {len(ArmorList)} items.'
    _file.close()
    print(_message)


def main():
    SearchContainer()
    WriteToFile()


if __name__ == '__main__':
    main()
