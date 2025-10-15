import pytest
from report_generator import calculate_average_rating

def test_average_rating():
    # Тестовые данные
    test_data = [
        {'name': 'iphone', 'brand': 'apple', 'price': 999, 'rating': 5.0},
        {'name': 'ipad', 'brand': 'apple', 'price': 799, 'rating': 4.0},
    ]
    
    result = calculate_average_rating(test_data)
    
    assert len(result) == 1
    assert result[0]['brand'] == 'apple'
    assert result[0]['rating'] == 4.5  # (5.0 + 4.0) / 2 = 4.5
