# Описание проекта - Построение дашборда 

## Файлы в папке
| Название файла | Описание | 
| :---------------------- | :---------------------- |
| [Тетрадь проекта](build_dashboard.ipynb) | Тетрадь Jupyter Notebook с описанием проекта, целями, агрегации выгруженных данных |
| [Презентация проекта](dash_presentation.pdf) | Презентация проекта для менеджеров контента |
| [Пайплайн проекта](pipeline_script.py) | Скрипт для автоматической агрегации сырых данных и записи агрегированных таблиц в БД |

## Данные

В наличии были сырые данные о взаимодействии пользователей со статьями на сайте.

## Задачи

1) Скачать сырые данные из БД.
2) Создать скрипт пайплайна для агрегации сырых данных и записи агрегированных в БД.
3) По агрегированным данным создать дашборд в Tableau Public по заранее согласованному ТЗ.

## Используемые библиотеки
*pandas*, *Tableau*, *SQLAlchemy*, *crontab*

## Выводы
1. Создан шаблон [скрипта пайплайна проекта](pipeline_script.py) для автоматической агрегации сырых данных.
2. Дашборд проекта можно найти по ссылке на Tableau Public:
https://public.tableau.com/views/Card_Dash_for_studies/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

3. Создана [презентация](dash_presentation.pdf) для менеджеров по использованию даша и выводами по данным.

## Статус проекта
Завершен.