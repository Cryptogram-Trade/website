help:
	@echo "Automation tasks"

deploy:
	@echo "Deploying app"
	ssh-add
	ssh cryptogram "\
		cd prod			&&\
		git pull		&&\
		docker-compose down &&\
		docker-compose up -d  &&\
		echo 'completed!'"
	@echo "App deployed"
