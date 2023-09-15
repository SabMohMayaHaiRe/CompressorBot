#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("23572120", cast=int)
    API_HASH = config("87e5640ca80bcad76ed7228d69dbbd7c")
    BOT_TOKEN = config("6516995458:AAHpAvgTIg-mXSlVMhei-wtRbTwS0YcD2Jw")
    OWNER = config("OWNER_ID", default=6341127778, cast=int)
    LOG = config("LOG_CHANNEL", "-1001772303732" cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
