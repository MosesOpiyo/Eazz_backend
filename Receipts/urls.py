from django.urls import path
import Receipts.views as Receipts

urlpatterns = [
    path("receipts",Receipts.receipt_view,name="receipt"),
    path("get_receipts",Receipts.get_receipts,name="all"),
    path("statements",Receipts.get_statements,name="statement"),
    path("latest",Receipts.latest_statements,name="latest"),
    path("user_receipts/<int:id>",Receipts.get_user_receipts,name="user_receipts")
]