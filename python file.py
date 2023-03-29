recipes = []

# Function to add a new recipe
def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    instructions = input("Enter instructions: ")
    category = input("Enter category: ")
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions,
        "category": category
    }
    recipes.append(recipe)
    print("Recipe added successfully!")

# Function to view all recipes
def view_recipes():
    if not recipes:
        print("No recipes found.")
    else:
        for i, recipe in enumerate(recipes):
            print(f"{i+1}. {recipe['name']} ({recipe['category']})")

# Function to view a recipe by name
def view_recipe():
    name = input("Enter recipe name: ")
    for recipe in recipes:
        if recipe['name'] == name:
            print(f"{recipe['name']} ({recipe['category']}):")
            print("Ingredients:")
            for ingredient in recipe['ingredients']:
                print(f"- {ingredient}")
            print("Instructions:")
            print(recipe['instructions'])
            return
    print("Recipe not found.")

# Function to delete a recipe by name
def delete_recipe():
    name = input("Enter recipe name: ")
    for recipe in recipes:
        if recipe['name'] == name:
            recipes.remove(recipe)
            print("Recipe deleted successfully!")
            return
    print("Recipe not found.")

# Main menu loop
while True:
    print("\n1. Add recipe")
    print("2. View all recipes")
    print("3. View recipe by name")
    print("4. Delete recipe by name")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_recipe()
    elif choice == '2':
        view_recipes()
    elif choice == '3':
        view_recipe()
    elif choice == '4':
        delete_recipe()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
