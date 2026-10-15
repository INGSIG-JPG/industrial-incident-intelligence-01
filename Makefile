.PHONY: all install ingest test run

all: install ingest test

install:
	pip install -r backend/requirements.txt

ingest:
	python pipelines/ingest_data.py

test:
	pytest backend/tests/test_api.py

run:
	cd backend && uvicorn app.main:app --reload
