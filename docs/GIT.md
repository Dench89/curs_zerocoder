# Git — шпаргалка

## Основные команды

git status — Проверить состояние проекта.

git add . — Добавить все изменения в индекс.

git add ИМЯ_ФАЙЛА — Добавить только указанный файл.

git commit -m "Описание изменений" — Создать новый коммит.

git push — Отправить коммиты на GitHub.

git pull — Получить изменения с GitHub.

git fetch — Проверить наличие новых изменений без слияния.

---

## История

git log — Показать полную историю коммитов.

git log --oneline — Краткая история коммитов.

git log --oneline --graph --decorate --all — История в виде дерева.

git show ХЕШ — Показать содержимое выбранного коммита.

---

## Ветки

git branch — Показать список веток.

git branch ИМЯ — Создать новую ветку.

git switch ИМЯ — Переключиться на ветку.

git switch -c ИМЯ — Создать ветку и сразу перейти в неё.

git branch -d ИМЯ — Удалить ветку.

---

## Восстановление

git restore ФАЙЛ — Отменить изменения файла.

git restore --staged ФАЙЛ — Убрать файл из индекса (отменить git add).

git restore --staged . — Убрать все файлы из индекса.

git restore --source=ХЕШ ФАЙЛ — Вернуть файл из указанного коммита.

git checkout ХЕШ — Открыть проект в состоянии выбранного коммита.

git switch main — Вернуться к последней версии проекта.

git revert ХЕШ — Безопасно отменить коммит, создав новый.

git reset --hard ХЕШ — Полностью вернуть проект к выбранному коммиту.

---

## GitHub

git remote -v — Показать подключённые удалённые репозитории.

git clone URL — Скачать репозиторий с GitHub.

---

## Сравнение

git diff — Показать изменения до git add.

git diff --staged — Показать изменения после git add.

git diff ХЕШ1 ХЕШ2 — Сравнить два коммита.

---

## Настройки

git remote -v — Проверить адрес GitHub-репозитория.

git config --global user.name — Показать имя пользователя Git.

git config --global user.email — Показать email пользователя Git.

git --version — Показать установленную версию Git.

git config --global core.quotepath false — Показывать русские имена файлов без кодировки.

git config --global core.autocrlf true — Автоматически преобразовывать окончания строк (Windows).

git config --global init.defaultBranch main — Сделать ветку main веткой по умолчанию.

---

## Полезные команды

git status -s — Короткий вывод состояния файлов.

---

## Обозначения Git

HEAD -> main — Текущий коммит, на котором вы находитесь.

origin/main — Последний коммит на GitHub.

HEAD == origin/main — Локальный репозиторий полностью синхронизирован с GitHub.

HEAD впереди origin/main — Есть локальные коммиты, выполните git push.

origin/main впереди HEAD — На GitHub есть новые изменения, выполните git pull.

---

## Полезные сообщения Git

Everything up-to-date — Новых коммитов для отправки нет.

LF will be replaced by CRLF — Не ошибка. Git автоматически преобразует окончания строк для Windows.

---

## Обычный порядок работы

git status

git add .

git commit -m "Описание изменений"

git push