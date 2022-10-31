init:
    pip install -r requirements.txt

venv: 
    source venv/bin/activate

test:
    py.test tests

.PHONY: init test venv
