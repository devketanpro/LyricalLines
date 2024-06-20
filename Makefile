BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
WHITE ?= \033[1;37m
COFF ?= \033[0m

.PHONY: all shell build runserver test

all: help

help:
	@echo -e "\n$(WHITE)Available commands:$(COFF)"
	@echo -e "$(CYAN)make build$(COFF)            - Sets up the project in your local machine."
	@echo -e "                        This includes building Docker containers and running migrations."
	@echo -e "$(CYAN)make start$(COFF)        - Runs the django app in the container, available at http://127.0.0.1:8000"
	@echo -e "$(CYAN)make shell$(COFF)            - Starts a Linux shell (bash) in the django container"
	@echo -e "$(CYAN)make down$(COFF)            - Down the containerised project in your local machine"
	@echo -e "$(CYAN)make superuser$(COFF)            - Create superuser to access django admin panel"


build:
	@echo -e "$(CYAN)Creating Docker images with all django basic setup:$(COFF)"
	@sudo docker-compose build

start:
	@echo -e "$(CYAN)Starting Bash in the web container:$(COFF)"
	@sudo docker-compose up -d

down:
	@sudo docker-compose down -v

shell:
	@echo -e "$(CYAN)Starting Bash in the web container:$(COFF)"
	@sudo docker exec -it lyricallines_web_1 python manage.py shell

createsuperuser:
	@echo -e "$(CYAN)Create superuser:$(COFF)"
	@sudo docker exec -it lyricallines_web_1 python manage.py createsuperuser
