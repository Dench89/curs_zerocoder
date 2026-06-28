Запуск Python
Команда	Назначение
python	Запустить интерактивный Python.
python --version	Показать установленную версию Python.
python main.py	Запустить файл Python.
py	Запустить Python через Python Launcher (Windows).
py -3	Запустить последнюю установленную версию Python 3.

Виртуальное окружение (venv)
Команда	Назначение
python -m venv .venv	Создать виртуальное окружение.
.venv\Scripts\Activate.ps1	Активировать venv (PowerShell).
.venv\Scripts\activate.bat	Активировать venv (CMD).
deactivate	Деактивировать виртуальное окружение.

pip
Команда	Назначение
pip --version	Показать версию pip.
pip list	Показать установленные пакеты.
pip install ИМЯ_ПАКЕТА	Установить пакет.
pip uninstall ИМЯ_ПАКЕТА	Удалить пакет.
pip install --upgrade ИМЯ_ПАКЕТА	Обновить пакет.
pip install --upgrade pip	Обновить pip.
pip freeze	Показать список пакетов для requirements.txt.
pip freeze > requirements.txt	Создать requirements.txt.
pip install -r requirements.txt	Установить зависимости из requirements.txt.

Полезные модули
Команда	Назначение
python -m pip	Запустить pip через Python.
python -m venv	Запустить модуль создания venv.
python -m http.server	Запустить простой HTTP-сервер.
python -m json.tool	Проверить и красиво вывести JSON.

Проверка окружения
Команда	Назначение
where python	Показать путь к Python (Windows).
where pip	Показать путь к pip.
python -c "import sys; print(sys.executable)"	Показать используемый Python.
python -c "import sys; print(sys.version)"	Показать версию Python.
python -c "import os; print(os.getcwd())"	Показать текущую папку.

Работа с пакетами
Команда	Назначение
pip show ИМЯ_ПАКЕТА	Показать информацию о пакете.
pip cache dir	Показать папку кэша pip.
pip cache purge	Очистить кэш pip.

Часто используемые команды
Команда	Назначение
python main.py	Запустить программу.
python --version	Проверить версию Python.
python -m venv .venv	Создать виртуальное окружение.
.venv\Scripts\Activate.ps1	Активировать окружение.
pip install -r requirements.txt	Установить все зависимости проекта.
pip freeze > requirements.txt	Обновить список зависимостей.
deactivate	Выйти из виртуального окружения.