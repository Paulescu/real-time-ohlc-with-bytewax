.PHONY: deploy delete list project-files run

# install Poetry and Python dependencies
init:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install

# run the feature-pipeline locally
run:
	poetry run streamlit run src/frontend.py