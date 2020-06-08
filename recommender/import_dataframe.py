import pandas as pd
from c_opportunities.models import ContractOpportunities

# import combined csv into model fields

data = pd.read_csv('../data/combined.csv')
# data['responseDeadLine'].fillna(value='', inplace=True)

for idx, row in data.iterrows():
        responseDeadLine=str(row['responseDeadLine'])
        if responseDeadLine == 'nan':
            responseDeadLine = None
        _, created = ContractOpportunities.objects.get_or_create(
                title=row['title'],
                noticeId=row['noticeId'],
                department=row['department'],
                subTier=row['subTier'],
                postedDate=row['postedDate'],
                deadline=responseDeadLine,
                link=row['uiLink'],
        )
