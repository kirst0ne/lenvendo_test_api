from pprint import pprint
from fixture.JsTestTask import JsTestTask


def test_js_test_task(api_client):
    response_data = api_client(search="Alcatel", sort_field="name")
    print("Response Data:")
    pprint(response_data)
    assert 'products' in response_data
    products = response_data['products']
    assert isinstance(products, list)
    tasks = [JsTestTask(item['name'], item['image'], item['price']) for item in products]
    for task in tasks:
        assert "Alcatel" in task.name, f"Имя '{task.name}' не содержит 'Alcatel'"
    sorted_names = sorted(task.name for task in tasks)
    assert [task.name for task in tasks] == sorted_names, "Элементы не отсортированы по имени"
