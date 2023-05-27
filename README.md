# recipe-app-api
Basic Django-Rest-Framework CRUD project
  - Designed and implemented a scalable RESTful API project using Django Rest Framework, with Docker containerization for improved portability and flexibility.
  - Incorporated JWT Authentication using simple jwt framework. As a result, gained knowledge about how Token and Session based Authentication internally works.
  - Orchestrated proxy and load-balancing congurations with Nginx, leveraging its advanced capabilities to optimize trac routing and resource allocation.
  - Provides Login/Registration and Refresh Token endpoints with JWT Token Authentication.
  - Provides CRUD Api to create Recipes.
  - Sends a verfication email on registration using celery task.
  - Delete api is implemented to delete user or recipe or tags or ingredients.
  - Delete feature is implemented such that a soft delete happens and later the data is removed from database using celery-beat cron job.
  - celery is used to send the verication email during registration process and Redis is used as the message broker.
  - Incorporated Celery-Beat as a cron job to automatically remove soft-deleted user data from the database, optimizing system performance and storage management.
