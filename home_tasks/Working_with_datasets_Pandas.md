# Лекция «Работа с датасетами. Pandas»

**Что такое Pandas?**
Pandas — это библиотека Python, предназначенная для удобной работы с данными. Она предоставляет мощные структуры данных, такие как **DataFrame** и **Series**, которые позволяют легко манипулировать, анализировать и визуализировать данные. Pandas широко используется в анализе данных, обработке данных и машинном обучении.

**Установка Pandas**
Если библиотека Pandas не установлена, её можно добавить командой:

*pip install pandas*
# Основные структуры данных: Series и DataFrame
## 1. Series
   Series — это одномерная структура данных, похожая на массив, но с индексами.
   
**Пример:**
*import pandas as pd*

*data = [10, 20, 30, 40]*
*series = pd.Series(data, index=['a', 'b', 'c', 'd'])*
*print(series)*

<ins>Вывод:</ins>
*a    10*
*b    20*
*c    30*
d    40*
*dtype: int64*
Здесь a, b, c, d — это индексы, а 10, 20, 30, 40 — значения.
## 2. DataFrame
DataFrame — это двумерная таблица данных с индексами строк и колонок.

**Пример:**
*data = {'Name': ['Alice', 'Bob', 'Charlie'],*
`    `*'Age': [25, 30, 35],*
`    `*'Salary': [50000, 60000, 70000]}*
*df = pd.DataFrame(data)*
*print(df)*

<ins>Вывод:</ins>
	Name Age Salary
