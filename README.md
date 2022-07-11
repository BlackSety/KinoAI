# KinoAI
### Проект для практики МАИ по Online cinema

Онлайн кинотеатр, на основе технологии [Webtorrent](https://webtorrent.io/intro), для трансляции требуется раздача с другого устройства
### Для работы сервера требуются, установленные в виртуальную среду:
- django
- pillow
- sqlparse
- asgiref
##### необходимые версии указаны в requirements.txt
## Поддерживается работа с [Docker](https://www.docker.com/)
  1. Установить docker.
  2. Зайти в папку проекта и ввести команду:  
  > docker -t image_name .
  3. Ввести команду:
  > docker images
  4. скопировать IMAGE ID вашего имеджа.
  5. Ввести команду:
  > docker run -p 8000:8000 -d IMAGE_ID
  6. Ввести команду:
  > docker ps 
  7. проверить запущен ли процесс image_name которого совпадает с введённым.
