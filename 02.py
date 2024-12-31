import re
from typing import Callable

# Генератор для знаходження всіх дійсних чисел у тексті
def generator_numbers(text: str):
    # patern для пошуку дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    
    # Знаходимо всі відповідаючі патерну числа
    for match in re.finditer(pattern, text):
    
        yield float(match.group())

# підсумовування всіх чисел, які повертаються генератором
def sum_profit(text: str, func: Callable):
    # Використовуємо генератор для обчислення суми
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
