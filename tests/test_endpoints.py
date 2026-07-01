from database.engine import db
from database.models.todo import Task
from database.models.auth import User

# def test_endpoint_login(base_url):
# 	response = requests.get(f'{base_url}/auth/login')
# 	assert response.status_code == 200
# 	assert 'html' in response.headers['Content-Type']


# def test_endpoint_register(base_url, is_check):
# 	response = requests.get(f'{base_url}/auth/register')
# 	text = is_check
# 	text.lower()
# 	text.upper()
#
# 	assert response.status_code == 200



def test_create_task(db):
	task = Task(title='ффф', description='ыыы', user_id=5)
	db.session.add(task)
	assert task is not None