0   Alice   25   50000
1     Bob   30   60000
2  Charlie   35   70000
### 2.1 Создание DataFrame из разных источников
#### 1. Из словаря:
*data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}*
*df = pd.DataFrame(data)*
*print(df)*
#### 2. Из списка списков:
*data = \[[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]*
*df = pd.DataFrame(data, columns=['ID', 'Name'])*
*print(df)*
#### 3. Чтение из файла:
Pandas позволяет читать данные из различных форматов файлов: CSV, Excel, SQL.
**Чтение CSV:**
*df = pd.read\_csv('data.csv')*
*print(df.head())  # Показывает первые 5 строк*
### 2.2 Основные методы работы с DataFrame
#### 1. Просмотр данных:
 *df.head(n)* — первые n строк (по умолчанию 5).
 *df.tail(n)* — последние n строк.
#### 2. Получение информации о данных:
*print(df.info())       # Информация о типах данных и пропусках*
*print(df.describe())   # Статистическое описание числовых данных*
#### 3. Доступ к данным:
- По имени столбца:
*print(df['Name'])  # Вывести столбец "Name"*

- По индексу строки
*print(df.loc[0])  # Первая строка*

- По индексу строки и столбца
*print(df.iloc[0, 1])  # Значение первой строки второго столбца*
### Практика:

- Создайте DataFrame, используя данные о студентах (имя, возраст, баллы).
------------------------------------------------------------------
import pandas as pd

data_dict = {'Name': ['John', 'George', 'Ann', 'Mary', 'Deby', 'Chris'],
	             'Age': [20, 25, 35, 40, 33, 23],
	             'Score': [6, 7, 8, 9, 10, 5]}
df = pd.DataFrame(data_dict)

print(df)

    Name  Age  Score
0    John   20      6
1  George   25      7
2     Ann   35      8
3    Mary   40      9
4    Deby   33     10
5   Chris   23      5

- Вывести первые 3 строки.
--------------------------
print(df.head(3))

     Name  Age  Score
0    John   20      6
1  George   25      7
2     Ann   35      8

- Посчитать средний возраст.
----------------------------
print(df["Age"].mean())

29.333333333333332

- Выбрать всех студентов с баллами выше определённого значения.
---------------------------------------------------------------
print(df.loc[df['Score']>7])
print(df[df['Score']>7]) # или такой вариант

	Name  Age  Score
2   Ann   35      8
3  Mary   40      9
4  Deby   33     10
### 2.3 Обработка данных и операции с DataFrame

#### 1. Добавление и удаление данных

1. **Добавление нового столбца:**
   Создать новый столбец можно с помощью простой присваивающей операции.
   
**Пример:**
   *import pandas as pd*
 *data = {'Name': ['Alice', 'Bob', 'Charlie'],
   `    `'Age': [25, 30, 35]}*
   *df = pd.DataFrame(data)*
   *df['Salary'] = [50000, 60000, 70000]  # Новый столбец*
   *print(df)*
   
<ins>Вывод:</ins>
`    `Name  Age  Salary
0   Alice   25   50000
1     Bob   30   60000
2  Charlie   35   70000

2. **Удаление столбцов и строк:**
- Удаление столбца
*df = df.drop(columns=['Salary'])*
- Удаление строки:
*df = df.drop(index=[0])  # Удаляет строку с индексом 0*
### Фильтрация данных

1. **Условная фильтрация:**
   Можно выбрать строки, соответствующие определённым условиям.

   **Пример:**
*filtered\_df = df[df['Age'] > 25]*
*print(filtered\_df)*

<ins>Вывод:</ins>
`    `Name  Age  Salary
1     Bob   30   60000
2  Charlie   35   70000

2. **Фильтрация по нескольким условиям:**
Используйте & (и) или | (или) для комбинирования условий.

**Пример:**
*filtered\_df = df[(df['Age'] > 25) & (df['Salary'] > 60000)]*
*print(filtered\_df)*
### Изменение данных

1. **Обновление значений в столбце:**
*df['Salary'] = df['Salary'] \* 1.1  # Увеличить зарплаты на 10%*

2. **Замена данных:**
   Используйте метод replace().
*df['Name'] = df['Name'].replace({'Alice': 'Alicia'})*
### Работа с пропущенными значениями

1. **Поиск пропусков:**
print(df.isnull())  # Возвращает DataFrame с True для пропущенных значений

print(df.isnull().sum())  # Считает количество пропусков в каждом столбце

2. **Удаление строк или столбцов с пропусками:**
- Удалить строки:
*df = df.dropna()*

- Удалить столбцы:
*df = df.dropna(axis=1)*

3. **Заполнение пропусков:**
Можно заполнить пропуски определённым значением или средним.

*df['Age'] = df['Age'].fillna(30)  # Заполнить пропуски значением 30*

*df['Salary'] = df['Salary'].fillna(df['Salary'].mean())  # Средним*
### Группировка данных

1. **Группировка и агрегирование:**
   Используйте groupby() для разделения данных на группы.

   **Пример:**
*data = {*
`    `*'Department': ['HR', 'IT', 'HR', 'IT'],*
`    `*'Salary': [50000, 60000, 55000, 65000]*
*}*
*df = pd.DataFrame(data)*
*grouped = df.groupby('Department')['Salary'].mean()*
*print(grouped)*

<ins>Вывод:</ins>
*Department*
*HR  52500.0*
*IT    62500.0*
*Name: Salary, dtype: float64*

2. **Агрегация нескольких столбцов:**
*aggregated = df.groupby('Department').agg({'Salary': ['mean', 'max']})*
*print(aggregated)*

<ins>Вывод:</ins>
	Salary       
    mean    max
Department                
HR        52500.0  55000
IT          62500.0  65000
### Практика:

- Создайте DataFrame с информацией о продажах (категория, количество, доход).
----------------------------------------------------------------------
import pandas as pd

data_dict = {'Category': ['HDD', 'SSD', 'CPU', 'DDR', 'HDD', 'HDD', 'SSD', 'CPU', 'DDR', 'CPU' ],
	             'Amount': [10, 20 30, 40, 50, 60, 70, 80, 90, 100 ],
	             'Sum': [100, 200 300, 400, 500, 600, 700, 800, 900, 1000]}
df = pd.DataFrame(data_dict)
  
Category  Amount   Sum
0      HDD      10   100
1      SSD      20   200
2      CPU      30   300
3      DDR      40   400
4      HDD      50   500
5      HDD      60   600
6      SSD      70   700
7      CPU      80   800
8      DDR      90   900
9      CPU     100  1000

- Найти средний доход по каждой категории.
---------------------------------------------------------------------------
df = df.groupby('Category')['Sum'].mean()

Category
CPU    700.0
DDR    650.0
HDD    400.0
SSD    450.0
Name: Sum, dtype: float64

- Удалить строки с пропущенными данными.
-------------------------------------------------------------------------------
Category  Amount    Sum
0      HDD    10.0  100.0
1      SSD    20.0    NaN
2      CPU    30.0  300.0
3      DDR     NaN  400.0
4      HDD    50.0  500.0
5      HDD    60.0  600.0
6      SSD    70.0  700.0
7      CPU     NaN  800.0
8      DDR    90.0  900.0
9      CPU   100.0    NaN

df = df.dropna()
Category  Amount    Sum
0      HDD    10.0  100.0
2      CPU    30.0  300.0
4      HDD    50.0  500.0
5      HDD    60.0  600.0
6      SSD    70.0  700.0
8      DDR    90.0  900.0

- Увеличить доходы на 20%.
--------------------------------------------------------------------------
df['Sum'] = df['Sum']*1.2
 Category  Amount     Sum
0      HDD    10.0   120.0
1      SSD    20.0     NaN
2      CPU    30.0   360.0
3      DDR     NaN   480.0
4      HDD    50.0   600.0
5      HDD    60.0   720.0
6      SSD    70.0   840.0
7      CPU     NaN   960.0
8      DDR    90.0  1080.0
9      CPU   100.0     NaN

### Продвинутая работа с данными
#### Слияние, объединение и соединение DataFrame

1. **Объединение с помощью concat:**
   Используется для вертикального или горизонтального объединения двух или более DataFrame.

   **Пример:**
*import pandas as pd*
*df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})*
*df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Age': [35, 40]})*
*combined = pd.concat([df1, df2], ignore\_index=True)*
*print(combined)*

