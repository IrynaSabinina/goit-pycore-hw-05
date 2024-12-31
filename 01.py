def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}
    
    # Визначаємо fibonacci
    def fibonacci(n):
        # Якщо значення n вже є, повертаємо
        if n in cache:
            return cache[n]
        
        # якщо n <= 0, то це 0; якщо n == 1, то це 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Обчислюємо число Фібоначчі рекурсивно
        result = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Зберігаємо результат у кеші
        cache[n] = result
        
        return result
    
    # Повертаємо функцію fibonacci, яка може використовувати кеш
    return fibonacci


# Створюємо функцію fibonacci
fibonacci = caching_fibonacci()
print(fibonacci(15)) 

# for i in range(20):
#     print(f"F({i}) = {fibonacci(i)}")

