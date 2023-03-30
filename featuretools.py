import featuretools as ft
import numpy as np
import pandas as pd

clients = pd.read_csv('clients.csv', parse_dates=['joined']) #loads datasets of clients
loans = pd.read_csv('loans.csv', parse_dates=['loan_start', 'loan_end']) #loads datasets of loans
payments = pd.read_csv('payments.csv', parse_dates=['payment_date']) #loads datasets of payemnt

es = ft.EntitySet(id='clients_data')

clients['join_month'] = clients['joined'].dt.month  # Makes 'Month Joined'
clients['log_income'] = np.log(clients['income'])  # Makes log_income

es = es.entity_from_dataframe(entity_id='clients',  # adding dataframe 
                              dataframe=clients,
                              index='client_id',
                              time_index='joined')
es = es.entity_from_dataframe(entity_id='loans',
                              dataframe=loans,
                              index='loan_id',
                              time_index='loan_start')
es = es.entity_from_dataframe(entity_id='payments',
                              dataframe=payments,
                              index='payment_id',
                              time_index='payment_date')

r_client_loan = ft.Relationship(es['clients']['client_id'], es['loans']['client_id']) #making relation between dataframes
es = es.add_relationship(r_client_loan)

r_loan_payment = ft.Relationship(es['loans']['loan_id'], es['payments']['loan_id'])
es = es.add_relationship(r_loan_payment)

agg_primitives = ['sum', 'count'] # use sum, count primitive methods
trans_primitives = [] # transform to there

features, feature_names = ft.dfs(entityset=es, target_entity='clients',
                                 agg_primitives=agg_primitives, trans_primitives=trans_primitives,
                                 max_depth=2)  # adding feature

loan_amount_total = features['SUM(loans.loan_amount)']   #adding feature
clients = clients.merge(loan_amount_total.reset_index(), on='client_id', how='left') # merging datas

print(clients.head(10)) #print output