<ins>Вывод:</ins>
    `Name  Age
0   Alice   25
1     Bob   30
2  Charlie   35
3   David   40

**Соединение с помощью merge:**
Используется для соединения DataFrame по ключевым столбцам, аналогично SQL JOIN.

**Пример:**
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salary': [50000, 60000, 70000]})
merged = pd.merge(df1, df2, on='ID', how='inner')  # Внутреннее соединение
print(merged)

<ins>Вывод:</ins>
    `ID    Name  Salary
0    1   Alice   50000
1    2     Bob   60000
  
*Доступные виды соединений:*
- inner — внутреннее (по совпадающим значениям ключа).
- left — левостороннее (все из первого, только совпадающие из второго).
   ID   Name  Salary
0   1    Alice  50000.0
1   2      Bob  60000.0
2   3  Charlie      NaN
- right — правостороннее.
   ID   Name  Salary
0   1  Alice   50000
1   2    Bob   60000
2   4    NaN   70000
- outer — полное соединение.
   ID     Name   Salary
0   1    Alice  50000.0
1   2      Bob  60000.0
2   3  Charlie      NaN
3   4      NaN  70000.0
  
Добавление строк с помощью append (устарело, использовать concat):
*new\_row = {'Name': 'Eve', 'Age': 29}*
*df = df1.append(new\_row, ignore\_index=True)*
*print(df)*
#### Преобразование данных

1. **Изменение названий столбцов:**
*df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)*

2. **Поворот таблицы с помощью pivot:**
   Используется для перестройки таблицы.

**Пример:**
*data = {*
`    `*'Date': ['2023-01-01', '2023-01-01', '2023-01-02'],*
`    `*'Category': ['A', 'B', 'A'],*
`    `*'Value': [100, 200, 150]*
*}*
*df = pd.DataFrame(data)*

  Date Category  Value
0  2023-01-01        A    100
1  2023-01-01        B    200
2  2023-01-02        A    150

*pivoted = df.pivot(index='Date', columns='Category', values='Value')*
*print(pivoted)*

<ins>Вывод:</ins>
Category           A      B
Date                      
2023-01-01     100.0  200.0
2023-01-02     150.0    NaN

3. **"Расплавление" таблицы с помощью melt:**
Обратная операция pivot, преобразует таблицу в длинный формат.
*melted = pivoted.reset\_index().melt(id\_vars='Date', value\_name='Value')*
*print(melted)*

<ins>Вывод:</ins>
Date Category  Value
0  2023-01-01        A  100.0
1  2023-01-02        A  150.0
2  2023-01-01        B  200.0
3  2023-01-02        B    NaN
#### Индексация и сортировка

1. **Сортировка данных:**
- По столбцу:
df = df.sort\_values(by='Age', ascending=False)

- По индексу:
*df = df.sort\_index()*

2. **Установка нового индекса:**
*df.set\_index('Name', inplace=True)*

3. **Сброс индекса:**
df.reset\_index(inplace=True)

### **Практика:**

Cоздайте два DataFrame с данными о студентах (ID, имя, курс) и их оценках (ID, предмет, оценка).

---------------------------------------------------------------------------
data1 = {'ID': ['b001', 'b002', 'b004', 'm001', 'm002'],
        'Name': ['Piter', 'Wes', 'Kate', 'Jack', 'Alice'],
        'Course': ['01', '02', '04', '05', '06']}
data2 = {'ID': ['b001', 'b002', 'b004', 'm001', 'm002'],
         'Linguistics': [3, 4, 5, 6, 7],
         'Physics': [6, 4, 5, 9, 3],
         'Chemistry': [3, 8, 5, 9, 7],
         'Computer Science': [7, 4, 8, 6, 5]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)

1  b002    Wes     02
2  b004   Kate     04
3  m001   Jack     05
4  m002  Alice     06
     ID  Linguistics  Physics  Chemistry  Computer Science
