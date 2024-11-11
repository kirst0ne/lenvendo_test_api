import pytest
import requests


@pytest.fixture
def api_client():
    base_url = "https://www.lenvendo.ru/api/js-test-task/"

    def get_js_test_task(search=None, sort_field=None, page=None):
        params = {}
        if search:
            params['search'] = search
        if sort_field:
            params['sort_field'] = sort_field
        if page:
            params['page'] = page
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()

    return get_js_test_task
