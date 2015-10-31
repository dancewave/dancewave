#!/usr/bin/python
import os
from neverwise import Util

li = Util.createListItem(Util._addonName, thumbnailImage = '{0}/icon.png'.format(os.path.dirname(os.path.abspath(__file__))), streamtype = 'music', infolabels = { 'title' : Util._addonName })
xbmc.Player(xbmc.PLAYER_CORE_PAPLAYER).play('http://dancewave.hopto.org/dance.mp3', li)
