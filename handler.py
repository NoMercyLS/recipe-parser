from hosts import edaru, gastronomru, artlunchru
import validators


class CommandHandler:
    def __init__(self):
        self.host = "vk.com"
        self.allowed_resources = [
            "https://eda.ru",
            "https://www.gastronom.ru",
            "https://art-lunch.ru"
        ]
        self.is_default = True

    def set_new_host(self, new_host_url):
        if self.is_default:
            self.is_default = False
        self.host = new_host_url

    def is_allowed(self):
        if validators.url(self.host):
            for resource in self.allowed_resources:
                if resource in self.host:
                    return True
        return False

    def get_resource(self):
        for resource in self.allowed_resources:
            if resource in self.host:
                return resource

    def get_dto(self):
        if self.is_allowed():
            if self.get_resource() == self.allowed_resources[0]:
                eda = edaru.EdaRu(self.host)
                return eda.get_recipe_dto().to_string()
            if self.get_resource() == self.allowed_resources[1]:
                gastronom = gastronomru.GastronomRu(self.host)
                return gastronom.get_recipe_dto().to_string()
            if self.get_resource() == self.allowed_resources[2]:
                artlunch = artlunchru.ArtLunchRu(self.host)
                return artlunch.get_recipe_dto().to_string()
            return "NOT FOUNDED"
        else:
            if self.host == "!exit":
                exit(0)
            else:
                return "Incorrect source link, try again\nTo finish, write !exit"
