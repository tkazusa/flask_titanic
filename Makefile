FRONTEND_DIR := frontend/

FRONTEND_IMAGE := frontend:v1.0

FRONTEND_CONTAINER := frontend

PROJECT_ID := "flask-titanic"


.PHONY: build
build: frontend/ 
	 sudo docker build -t  $(FRONTEND_IMAGE) $(FRONTEND_DIR)

.PHONY: up
up:
	sudo docker-compose up -d

.PHONY: clean
	sudo docker-compose stop
	sudo docker-compose down

.PHONY: stop
stop:
	sudo docker-compose stop

.PHONY: down
down:
	sudo docker-compose down
	
.PHONY: clean
clean:
	 docker stop $(FRONTEND_CONTAINER)
	 docker rm $(FRONTEND_CONTAINER)
	 docker rmi $(FRONTEND_IMAGE)

.PHONY: install
install: requirements.txt
	pip intall -r requirements.txt

.PHONY: run
run:
	 sudo docker run -itd --name $(FRONTEND_CONTAINER) -p 8080:8080 -e PROJECT_ID=$(PROJECT_ID) $(FRONTEND_IMAGE)

