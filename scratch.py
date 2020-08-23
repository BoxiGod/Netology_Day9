import requests


class SuperHeroes:

    super_heroes = []

    def __init__(self, hero):
        self.__class__.super_heroes.append(self)
        self.hero = hero

    def get_powerstat(self, powerstat):
        return self.hero['results'][0]['powerstats'][powerstat]

    @classmethod
    def get_highest_powerstat(cls, powerstat):
        highest_powerstat = 0
        for super_hero in cls.super_heroes:
            if int(super_hero.get_powerstat(powerstat)) > highest_powerstat:
                highest_powerstat = int(super_hero.get_powerstat(powerstat))
            else:
                continue
        return highest_powerstat


if __name__ == '__main__':
    access_token = "2619421814940190"
    super_heroes = {"Hulk": "", "Captain America": "", "Thanos": ""}
    for super_hero in super_heroes.keys():
        print(super_hero)
        super_heroes[super_hero] = SuperHeroes(requests.get("https://superheroapi.com/api/"
                                                            + access_token + "/search/" + super_hero).json())
    print(SuperHeroes.get_highest_powerstat("intelligence"))
