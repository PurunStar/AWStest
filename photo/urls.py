from django.urls import path
from .views import PhotoMylist, PhotoLike, PhotoList, PhotoDelete, PhotoCreate, PhotoUpdate, PhotoDetail

#다른 앱들과 url parttern이름이 겹치는것을 방지하기 위해 사용 
app_name = "photo"
urlpatterns = [
    #함수형 뷰는 이름만 적지만
    #클래스형 뷰는 이름.as_view()로 작성 name은 나중에 불러쓰기 위해 저장
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>", PhotoDetail.as_view(), name='detail'),
    #전체 사진을 보여주는 photolist
    path("",PhotoList.as_view(), name='list'),
    # path("", views.base, name='list'),

    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("mylist/", PhotoMylist.as_view(), name='mylist')
]
