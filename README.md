# hw4



# 1 Страница администратора
Cтраница администратора доступна по адресу http://127.0.0.1:8000/admin/ .  
Логин/пароль - admin/admin  


# 2 Страница приложения
GET /api/tasks - получть список всех задач   
GET /api/tasks/{id} - получть одну конкретную задачу  
POST /api/tasks - создать задачу  
PUT (или PATCH) /api/tasks/{id} - отредактировать существующую задачу  
DELETE /api/tasks/{id} - удалить одну задачу  
запрос GET может быть дополнен query-параметром ?title=  
запрос GET может быть дополнен query-параметром ?is_active=  
запрос GET может быть дополнен query-параметром ?ordering=  
