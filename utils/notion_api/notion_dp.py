import requests
import data
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_pages(num_pages=None):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    # import json
    # with open('db.json', 'w', encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{config.DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results


pages = get_pages()

for page in pages:
    created_time = page["properties"]['Время создания.']["created_time"]
    description = page["properties"]['Описание.']["rich_text"]
    blocking = page["properties"]["Блокировка."]
    update_date = page["properties"]["Дата обновления."]
    distribution = page["properties"]["Распределение."]
    blocked = page["properties"]["Заблокирован."]
    resources = page["properties"]["Ресурсы ."]
    status = page["properties"]["Статус."]
    preparation = page["properties"]["Подготовка."]
    achive = page["properties"]["Архив."]
    objectives = page["properties"]["Задачи."]
    id_page = page["properties"]["ID"]

    print(created_time, description, blocking, update_date, distribution, blocked, resources, status, preparation, achive, objectives, id_page)

