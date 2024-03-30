from django.shortcuts import render

# Create your views here.
def display(req):
    return render(req,'testapp/index.html')
def movie_info(req):
    head_msg='Movies Informaton'
    sub_msg1='BB movie is about love and effection of two countries people'
    sub_msg2='War is complete soldier movie'
    sub_msg3='Puspa 2 the rise will be upcoming blockbuster'
    type = 'movies'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(req,'testapp/news.html',my_dict)

def sport_info(req):
    head_msg='Sports Informaton'
    sub_msg1=' Football is the famous sport on the world'
    sub_msg2='Children everday must play sports '
    sub_msg3=' Dhoni is the best captian in ICC and IPL'
    type = 'sports'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(req,'testapp/news.html',my_dict)

def politics_info(req):
    head_msg='Movies Informaton'
    sub_msg1=' Day by Day politics has been increased '
    sub_msg2='Please vote before think '
    sub_msg3=' Loksatta is the best political party'
    type = 'politics'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(req,'testapp/news.html',my_dict)

