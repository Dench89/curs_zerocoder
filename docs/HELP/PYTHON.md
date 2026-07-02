# Python — шпаргалка

## Виртуальное окружение

```powershell
python -m venv .venv
```
Создать виртуальное окружение.

```powershell
.\.venv\Scripts\Activate.ps1
```
Активировать виртуальное окружение.

После активации приглашение должно выглядеть так:

```text
(.venv) PS F:\Projects\МойПроект>
```

---

## Проверка Python

```powershell
python --version
```
Показать установленную версию Python.

```powershell
where python
```
Показать путь к используемому Python.

---

## Работа с библиотеками

```powershell
pip list
```
Показать все установленные библиотеки.

```powershell
pip show ИМЯ_ПАКЕТА
```
Показать информацию о библиотеке.

```powershell
pip install ИМЯ_ПАКЕТА
```
Установить библиотеку.

```powershell
pip install -r requirements.txt
```
Установить все библиотеки из файла `requirements.txt`.

```powershell
pip install --upgrade -r requirements.txt
```
Обновить библиотеки из `requirements.txt`.

```powershell
pip list --outdated
```
Показать библиотеки, для которых доступны обновления.

---

## Сохранение зависимостей

```powershell
pip freeze > requirements.txt
```
Сохранить список установленных библиотек в `requirements.txt`.

> Используйте **только после** установки или обновления библиотек.

---

## Пересоздание виртуального окружения

Если возникают ошибки с зависимостями:

1. Удалите папку `.venv`.
2. Создайте новое окружение:

```powershell
python -m venv .venv
```

3. Активируйте окружение:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Установите зависимости:

```powershell
pip install -r requirements.txt
```

---

## Типичный порядок работы

### Новый проект

```powershell
python -m venv .venv
```

↓

```powershell
.\.venv\Scripts\Activate.ps1
```

↓

```powershell
pip install ИМЯ_ПАКЕТА
```

↓

```powershell
pip freeze > requirements.txt
```

---

### Скачали готовый проект

```powershell
.\.venv\Scripts\Activate.ps1
```

↓

```powershell
pip install -r requirements.txt
```

---

### Добавили новую библиотеку

```powershell
pip install ИМЯ_ПАКЕТА
```

↓

```powershell
pip freeze > requirements.txt
```