class RecipeDto:
    def __init__(self, title="Unknown recipe",
                 energy_value=0,
                 serving_count=0,
                 cooking_time=0,
                 note="",
                 source_link="Unknown url",
                 img_url="Unknown url",
                 ingredients=None,
                 steps=[]
                 ):
        self.title = title
        self.energy_value = energy_value
        self.serving_count = serving_count
        self.cooking_time = cooking_time
        self.note = note
        self.source_link = source_link
        self.img_url = img_url
        self.ingredients = ingredients
        self.steps = steps

    def to_string(self):
        ingredient = []
        output = ""
        output += "Name: " + str(self.title) + '\n'
        output += "Source: " + str(self.source_link) + '\n'
        output += "Image: " + str(self.img_url) + '\n'
        output += "Note: " + str(self.note) + '\n'
        output += "Calories: " + str(self.energy_value) + '\n'
        output += "Ingredients: \n"
        if self.source_link.__contains__("gastronom"):
            for ingredient in self.ingredients:
                if ingredient != self.ingredients[len(self.ingredients) - 1]:
                    output += str(ingredient) + ',\n'
            output += str(ingredient) + '\n'
        else:
            for ingredient in self.ingredients:
                if ingredient != self.ingredients[len(self.ingredients) - 1]:
                    output += str(ingredient[0]) + ' - ' + str(ingredient[1]) + ',\n'
            output += str(ingredient[0]) + ' - ' + str(ingredient[1]) + '\n'
        output += "Servings count: " + str(self.serving_count) + '\n'
        output += "Cooking time: " + str(self.cooking_time) + '\n'
        output += "Steps: " + '\n'
        for index in range(len(self.steps)):
            if index != len(self.steps) - 1:
                output += str(index+1) + ". " + str(self.steps[index]) + '\n'
            else:
                output += str(index+1) + ". " + str(self.steps[index]) + '\n'
        return output

    def to_dto(self):
        return {
            "title": self.title,
            "energyValue": self.energy_value,
            "servingsCount": self.serving_count,
            "cookingTime": self.cooking_time,
            "note": self.note,
            "src": self.source_link,
            "img_url": self.img_url,
            "ingredients": self.ingredients,
            "steps": self.steps
        }
