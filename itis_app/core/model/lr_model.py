from itis_proj.settings import MEDIA_ROOT

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

_columns = ['anaemia', 'DEATH_EVENT', 'diabetes', 'high_blood_pressure', 'serum_creatinine', 'serum_sodium', 'sex',
            'smoking']


def model_data():
    df_1 = pd.read_csv(MEDIA_ROOT + 'heart_failure_clinical_records_dataset.csv', index_col=0, decimal=',')
    df_y = df_1['DEATH_EVENT']

    return df_1, df_y


def _classification(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    lr = linear_model.LogisticRegression(max_iter=1000)
    lr.fit(x_train, y_train)
    test_predictions = lr.predict(x_test)
    r2 = round(lr.score(x_test, y_test), 4)

    return y_test, test_predictions, r2


def classification(x, y, data):
    col = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'time']
    #user_frame = pd.DataFrame.from_records(data, columns=col)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    lr = linear_model.LogisticRegression(max_iter=1000)
    lr.fit(x_train, y_train)
    #answer_predictions = lr.predict(user_frame)
    # no eat user_frame
    answer_predictions = 1

    return answer_predictions


def check_health(user_data):
    df_1, df_y = model_data()
    df_x_1 = df_1.drop(_columns, axis=1)
    answer = classification(df_x_1, df_y, user_data)

    return answer
