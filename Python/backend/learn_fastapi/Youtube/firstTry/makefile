# checking environment:
# env name = defined name activate it or create venv base on defined name then activate it.
check_env:

	VENV_NAME=.fastapi_learning_env
	
	@if [ -d "$(VENV_NAME)" ]; then \
		echo "The virtual environment $(VENV_NAME) already exists."; \
		echo "Activating $(VENV_NAME)..."; \
		./$(VENV_NAME)/bin/activate; \
	else \
		echo "Creating virtual environment $(VENV_NAME)..."; \
		python -m venv $(VENV_NAME); \
		echo "Activating $(VENV_NAME)..."; \
		./$(VENV_NAME)/bin/activate; \
	fi

# install commands
# install requirement packages
install:
	#pip install -r requirements.txt

#format code
format:
	#formate code

# install lint
lint:
	#flake8 or black or pylint
	
# run test
test:
	#test
# deploy to production if is production
deploy:
	#deploy

dev: check_env install test
production: install lint test deploy