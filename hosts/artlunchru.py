import requests
from bs4 import BeautifulSoup
from dto import recipe_dto


class ArtLunchRu:
    def __init__(self, src):
        self.main_url = "https://art-lunch.ru/"
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
        notes = self.html_document.find("div", {"class": "post-content recipe-content"}).find_all("p")
        out = ""
        for note in notes:
            if note.parent.get("class") is None:
                break
            out += note.text
        return out

    def get_steps(self):
        steps = self.html_document.find("div", {"id": "recipeInstructions"}).find_all("p")
        instruction = []
        for step in steps:
            instruction.append(step.text.replace('\n', ''))
        return instruction

    def get_title(self):
        title = self.html_document.find("h1").contents[0]
        title = ' '.join(title.split())
        return title

    def get_image_src(self):
        img_src = self.html_document.find("img", {"itemprop": "resultPhoto"}).get("src")
        return img_src

    def get_calories_amount(self):
        return self.html_document.find("span", {"itemprop": "calories"}).contents[0].split()[0]

    def get_serving_count(self):
        return self.html_document.find("span", {"itemprop": "recipeYield"}).contents[0].split()[0][0]

    def get_ingredients(self):
        ingredients = []
        ing = self.html_document.find_all("span", {"itemprop": "recipeIngredient"})
        for ingredient in ing:
            item = ingredient.contents[0].strip().replace('\t', '')
            item1 = ingredient.contents[1].text.strip().replace('\t', '') \
                .replace("веточки", "шт.") \
                .replace("1/2", "0,5") \
                .replace("1/4", "0,25") \
                .replace('зубчика', 'шт.') \
                .replace('зубчик', 'шт.').split('-')
            try:
                item1 = item1[1]
            except:
                item1 = item1[0]
            ingredients.append([item, item1])
        return ingredients

    def get_cooking_time(self):
        cooking_time = self.html_document.find("div", {"class": "small"}).find("span")
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
