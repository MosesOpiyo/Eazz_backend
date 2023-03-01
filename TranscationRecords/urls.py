from django.urls import path
from TranscationRecords import views as Records

urlpatterns = [
    path('TransactionRecord',Records.transactionRecord_view,name="transaction_record"),
    path('TransactionRecords',Records.get_records,name="records")
]