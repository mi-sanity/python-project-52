MANAGE := uv run python manage.py

.PHONY: test
test:
	uv run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@uv sync

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: makemigrations
makemigrations:
	@$(MANAGE) makemigrations

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: build
build:
	./build.sh

.PHONY: render-start
render-start:
	gunicorn task_manager.wsgi

.PHONY: collectstatic
collectstatic:
	@$(MANAGE) collectstatic --noinput

.PHONY: lint
lint:
	uv run ruff check task_manager

.PHONY: check
check:
	uv run ruff check .

.PHONY: fix
fix:
	uv run ruff check --fix .

.PHONY: translate-makemessages
translate-makemessages:
	@$(MANAGE) makemessages -l ru

.PHONY: translate-compile
translate-compile:
	@$(MANAGE) compilemessages

.PHONY: start
start:
	uv run manage.py runserver

.PHONY: ci-install
ci-install:
	uv sync --group dev

.PHONY: ci-migrate
ci-migrate:
	uv run python manage.py makemigrations --noinput && \
	uv run python manage.py migrate --noinput

.PHONY: ci-test
ci-test:
	uv run coverage run --omit='*/migrations/*,*/settings.py,*/venv/*,*/.venv/*' -m pytest --ds=task_manager.settings --reuse-db
	uv run coverage xml
	uv run coverage report --show-missing --skip-covered