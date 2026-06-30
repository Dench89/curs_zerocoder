# KODA CLI — Справочник

## Проверка Node.js
```powershell
node -v
```
Проверить установленную версию Node.js.

```powershell
npm -v
```
Проверить установленную версию npm.

## Установка Koda CLI
```powershell
npm install -g @kodadev/koda-cli@latest
```
Установить или обновить Koda CLI глобально.

## Проверка версии
```powershell
koda --version
```
Показать установленную версию Koda.

## Запуск Koda
```powershell
koda
```
Запустить Koda CLI.

```powershell
koda --help
```
Показать список всех доступных команд.

```powershell
koda --debug
```
Запустить Koda в режиме отладки с подробным выводом.

```powershell
npx @kodadev/koda-cli@latest
```
Запустить Koda без предварительной установки.

### Решение ошибок авторизации
Если появляется ошибка:
```
401 Authorization header required
```
или сообщение:
```
Authenticated via "skip"
```
Выполните:
```text
/auth
```
и войдите через **Koda Auth**.

## Горячие клавиши

| Клавиши | Действие |
|---------|----------|
| `Ctrl + C` | Закрыть Koda |
| `Enter` | Подтвердить выбор |
