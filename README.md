# Подбор вакансий к резюме

NLP проект в рамках курса **Глубокое обучение на практике**

Команда:
- Борисов Дмитрий Сергеевич (@dsborisov)
- Изюмова Анастасия Витальевна (@starminalush)
- Азаматов Ильдар Русланович (@eelduck)

## Содержание репозитория

- В папке [src/](/src/) содержится исходный код проекта.
- В папке [notebooks/](/notebooks/) содержатся jupyter ноутбуки с экспериментами


## Начало работы

### Подготовка окружения

- Устанавливаем `python 3.10`
    - Windows

      Устанавливаем через [официальный установщик](https://www.python.org/downloads/)

    - Linux

        ```bash
        sudo apt install python3.10
        ```

- Устанавливаем [poetry](https://python-poetry.org/docs/#installation)
    - Windows

      Используйте [официальные инструкции](https://python-poetry.org/docs/#windows-powershell-install-instructions)
      или команду `powershell`

        ```powershell
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        ```

    - Linux

        ```bash
        curl -sSL https://install.python-poetry.org | python3 -
        ```
- Устанавливаем требуемые пакеты с помощью команды
    ```bash
    poetry install
    ```

## Запуск системы

- Для запуска системы введите команды
    ```bash
    cd src/
    python gradio_app.py
    ```
  После этого у вас запустится Gradio приложение по адресу http://localhost:7860/

## Демо
TBD

## Эксперименты
TBD

## Сравнение энкодеров
| Модель | Accuracy |  Precision@10 | Recall@10 | F1@10 |
| --- | --- | --- | --- | --- |
| [intfloat/multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large)| 0.830 |  0.175 | 0.124 | 0.145 |
| [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)| 0.805 |  0.156 | 0.180 | 0.127 |
| [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)| 0.810 |  0.138 | 0.094 | 0.111 |
| [sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1)| 0.831 |  0.131 | 0.091 | 0.107 |
| [cointegrated/LaBSE-en-ru](https://huggingface.co/cointegrated/LaBSE-en-ru)| 0.823 |  0.169 | 0.119 | 0.139 |