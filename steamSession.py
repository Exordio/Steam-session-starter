from steam import webauth


class SteamSession(object):
    def __init__(self, login, password):
        self.steamLogin = login
        self.steamPassword = password
        self.session = self.__getSteamSession()

    def __getSteamSession(self):
        steamInit = webauth.WebAuth(self.steamLogin)
        return steamInit.cli_login(self.steamPassword)


if __name__ == '__main__':
    login = ''
    password = ''
    s = SteamSession(login, password)
    print(s.session)
