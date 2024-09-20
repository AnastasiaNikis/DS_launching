class Data_processing:

    def EmptyData(dataset):
        column_names = dataset.columns.tolist()
        for column in column_names:
            nulls = dataset[column].isnull().sum()
            print(f'в столбце {column} - {nulls} пустых значений')


    def FulFill(dataset):
        column_names = dataset.columns.tolist()
        print('Заменены пустые значения:')
        for column in column_names:
            if dataset[column].dtypes == object:
                top = dataset[column].mode()
                dataset[column].fillna(top[0], inplace=True)
                print(f'в столбце {column} - мода {top[0]} - категориальное значение')
            else:
                median_value = dataset[column].median()
                dataset[column].fillna(median_value, inplace=True)
                print(f'в столбце {column} - медиана {median_value}')