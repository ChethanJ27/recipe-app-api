# recipe-app-api
Basic Django-Rest-Framework CRUD project
  - Designed and implemented a scalable RESTful API project using Django Rest Framework, with Docker containerization for improved portability and flexibility.
  - Incorporated JWT Authentication using simple jwt framework.
  - Nginx is used as a reverse proxy and as a Load balancer.
  - Provides Login/Registration and Refresh Token endpoints with JWT Token Authentication.
  - Provides CRUD Api to create Recipes.
  - Sends a verfication email on registration using celery task.
  - Delete api is implemented to delete user or recipe or tags or ingredients.
  - Delete feature is implemented such that a soft delete happens and later the data is removed from database using celery-beat cron job.
