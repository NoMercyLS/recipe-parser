class RecipeDto:
    def __init__(self, title="Unknown recipe",
                 src="Unknown url",
                 categories=None,
                 img_url="Unknown url",
                 calories_amount=0,
                 ingredients=None,
                 servings_count=0,
                 cooking_time=0,
                 steps=[]
                 ):
        self.title = title
        self.src = src
        self.categories = categories
        self.img_url = img_url
        self.calories_amount = calories_amount
        self.ingredients = ingredients
        self.servings_count = servings_count
        self.cooking_time = cooking_time
        self.steps = steps

    def to_string(self):
        category = []
        ingredient = []
        step = []
        output = ""
        output += "Name: " + str(self.title) + '\n'
        output += "Source: " + str(self.src) + '\n'
        output += "Categories: "
        for category in self.categories:
            if category != self.categories[len(self.categories) - 1]:
                output += str(category) + ', '
        output += str(category) + '\n'
        output += "Image: " + str(self.img_url) + '\n'
        output += "Calories: " + str(self.calories_amount) + '\n'
        output += "Ingredients: \n"
        for ingredient in self.ingredients:
            if ingredient != self.ingredients[len(self.ingredients) - 1]:
                output += str(ingredient[0]) + ' - ' + str(ingredient[1]) + ',\n'
        output += str(ingredient[0]) + ' - ' + str(ingredient[1]) + '\n'
        output += "Servings count: " + str(self.servings_count) + '\n'
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
            "name": self.title,
            "src": self.src,
            "categories": self.categories,
            "img_url": self.img_url,
            "calories": self.calories_amount,
            "ingredients": self.ingredients,
            "servings_count": self.servings_count,
            "cooking_time": self.cooking_time,
            "steps": self.steps
        }
