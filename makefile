build: test_requirements test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

flake8:
	flake8 . --exclude=.venv/

pytest:
	pytest . --cov=. --cov-config=.coveragerc --capture=no $(pytest_args)

CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

compile_requirements:
	python3 -m piptools compile requirements.in

compile_test_requirements:
	python3 -m piptools compile requirements_test.in

compile_all_requirements: compile_requirements compile_test_requirements

test: flake8 pytest
	$(CODECOV)


.PHONY: build clean test_requirements flake8 pytest test
