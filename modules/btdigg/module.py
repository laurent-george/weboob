# -*- coding: utf-8 -*-

from weboob.capabilities.torrent import CapTorrent
from weboob.tools.backend import Module

from .browser import BTDiggBrowser


__all__ = ['BTDiggModule']


class BTDiggModule(Module, CapTorrent):
    NAME = 'btdigg'
    MAINTAINER = u'Matthieu Rakotojaona'
    EMAIL = 'matthieu.rakotojaona@gmail.com'
    VERSION = '1.0'
    DESCRIPTION = 'The BitTorrent DHT search engine.'
    LICENSE = 'CC0'
    BROWSER = BTDiggBrowser

    def create_default_browser(self):
        return self.create_browser()

    def get_torrent(self, id):
        return self.browser.get_torrent(id)

    def get_torrent_file(self, id):
        return self.browser.get_torrent_file(id)

    def iter_torrents(self, pattern):
        return self.browser.iter_torrents(pattern.replace(' ', '+'))

    #def fill_torrent(self, torrent, fields):
    #    if 'description' in fields or fields == None:
    #        return self.get_torrent(torrent.id)

    #OBJECTS = {
    #    Torrent:fill_torrent
    #}
