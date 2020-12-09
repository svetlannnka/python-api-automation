# docker build -t pytest_check .
# docker run --rm --mount type=bind,src=$(pwd),target=/tests/ pytest_check python -m pytest -s --alluredir=test_results/ framework_example/tests/

FROM python

WORKDIR /tests

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD  python -m pytest --help