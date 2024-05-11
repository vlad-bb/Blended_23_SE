1) Docker build image
```docker build . --platform=linux/amd64 -t hajusag/test_cron:0.0.1```

2) Завантаження/Upload образу на DockerHub
```docker push hajusag/test_cron:0.0.1```

3) Завантаження/Upload образу на Server
```docker pull hajusag/test_cron:0.0.1```

4) Create run time in Cron Ubunty https://crontab.guru/
```crontab -e```

5) Запуск Docker контейнеру на сервері
```docker run --rm --name cron_test_docker -v /home/data:/data hajusag/test_cron:0.0.1```

6) подивитися на запущенні контенери 
```docker ps -a```
7) подивитися на скаченні імаджи
```docker images```
8) видалити непотрібний image
```docker rmi <id>```
9) Запустити зупинений контейнер
```docker start <id container>```
10) Зупинити контейнер
```docker stop <id container>```
11) Перезапустити контейнер
```docker restart <id container>```
12) Подивитися логи
```docker logs <id container>```
13) Підключитися до запущенного контейнеру
```docker attach <id container>```