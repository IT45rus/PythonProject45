from collections import defaultdict

def calculate_average_rating(data):
    """
    Считает средний рейтинг для каждого бренда
    """
    brand_ratings = defaultdict(list)
    
    for product in data:
        brand = product['brand']
        rating = product['rating']
        brand_ratings[brand].append(rating)
    
    # Считаем среднее для каждого бренда
    result = []
    for brand, ratings in brand_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        result.append({
            'brand': brand,
            'rating': round(avg_rating, 2)
        })
    
    # Сортируем по рейтингу (от высокого к низкому)
    result.sort(key=lambda x: x['rating'], reverse=True)
    return result
