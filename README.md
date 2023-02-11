# recipe-app-api
Basic Django-Rest-Framework CRUD project
  - Nginx is used as a reverse proxy and as a Load balancer.
  - Dockerized project.
  - Provides Login/Registration and Refresh Token endpoints with JWT Token Authentication.
  - Provides CRUD Api to create Recipes.
  - Sends a verfication email on registration using celery task.
  - Delete api is implemented to delete user or recipe or tags or ingredients.
  - Delete feature is implemented such that a soft delete happens and later the data is removed from database using celery-beat cron job.
