from django.urls import path
import Receipts.views as Receipts

urlpatterns = [
    path("receipts",Receipts.receipt_view,name="receipt"),
    path("get_receipts",Receipts.get_receipts,name="all"),
    path("user_receipts/<int:pk>",Receipts.get_user_receipts,name="user_receipts")
]