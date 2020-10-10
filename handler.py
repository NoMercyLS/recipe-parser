from hosts import edaru
import validators


class CommandHandler:
    def __init__(self):
        self.host = "vk.com"
        self.allowed_resources = [
            "https://eda.ru"
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

    def get_dto(self):
        if self.is_allowed():
            eda = edaru.EdaRu(self.host)
            return eda.get_recipe_dto().to_string()
        else:
            if self.host == "!exit":
                exit(0)
            else:
                return "Incorrect source link, try again\nTo finish, write !exit"
