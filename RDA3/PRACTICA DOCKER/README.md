docker build -t emenesesdev/alpine_practica:0.0.1.RELEASE .
docker container run -d -p 4000:4000 --name alpine_practica emenesesdev/alpine_practica:0.0.1.RELEASE