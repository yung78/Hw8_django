from datetime import date
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


# @pytest.mark.django_db  # Генерируем и проверяем курс по URL и id
# def test_get_course(client, student_factory, course_factory):
#     course = course_factory(_quantity=1)
#     response = client.get('/api/v1/courses/1/')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data['id'] == 1
#
#
# @pytest.mark.django_db  # Генерируем и проверяем список курсов
# def test_get_courses(client, student_factory, course_factory):
#     course = course_factory(_quantity=10)
#     response = client.get('/api/v1/courses/')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == len(course)
#     for i, c in enumerate(data):
#         assert c['id'] == course[i].id
#
#
# @pytest.mark.django_db  # Проверка фильтрации списка курсов по id
# def test_get_filter_id(client, student_factory, course_factory):
#     course = course_factory(_quantity=15)
#     response = client.get('/api/v1/courses/?id=5&id=10')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 2
#     check_id = []
#     for c in data:
#         check_id.append(c['id'])
#     assert check_id[0] == 5
#     assert check_id[1] == 10
#
#
# @pytest.mark.django_db   # Проверка фильтрации списка курсов по name
# def test_get_filter_name(client, student_factory, course_factory):
#     course = course_factory(_quantity=10)
#     c_name = course[1].name
#     response = client.get('/api/v1/courses/', {'name': c_name})
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data[0]['name'] == c_name
#
#
# @pytest.mark.django_db   # Проверка успешного создания курса
# def test_post_course(client):
#     c_name = 'python'
#     response = client.post('/api/v1/courses/', {'name': c_name})
#
#     assert response.status_code == 201
#     response = client.get('/api/v1/courses/')
#     data = response.json()
#     assert data[0]['name'] == c_name
#
#
# @pytest.mark.django_db   # Проверка успешного изменения курса
# def test_get_filter_name(client, student_factory, course_factory):
#     course = course_factory(_quantity=1)
#     c_name = 'python'
#     response = client.get('/api/v1/courses/')
#
#     assert response.status_code == 200  # проверяем создание
#     data = response.json()
#     assert data[0]['name'] == course[0].name
#
#     response2 = client.patch('/api/v1/courses/1/', {'name': c_name})
#
#     assert response2.status_code == 200
#
#     response3 = client.get('/api/v1/courses/')
#     data = response3.json()
#
#     assert data[0]['name'] == c_name  # проверяем изменение
#
#
# @pytest.mark.django_db  # Проверка удаления
# def test_del_course(client, student_factory, course_factory):
#     course = course_factory(_quantity=10)
#     response = client.get('/api/v1/courses/')
#
#     assert response.status_code == 200  # проверяем создание, количество и первый элемент
#     data = response.json()
#     assert data[0]['id'] == 1
#     assert len(data) == 10
#
#     response2 = client.delete('/api/v1/courses/1/')
#
#     assert response2.status_code == 204
#
#     response = client.get('/api/v1/courses/')
#     data = response.json()
#
#     assert len(data) == 9  # проверяем корректное удаление
#     assert data[0]['id'] == 2
