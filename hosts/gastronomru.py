import requests
from bs4 import BeautifulSoup
from dto import recipe_dto


class GastronomRu:
    def __init__(self, src):
        self.main_url = "https://www.gastronom.ru/"
        self.src = src
        self.html_document = self.get_html_file()

    def get_html_file(self):
        html = requests.get(self.src, allow_redirects=False)
        html.encoding = 'utf-8'
        return BeautifulSoup(html.text, features="html.parser")

    def get_recipe_dto(self):
        # Build recipe object
        recipe_obj = recipe_dto.RecipeDto(self.get_title(),
                                          self.get_calories_amount(),
                                          self.get_serving_count(),
                                          self.convert_time(
                                              self.get_cooking_time()
                                          ),
                                          self.get_note(),
                                          self.src,
                                          self.get_image_src(),
                                          self.get_ingredients(),
                                          self.get_steps())
        return recipe_obj

    def get_note(self):
        note = self.html_document.find("div", {"class": "recipe__intro"})
        if note is None:
            note = self.html_document.find("div", {"class": "post-author"})
            if note is None:
                return None
            return ' '.join(note.find_all("p")[1].contents[0].split())
        return note.find("p").contents[0]

    def get_steps(self):
        steps = self.html_document.find_all("div", {"class": "recipe__step-text"})
        if not steps:
            steps = self.html_document.find_all("div", {"class": "recipe__step"})
            instruction = []
            for step in steps:
                instruction.append(' '.join(step.find_all("div")[1].contents[0].split()))
        else:
            instruction = []
            for step in steps:
                instruction.append(' '.join(step.contents[0].split()))
        return instruction

    def get_title(self):
        title = self.html_document.find("h1", {"class": "recipe__title"}).contents[0]
        title = ' '.join(title.split())
        return title

    def get_image_src(self):
        img_src = self.html_document.find("div", {"class": "main-slider__image-wrap"}).find("img").get("src")
        if self.main_url not in img_src:
            img_src = self.main_url + img_src
        return img_src

    def get_calories_amount(self):
        calories_amount = self.html_document.find("div", {"itemprop": "calories"})
        if calories_amount is None:
            return None
        return calories_amount.contents[0].split()[0]

    def get_serving_count(self):
        default_serving_count = self.html_document.find("div", {"itemprop": "recipeYield"})
        if default_serving_count is None:
            return None
        else:
            return default_serving_count.contents[0].split()[0][0]

    def get_ingredients(self):
        ingredients = []
        ing = self.html_document.find_all("li", {"itemprop": "recipeIngredient"});
        if not ing:
            ing = self.html_document.find_all("div", {"class": "recipe__Ingredients"})
        for ingredient in ing:
            if ingredient.find("a") is None:
                item = ingredient.contents[0]
            else:
                item = ingredient.find("a").contents[0]
            ingredients.append(item)
        return ingredients

    def get_cooking_time(self):
        cooking_time = self.html_document.find("div", {"itemprop": "totalTime"})
        if cooking_time is None:
            return None
        return cooking_time.contents[0].split()

    @staticmethod
    def convert_time(time):
        if time is None:
            return None
        if len(time) > 2:
            result = int(time[0]) * 60 + int(time[2])
        else:
            if 'мин' in time[1]:
                result = int(time[0])
            else:
                result = int(time[0]) * 60
        return result
