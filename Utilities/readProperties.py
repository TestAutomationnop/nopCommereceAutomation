import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("Login data",'baseUrl')
        return url


    @staticmethod
    def getUsername():
        usernaame = config.get("Login data",'Username')
        return usernaame

    @staticmethod
    def getPassword():
        password = config.get("Login data", 'password')
        return password