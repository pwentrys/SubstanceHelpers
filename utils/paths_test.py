import os
from os.path import realpath, dirname
from pathlib import Path, PurePath

# TODO Expand
real = realpath(__file__)
raw = dirname(real)
path = Path(raw)
name = path.name
pure = PurePath(path)
pureName = pure.name
osAbsPath = os.path.abspath(real)
osBasename = os.path.basename(real)
osCommonPrefix = os.path.commonprefix(real)
osDirName = os.path.dirname(real)
osNormCase = os.path.normcase(real)
osNormPath = os.path.normpath(real)
osRealName, osRealExt = os.path.splitext(real)
os__file__Name, os__file__Ext = os.path.splitext(__file__)
logPath = Path(f'{osRealName}.log')

logPath.write_text(f'\n'
                   f'__file__: {__file__}\n'
                   f'real: {real}\n'
                   f'raw: {raw}\n'
                   f'path: {path}\n'
                   f'name: {name}\n'
                   f'pure: {pure}\n'
                   f'pureName: {pureName}\n'
                   f'osAbsPath: {osAbsPath}\n'
                   f'osCommonPrefix: {osCommonPrefix}\n'
                   f'osBasename: {osBasename}\n'
                   f'osDirName: {osDirName}\n'
                   f'osNormCase: {osNormCase}\n'
                   f'osNormPath: {osNormPath}\n'
                   f'osName: {osRealName}\n'
                   f'osExt: {osRealExt}\n'
                   f'os__file__Name: {os__file__Name}\n'
                   f'os__file__Ext: {os__file__Ext}\n'
                   f'logPath: {logPath}\n'
                   )
