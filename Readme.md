# Дипломный проект "Сайт медицинской компнаии"

## Запуск проекта
### 1. Открыть терминал
### 2. С помощью команды cd перейти в каталог, где будет размещён проект.
### 3. Выполнить команду для клонирования проекта:
git clone https://github.com/TonyShikhovtsev/Medical-company-website.git

### 4. Перейти в каталог проекта
cd course_work_8_docker

### 5. В корневой папке проекта создать файл .env
touch .env

### 6. Открыть файл
nano .env

### 7. Записать в файл следующие настройки

PASSWORD_DATABASE=

### 8. Запустить проект с помощью Docker, используя следующую команду:
docker-compose build --no-cache && docker-compose up


### В проекте использованы следующие компоненты:
#### Django==5.0.2;
#### bootstrap;
#### postgresql;
#### psycopg2-binary==2.9.9
#### Более подробно см. файл requirements.txt






