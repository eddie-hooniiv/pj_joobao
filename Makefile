# 가상환경 이름
VENV_NAME=venv

# 가상환경 생성
$(VENV_NAME):
	python3 -m venv $(VENV_NAME)

# 가상환경에 필요한 패키지 설치
install: $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && $(VENV_NAME)/bin/pip install -r requirements.txt

# 가상환경 생성 및 패키지 설치
shell: install