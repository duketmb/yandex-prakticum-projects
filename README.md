# Репозиторий проектов для курса "Аналитик данных" от Яндекс.Практикум

## Описание выполненных проектов

Данные проекты были выполнены в ходе обучения в Яндекс.Практикуме по профессии "Аналитик данных".  
Выполненные проекты представлены в хронологическом порядке, благодаря чему можно проследить совершенствование используемых подходов в обращении с данными.
Удобнее просмотреть тетратки jupyter notebook можно через [nbviewer](https://nbviewer.org/github/duketmb/yandex-prakticum-projects/tree/main/) (работает перемещение по оглавлению, видны графики plotly).

| Название проекта | Описание | Используемые библиотеки | 
| :---------------------- | :---------------------- | :---------------------- |
| [1. Музыка больших городов](big_cities_music) | Сравнение предпочтений пользователей Яндекс.Музыки из Москвы и Санкт-Петербурга в зависимости от времени (утро и вечер) и дня недели (понедельник, среда, пятница)| *pandas* |
| [2. Исследование надежности заемщиков](reliability_of_debtors) | Проведение исследования, влияют ли на возврат кредита в срок такие факторы как количество детей, семейное положение, уровень дохода, цель кредита| *pandas* |
| [3. Исследование объявлений о продаже квартир](real_estate) | Исследование параметров объектов недвижимости, выявление отличия квартир в центре от всех остальных квартир| *pandas*, *matplotlib* |
| [4. Определение выгодного тарифа для телеком компании](telecom_tariffs) | Анализ поведения клиентов оператора связи и проверка статистических гипотез об отличии выручки тарифов| *pandas*, *matplotlib*, *seaborn*, *NumPy*, *SciPy.stats*, *statistics*|
| [5. Изучение закономерностей успешности игр](game_success_analysis) | Исследовательский анализ выпускаемых игр, определение актуального периода для построения прогноза, выбор потенциально прибыльных платформ и жанров, составление портретов игроков из разных регионов, проверка статистических гипотез о разности пользовательских оценок| *pandas*, *matplotlib*, *seaborn*, *NumPy*, *SciPy.stats*, *statistics* |
| [6. Анализ продуктовых метрик приложения](app_metrics) | Исследовательский анализ профилей пользователей приложения и оценка окупаемости рекламы по метрикам CR, RR, LTV, ROI, CAC| *pandas*, *matplotlib*, *seaborn*, *NumPy* |
| [7. Приоритезация и проверка гипотез](check_hypothesis) | По заранее выставленным оценкам проведена приоритезация гипотез по ICE и RICE. По приоритетной гипотезе был поставлен А/В-тест, результаты которого представлены графиками и статистическими тестами (по кумулятивной выручке, среднему чеку, конверсии)| *pandas*, *matplotlib*, *seaborn*, *NumPy*, *SciPy.stats* |
| [8. Исследование рынка общепита Москвы](catering) | Исследованы открытые данные о точках общепита Москвы для определения параметров проектируемого заведения. Для потенциальных инвесторов подготовлена презентация с рекомендациями| *pandas*, *Plotly*, *NumPy* |
| [9. Анализ пользовательского поведения в приложении](users_behavior_in_mobile_app) | Построение воронки событий для пользователей приложения и одновременное проведение A/A/B-теста о влиянии новых шрифтов на поведение пользователей| *pandas*, *matplotlib*, *Plotly*, *SciPy.stats*, *NumPy* |
| [10. Построение дашборда](dashboard_tableau) | Работа с сырыми данными из БД, агрегирование их для построение дашборда и само построение дашборда. Дополнительно написан скрипт для автоматической агрегации сырых данных и настроена его автономная работа через crontab| *pandas*, *Tableau*, *SQLAlchemy*, *crontab* |
| [11. Повышение качества работы с клиентами на основе ML](improving_quality_service_with_ML) | На основе данных о посетителях сети фитнес-центров спрогнозирована вероятность оттока для каждого клиента, с помощью кластеризации составлены портреты пользователей, даны рекомендации по удержанию клиентов| *pandas*, *matplotlib*, *seaborn*, *sklearn*, *scipy* |