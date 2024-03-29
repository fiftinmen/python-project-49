setup: install build package-force-reinstall

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

package-force-reinstall:
	python -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games