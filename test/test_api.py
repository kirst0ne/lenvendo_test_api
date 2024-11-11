from pprint import pprint
from fixture.JsTestTask import JsTestTask


def test_js_test_task(api_client):
    search_term = "Alcatel"
    sort_field_term = "name"
    current_page = 1
    while True:
        response_data = api_client(search=search_term, sort_field=sort_field_term, page=current_page)
        print(f"Response Data for page {current_page}:")
        pprint(response_data)
        assert 'products' in response_data, "Ответ API содержит ключ 'products'"
        products = response_data['products']
        assert isinstance(products, list), "Ответ API содержит список продуктов"
        tasks = [JsTestTask(item['name'], item['image'], item['price']) for item in products]
        for task in tasks:
            assert "Alcatel" in task.name, f"Имя '{task.name}' не содержит 'Alcatel'"
        sorted_names = sorted(task.name for task in tasks)
        assert [task.name for task in tasks] == sorted_names, "Элементы не отсортированы по имени"
        if 'next_page_url' in response_data and response_data['next_page_url']:
            current_page += 1
        else:
            break
