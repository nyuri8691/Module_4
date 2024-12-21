
def test_function():
    def inner_function():

        print("Я в области видимости функции test_function")

    inner_function() #здесь ничего не возвращает


# inner_function()  # не работает! "ошибка"

test_function()  # f здесь - работает
