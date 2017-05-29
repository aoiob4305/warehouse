#-*- coding:utf-8 -*-

from django import forms

class searchForm(forms.Form):
    TYPE_LIST = (('no', '품번'),('name', '품명'),('description', '내역'),)
    PLANT_LIST = (('1100', '1공장'),('1700','DCT'))
    query_plant = forms.ChoiceField(label='플랜트', choices=PLANT_LIST)
    query_type = forms.ChoiceField(label='타입', choices=TYPE_LIST)
    query_text = forms.CharField(label='검색어', max_length=20)

class updateForm(forms.Form):
    filename = forms.CharField(label='파일명', max_length=20)

class uploadFileForm(forms.Form):
    file = forms.FileField()
