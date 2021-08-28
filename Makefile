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

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

push-all:
	git push --all origin

complete:
	rm -rf dist
	poetry build
	poetry install
	poetry publish --dry-run
	python3 -m pip install --force-reinstall dist/*.whl
