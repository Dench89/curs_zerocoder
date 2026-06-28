import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(f"Статус-код: {response.status_code}")

data = response.json()

print(f"ID: {data['id']}")
print(f"Заголовок: {data['title']}")
print(f"Первые 100 символов текста:")
print(data['body'][:100])