0  b001            3        6          3                 7
1  b002            4        4          8                 4
2  b004            5        5          5                 8
3  m001            6        9          9                 6
4  m002            7        3          7                 5

- Объедините их с помощью merge.
---------------------------------------------
merged_df = pd.DataFrame.merge(df1, df2, on='ID', how = 'left')
print(merged_df)

ID   Name Course  Linguistics  Physics  Chemistry  Computer Science
0  b001  Piter     01            3        6          3                 7
1  b002    Wes     02            4        4          8                 4
2  b004   Kate     04            5        5          5                 8
3  m001   Jack     05            6        9          9                 6
4  m002  Alice     06            7        3          7                 5

- Создайте сводную таблицу с оценками по предметам.
----------------------------------------------------------
df = merged_df.T
df.columns = list(df.loc['Name'])
df = df.drop(index=['ID', 'Name', 'Course'])
df.index.name = 'Objects'

	       Piter Wes Kate Jack Alice
Objects                                   
Linguistics          3   4    5    6     7
Physics              6   4    5    9     3
Chemistry            3   8    5    9     7
Computer Science     7   4    8    6     5

- Рассчитайте средние оценки для каждого студента.
-----------------------------------------------------------------------
data_mean = {'Name': ['Piter', 'Wes', 'Kate', 'Jack', 'Alice'],
             'Score_mean': [df['Piter'].mean(), df['Wes'].mean(), df['Kate'].mean(), df['Jack'].mean(), df['Alice'].mean()]}
df_mean = pd.DataFrame(data_mean)

Name  Score_mean
0  Piter        4.75
1    Wes        5.00
2   Kate        5.75
3   Jack        7.50
4  Alice        5.50

# Работа с реальными данными и сохранение результатов

## Чтение и запись данных из/в различные форматы

### 1. Чтение данных из файлов:
   1. **CSV:**
      df = pd.read\_csv('data.csv')
   2. **Excel:**
      df = pd.read\_excel('data.xlsx', sheet\_name='Sheet1')
   3. **SQL:**
      import sqlite3
      conn = sqlite3.connect('database.db')
      df = pd.read\_sql('SELECT \* FROM table\_name', conn)
### 2. Запись данных в файл:
   1. **CSV:**
      df.to\_csv('output.csv', index=False)  # Без индекса
   2. **Excel:**
	  df.to\_excel('output.xlsx', index=False)
   3. **SQL:**
      df.to\_sql('table\_name', conn, if\_exists='replace', index=False)
### 3. Обработка больших датасетов
Работа с большими файлами требует оптимизации для сохранения памяти.
1. **Чтение файла по частям:**
   Используйте параметр chunksize.
     for chunk in pd.read\_csv('large\_file.csv', chunksize=1000):
  `   `process(chunk)  # Ваша функция обработки данных

2. **Оптимизация типов данных:**
   Укажите типы данных для столбцов.
   df = pd.read\_csv('data.csv', dtype={'column1': 'int32', 'column2': 'float32'})

3. **Работа с компрессией:**
   Pandas поддерживает чтение и запись сжатых файлов.
   df.to\_csv('compressed.csv.gz', index=False, compression='gzip')
## Визуализация данных с Pandas
Для базовой визуализации данных в Pandas можно использовать встроенный метод .plot().
**Пример:**
import pandas as pd
import matplotlib.pyplot as plt
data = {'Category': ['A', 'B', 'C'], 'Values': [100, 200, 150]}
df = pd.DataFrame(data)
df.plot(kind='bar', x='Category', y='Values', title='Bar Plot')
plt.show()
### Практика на реальных данных
1. **Чтение данных из файла:**
   Загрузите датасет titanic.csv (или любой другой).
	df = pd.read\_csv('titanic.csv')

2. **Анализ данных:**
   1. Посмотрите структуру данных:
      print(df.info())
       print(df.describe())
       
   2. Найдите долю выживших пассажиров:
      survival\_rate = df['Survived'].mean() \* 100
      print(f"Survival Rate: {survival\_rate:.2f}%")

3. **Фильтрация данных:**
   1. Выберите только пассажиров первого класса:
      first\_class = df[df['Pclass'] == 1]
      print(first\_class.head())
      
4. **Группировка и агрегация:**
   1. Найдите средний возраст пассажиров по классам:
      avg\_age = df.groupby('Pclass')['Age'].mean()
      print(avg\_age)

5. **Сохранение результатов:**
   Сохраните отфильтрованные данные в новый файл:
	first\_class.to\_csv('first\_class\_passengers.csv', index=False)