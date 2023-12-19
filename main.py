from store import get_categories

def run():
    categories = get_categories('https://api.escuelajs.co/api/v1/categories')
    
    for category in categories:
        print(category['name'])

if __name__ == '__main__':
    run()