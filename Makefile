help:
	@echo "Automation tasks"

connect:
	ssh-add

deploy:
	@echo "Deploying app"
	ssh cryptogram "\
		cd prod			&&\
		git pull		&&\
		docker-compose down &&\
		docker-compose up -d &&\
		echo 'completed!'"
	@echo "App deployed"

remote-migrate:
	ssh cryptogram "\
	cd prod &&\
		docker-compose exec app python manage.py migrate &&\
		echo 'migrated!'"
