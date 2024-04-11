setup: install build package-force-reinstall

setup-linux: install build package-force-reinstall-linux

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

package-force-reinstall-linux:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

remove-envs:
	rm -rf .venv && poetry env remove --all