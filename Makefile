build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

