# main.py
import json

def load_favorites(filename="favorites.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return {
            "color": "red",
            "food": "steak",
            "movie": "Top Gun"
        }

def save_favorites(favorites, filename="favorites.json"):
    with open(filename, "w") as f:
        json.dump(favorites, f)

def display_favorites(favorites):
    print("Available categories:", ", ".join(favorites.keys()))

def lookup_favorite(favorites):
    category = input("Type a category to see my favorite: ")
    if category in favorites:
        print("My favorite", category, "is", favorites[category])
    else:
        print("Sorry, that category is not available.")

def add_favorite(favorites):
    new_cat = input("Enter name of new category: ")
    new_val = input("Enter your favorite for that category: ")
    favorites[new_cat] = new_val

def update_favorite(favorites):
    new_cat = input("Enter name of category: ")
    if new_cat not in favorites:
        print("Category not found.")
        return
    new_val = input("Enter your favorite for that category: ")
    favorites[new_cat] = new_val

def delete_favorite(favorites):
    cat = input("Enter name of old/new category: ")
    if cat in favorites:
        del favorites[cat]
    else:
        print("Category not found.")

def main():
    favorites = load_favorites()

    while True:
        display_favorites(favorites)
        lookup_favorite(favorites)

        add_new = input("Do you want to (update)/(add) a new favorite and value?: ")
        if add_new.lower() == "update":
            update_favorite(favorites)
        elif add_new.lower() == "add":
            add_favorite(favorites)

        del_opt = input("Do you want to delete a catergory? (yes/no): ")
        if del_opt.lower() == "delete":
            delete_favorite(favorites)

        q = input("Quit? (yes/no): ")
        if q.lower() == "yes":
            save_favorites(favorites)
            break

        print("Updated favorites:", favorites)

if __name__ == "__main__":
    main()
