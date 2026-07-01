import pytest


@pytest.fixture
def base_url():
    return 'http://127.0.0.1:5000'

@pytest.fixture
def is_check():
    print('Код до теста') # 1
    yield 'Тестовая функция'
    print('Код после теста')



