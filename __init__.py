print(" ██╗   ██╗██████╗  ██████╗")
print(" ██║   ██║██╔══██╗██╔════╝")
print(" ██║   ██║██████╔╝██║     ")
print(" ██║   ██║██╔══██╗██║     ")
print(" ╚██████╔╝██████╔╝╚██████╗")
print("  ╚═════╝ ╚═════╝  ╚═════╝")

from CanvasAPI import callapi
from CanvasAPI.util import file, zipfile, getpass, printer
import sys, os, ntpath
import configparser
from os.path import isabs
import logging


logging.basicConfig(filename='canvasapi.log',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())

parser = configparser.ConfigParser()
parser.read("{}/config-canvas.def".format(os.path.dirname(__file__)))

_CONNECT_AUTOMATICALLY = parser['Base']['ConnectAutomatically']
_DEFAULT_INSTANCE = int(parser['Base']['DefaultInstance'])
_DEFAULT_TOKEN_LOCATION = parser['Base']['TokenLocation']
if not isabs(_DEFAULT_TOKEN_LOCATION) or not _DEFAULT_TOKEN_LOCATION:
    _DEFAULT_TOKEN_LOCATION = os.getcwd() + "/" + _DEFAULT_TOKEN_LOCATION

_DEFAULT_TOKEN_FILENAMES = []
_DEFAULT_SERVERS = []
_ENVIRONMENTS = []
_CONNECTED = False

for section in parser.sections():
    if section != "Base":
        _ENVIRONMENTS.append(str(section))
        _DEFAULT_TOKEN_FILENAMES.append(parser[section]['TokenFile'])
        _DEFAULT_SERVERS.append(parser[section]['Server'])

if len(_ENVIRONMENTS) <= 0:
    print("No environments found")
    input("Press enter to close...")
    sys.exit(1)
    

if _CONNECT_AUTOMATICALLY:
    if _DEFAULT_INSTANCE <= len(_ENVIRONMENTS) and _DEFAULT_INSTANCE >= 1:
        _INSTANCE = _DEFAULT_INSTANCE
    else:
        printer.print_list(_ENVIRONMENTS, numbered=True)
        try:
            i = int(input("Select instance: "))
            if i <= len(_ENVIRONMENTS) and i >= 1:
                _INSTANCE = i
            else:
                print("Bad input")
                input("Press enter to close...")
                sys.exit(1)
        except ValueError as e:
            print("Bad input")
            input("Press enter to close...")
            sys.exit(1)
    _SERVER = _DEFAULT_SERVERS[_INSTANCE-1]   
    if zipfile.is_zipfile(_DEFAULT_TOKEN_LOCATION):
        zf = zipfile.ZipFile(_DEFAULT_TOKEN_LOCATION)
        for zinfo in zf.infolist():
            is_encrypted = zinfo.flag_bits & 0x1
        if is_encrypted:
            print("{} is password protected".format(_DEFAULT_TOKEN_LOCATION))
            tries = 0
            while True:
                try:
                    _TOKEN = zf.read(_DEFAULT_TOKEN_FILENAMES[_INSTANCE-1], pwd=bytes(getpass.getpass(),'utf-8')).decode()
                    break
                except RuntimeError as e:
                    tries += 1
                    print(e)
                    if tries >= 3:
                        _TOKEN = ""
                        break
                    continue
                
        else:
            _TOKEN = zf.read(_DEFAULT_TOKEN_FILENAMES[_INSTANCE-1]).decode().strip()
    else:
        try:
            f = open("{}/{}".format(_DEFAULT_TOKEN_LOCATION, _DEFAULT_TOKEN_FILENAMES[_INSTANCE-1]))
            _TOKEN = f.readline().strip()
            f.close()
        except FileNotFoundError as e:            
            print(e)
            _TOKEN = input("Input token: ")
    instance = callapi.Instance(_SERVER, _TOKEN.rstrip())
    _CONNECTED = True
else:
    instance = callapi.Instance()
    
from CanvasAPI import accounts
from CanvasAPI import admins
from CanvasAPI import analytics
from CanvasAPI import assignments
from CanvasAPI import courses
from CanvasAPI import custom_gradebook_columns
from CanvasAPI import enrollment_terms
from CanvasAPI import enrollments
from CanvasAPI import external_tools
from CanvasAPI import favorites
from CanvasAPI import feature_flags
from CanvasAPI import files
from CanvasAPI import groups
from CanvasAPI import grade_change_log
from CanvasAPI import navigation
from CanvasAPI import roles
from CanvasAPI import sections
from CanvasAPI import users
from CanvasAPI import quizzes

__all__ = ['instance',
           'accounts',
           'admins',
           'analytics',
           'assignments',
           'courses',
           'custom_gradebook_columns',
           'enrollment_terms',
           'enrollments',
           'external_tools',
           'favorites',
           'feature_flags',
           'files',
           'grade_change_log',
           'groups',
           'navigation',
           'quizzes',
           'roles',
           'sections',
           'users']

if _CONNECTED:
    _SELF = users.self()
    if _SELF is None:
        logging.error("Invalid token. Failed to connect to '{}'".format(_SERVER))
