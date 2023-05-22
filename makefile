build: test_requirements test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install --upgrade pip
	pip install -e .[test]

flake8:
	flake8 .

pytest:
	ENV_FILES='test,dev' \
	pytest $(ARGUMENTS) \
	--ignore=node_modules \
	--capture=no \
	--nomigrations \
	--reuse-db \
	-Wignore::DeprecationWarning \
	-vv

pytest_single:
	ENV_FILES='test,dev' \
	pytest \
	    $(ARGUMENTS)
		--junit-xml=./results/pytest_unit_report.xml \
		--cov-config=.coveragerc \
		--cov-report=html \
		--cov=. \

pytest_codecov:
	ENV_FILES='test,dev' \
	pytest \
		--cov-config=.coveragerc \
		--cov-report=term \
		--cov=. \
		--codecov \
		$(ARGUMENTS)
		

CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

test: flake8 pytest
	$(CODECOV)

compile_requirements:
	python3 -m piptools compile requirements.in

compile_test_requirements:
	python3 -m piptools compile requirements_test.in

compile_all_requirements: compile_requirements compile_test_requirements

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$DIRECTORY_PYPI_USERNAME --password $$DIRECTORY_PYPI_PASSWORD dist/*


.PHONY: build clean test_requirements flake8 pytest test compile_requirements compile_test_requirements compile_all_requirements publish
