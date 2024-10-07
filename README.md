#MLFLOW SETUP LOCALLY

- When we run experiments on our model we cannot do it in our production server model and thats not a good practice. So , we need to setup *mlflow* locally for our dummy 
experiments and log these expeiments in mlflow locally.
- Mlflow tracking server is required for my backend and artifact store to update the parameters values, metric values and atifacts respectively. For the backend store,
 I am using postgreSQL docker container and local storage for artifact store.
- I have also deployed MLflow tracking server container where MLflow is running. This container is responsible for serving the MLflow UI and communicating with the PostgreSQL backend
 (which stores the tracking metadata) and potentially the artifact store.
- In *docker-compose.yaml* I defined volumes for postgres databse and for artifact store and also going to write services for the databse and tracking server with
environment file. For tracking server, i have created my own image which is specified in dockerfile, the tracking server depends on back-end store
- docker-compose.yaml file is actually used when you are debugging locally and it is not used when we deploy mlflow on cloud.
- In *.envs* file, i have created *mlflow-common* file where i will keep my common environemtn variables that i am going to use for local installations, you can as well
 include remote configurations in the same file and deploy mlflow on cloud services.
- In *.envs*, there is *mlflow-dev*, were it hold ebvironment variables for development mlflow instance(local installations), i will address database(postgresql), artifact-store on my local machine.
- I have runned a script in docker directory called "run-server.sh" which runs the script whenever I start the container and start mlflow_tracking_server.
 run-server.sh will have host 0.0.0.0 that is going to run from docker and later we an access it from localhost, define our artifact-root ML_ARTIFACT_STORE, backend services ML_BACKEND
 and URI for the localhost to access MLflow. whatever variables I define in run-server.sh script is mapped to the environment variables declared in *.envs* file.
- In *Makefile*, I am going to include environment variables, it helps in consistency and ensures that the same variable are available acroos different systems and stages of development pipeline.
this consistency is critical when running tools like docker,mlflow and other tools which rely on specific configurations.
- In *Dockerfile*, as base image i have used python-3.11-slim image, which is lightweight version of 3.11,
 declared environement variables like virtual environment and modified the path so that executables in virtual environment are prioritized.
  and declared PYTHONUNBUFFERED  to make sure that python outputs are immediately flushed to the console with any delay
 this is helpful for real-time debugging and monitoring of the application's behaviour during execution.
 and install git which is needed by MLflow. Install poetry and copy pyproject.toml file and lock file to the container, "Poetry" Dependency resolution and locking can prevent errors
 that may arise in the future, and ease reproducibility. We all use external libraries in our projects and we don't want to have control over what maintainers of these libraries do
 whenever they upgrade the version of their packages. In pyproject.toml file as dependencies it only has mlflow and psycopg(which
 is a modern implementation of a postgreSQL adapter for python).
