from typing import List, Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Datatable
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib
import base64
from .forms import DateForm, FieldForm, PeriodForm
from django.contrib.auth.models import User
import datetime


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'
    login_url = '/crudapp/'  # проверка на автоматизацию полизователя
    redirect_field_name = 'redirect_to'  # проверка на автоматизацию

    # полизователя

    def get_queryset(self):
        return Datatable.objects.all()


def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(Datatable, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object': contact})


@login_required  # аннатация для отрытия только через логин
def dashboard(request):
    return render(request, 'crudapp/dashboard.html', {'section': 'dashboard'})


class AdminLogin(LoginView):
    template_name = 'crudapp/registration/login.html'


class AdminLogout(LogoutView):
    template_name = 'crudapp/registration/logged_out.html'


def import_data(request):  # добовление данных в базу из фаила Excel
    if request.POST:
        file = request.FILES['files']  # Загрузка файлов
        book = pd.read_excel(file, sheet_name='Sheet1')  # обрободка фаила
        bookDic = book.to_dict('records')  # переоброзование в фаил Json
        for i in bookDic:  # обрободка фаила в цыкле
            obj = Datatable(
                cell_5=i[''],
                cell_6=i[''],
                cell_7=i[''],
                cell_8=i[''],
                cell_9=i[''],
                cell_10=i[''],
                cell_11=i[''],
                cell_12=i[''],
                cell_13=i[''],
                cell_14=i[''],
                cell_15=i[''],
                cell_16=i[''],
                cell_17=i[''],
                cell_18=i[''],
                cell_19=i[''],
                cell_20=i[''],
                cell_21=i[''],
                cell_22=i[''],
                cell_23=i[''],
                cell_24=i[''],
                cell_25=i[''],
                cell_26=i[''],
                cell_27=i[''],
                cell_28=i[''],
                cell_29=i[''],
                cell_30=i[''],
                cell_31=i[''],
                cell_32=i[''],
                cell_33=i[''],
                cell_34=i[''],
                cell_35=i[''],
                cell_36=i[''],
                cell_37=i[''],
                cell_38=i[''],
                cell_39=i[''],
                cell_40=i[''],
                cell_41=i[''],
                cell_42=i[''],
                cell_43=i[''],
                cell_44=i[''],
            )
            obj.save()  # Сохронение данных в базу
        if file:
            messages.success(request, 'Файл успешно загружен')
        else:
            messages.error(request, 'Ошибка при загрузке файла')
        return redirect('index')  # возврат на главную страницу
    return render(request, 'crudapp/index.html')  # отрисовка


def edit(request):  # добовление данных в базу
    if request.POST:
        db = Datatable(
            cell_5=request.POST.get('cell_5'),
            cell_6=request.POST.get('cell_6'),
            cell_7=request.POST.get('cell_7'),
            cell_8=request.POST.get('cell_8'),
            cell_9=request.POST.get('cell_9'),
            cell_10=request.POST.get('cell_10'),
            cell_11=request.POST.get('cell_11'),
            cell_12=request.POST.get('cell_12'),
            cell_13=request.POST.get('cell_13'),
            cell_14=request.POST.get('cell_14'),
            cell_15=request.POST.get('cell_15'),
            cell_16=request.POST.get('cell_16'),
            cell_17=request.POST.get('cell_17'),
            cell_18=request.POST.get('cell_18'),
            cell_19=request.POST.get('cell_19'),
            cell_20=request.POST.get('cell_20'),
            cell_21=request.POST.get('cell_21'),
            cell_22=request.POST.get('cell_22'),
            cell_23=request.POST.get('cell_23'),
            cell_24=request.POST.get('cell_24'),
            cell_25=request.POST.get('cell_25'),
            cell_26=request.POST.get('cell_26'),
            cell_27=request.POST.get('cell_27'),
            cell_28=request.POST.get('cell_28'),
            cell_29=request.POST.get('cell_29'),
            cell_30=request.POST.get('cell_30'),
            cell_31=request.POST.get('cell_31'),
            cell_32=request.POST.get('cell_32'),
            cell_33=request.POST.get('cell_33'),
            cell_34=request.POST.get('cell_34'),
            cell_35=request.POST.get('cell_35'),
            cell_36=request.POST.get('cell_36'),
            cell_37=request.POST.get('cell_37'),
            cell_38=request.POST.get('cell_38'),
            cell_39=request.POST.get('cell_39'),
            cell_40=request.POST.get('cell_40'),
            cell_41=request.POST.get('cell_41'),
            cell_42=request.POST.get('cell_42'),
            cell_43=request.POST.get('cell_43'),
            cell_44=request.POST.get('cell_44'),
        )  # обрободка данных с клиента
        db.cell_47 = request.user
        db.save()  # Сохронение данных в базу
        if db:
            messages.success(request, 'Данные успешно отправлены')
        else:
            messages.error(request, 'Ошибка при отправлении данных')
        return redirect('index')  # возврат на главную страницу
    return render(request, 'crudapp/index.html')  # отрисовка


def get(request, template_name='crudapp/testing_orm.html'):
    all_data = Datatable.objects.all()
    hosp_id = request.user.id
    users = User.objects.filter(first_name__exact='ЗВО')
    filtered_data = Datatable.objects.filter(cell_47_id__exact=hosp_id)
    filtered_date_data = Datatable.objects.filter(cell_47_id__exact=hosp_id, cell_46__exact=datetime.date.today())
    context = {
        'all_data': all_data,
        'id': hosp_id,
        'filtered': filtered_data,
        'filtered_date': filtered_date_data,
        'users': users,
    }

    return render(request, template_name, context)


def test_matplotlib(request):
    # взято отсюда https://medium.com/@mdhv.kothari99/matplotlib-into-django-template-5def2e159997 и
    # https://devpractice.ru/matplotlib-lessons/

    x = []
    for i in range(0, 31):
        x.append(i + 1)

    y = [4, 6, 2, 12, 0, 3, 5, 3, 8, 1, 8, 3, 7, 4, 0,
         0, 4, 5, 8, 6, 1, 4, 6, 4, 7, 1, 8, 3, 9, 4, 6]
    # plt.plot(range(10))
    plt.grid()  # сетка графика
    plt.plot(x, y, 'o-r', label='Значения за месяц')  # построение графика
    plt.legend()  # легенда графика
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context = {
        'data': uri,
    }
    return render(request, 'crudapp/pandas_test.html', context)


def test_table(request):
    hosp_id = request.user.id
    filtered_data = None

    context = {
    }

    form = DateForm
    context['form'] = form

    if request.POST:
        print(request.POST)
        temp = request.POST.get('date_form_sort')
        print(temp)

        if temp == '1':
            filtered_data = Datatable.objects.filter(cell_47_id__exact=hosp_id).order_by(
                "-cell_46")  # сначала новые (по убыванию)
        elif temp == '2':
            filtered_data = Datatable.objects.filter(cell_47_id__exact=hosp_id).order_by(
                "cell_46")  # сначала старые (по возрастанию)

    context['filtered_data'] = filtered_data

    return render(request, 'crudapp/test_table.html', context)


def test_table_admin(request):
    filtered_data = None
    cell_date = 'cell_46'
    cell_fields = 'cell_45'

    context = {
    }

    formfield = FieldForm
    context['formfield'] = formfield

    formdate = DateForm
    context['formdate'] = formdate

    if request.POST:

        # temp_date = request.GET['date_form_sort']
        #
        # if temp_date == '1':
        #     cell_date = "-cell_46"
        # elif temp_date == '2':
        #     cell_date = "cell_46"

        temp_fields = request.POST['field_form_sort']

        if temp_fields == '1':
            cell_fields = "cell_46"
        elif temp_fields == '2':
            cell_fields = "cell_48"
        elif temp_fields == '3':
            cell_fields = "cell_45"
        elif temp_fields == '4':
            cell_fields = "cell_5"
        elif temp_fields == '5':
            cell_fields = "cell_6"
        elif temp_fields == '6':
            cell_fields = "cell_7"
        elif temp_fields == '7':
            cell_fields = "cell_8"
        elif temp_fields == '8':
            cell_fields = "cell_9"
        elif temp_fields == '9':
            cell_fields = "cell_10"
        elif temp_fields == '10':
            cell_fields = "cell_11"
        elif temp_fields == '11':
            cell_fields = "cell_12"
        elif temp_fields == '12':
            cell_fields = "cell_13"
        elif temp_fields == '13':
            cell_fields = "cell_14"
        elif temp_fields == '14':
            cell_fields = "cell_15"
        elif temp_fields == '15':
            cell_fields = "cell_16"
        elif temp_fields == '16':
            cell_fields = "cell_17"
        elif temp_fields == '17':
            cell_fields = "cell_18"
        elif temp_fields == '18':
            cell_fields = "cell_19"
        elif temp_fields == '19':
            cell_fields = "cell_20"
        elif temp_fields == '20':
            cell_fields = "cell_21"
        elif temp_fields == '21':
            cell_fields = "cell_22"
        elif temp_fields == '22':
            cell_fields = "cell_23"
        elif temp_fields == '23':
            cell_fields = "cell_24"
        elif temp_fields == '24':
            cell_fields = "cell_25"
        elif temp_fields == '25':
            cell_fields = "cell_26"
        elif temp_fields == '26':
            cell_fields = "cell_27"
        elif temp_fields == '27':
            cell_fields = "cell_28"
        elif temp_fields == '28':
            cell_fields = "cell_29"
        elif temp_fields == '29':
            cell_fields = "cell_30"
        elif temp_fields == '30':
            cell_fields = "cell_31"
        elif temp_fields == '31':
            cell_fields = "cell_32"
        elif temp_fields == '32':
            cell_fields = "cell_33"
        elif temp_fields == '33':
            cell_fields = "cell_34"
        elif temp_fields == '34':
            cell_fields = "cell_35"
        elif temp_fields == '35':
            cell_fields = "cell_36"
        elif temp_fields == '36':
            cell_fields = "cell_37"
        elif temp_fields == '37':
            cell_fields = "cell_38"
        elif temp_fields == '38':
            cell_fields = "cell_39"
        elif temp_fields == '39':
            cell_fields = "cell_40"
        elif temp_fields == '40':
            cell_fields = "cell_41"
        elif temp_fields == '41':
            cell_fields = "cell_42"
        elif temp_fields == '42':
            cell_fields = "cell_43"
        elif temp_fields == '43':
            cell_fields = "cell_44"

    startdate = request.POST.get("start")
    enddate = request.POST.get("end")
    print(startdate)
    print(enddate)
    print(request.POST)

    filtered_data = Datatable.objects.filter(cell_46__range=(startdate, enddate)).order_by(cell_fields)
    print(filtered_data)
    context['filtered_data'] = filtered_data

    return render(request, 'crudapp/test_table_admin.html', context)


def drawchart(datalist_a, datalist_b, days):
    days_list = []
    for i in range(days):
        days_list.append(i + 1)

    plt.grid()  # сетка графика
    plt.plot(days_list, datalist_a, lw=1, ls='-', marker='o', markersize=2, label='Занятые койки', color='r')  # построение графика
    plt.plot(days_list, datalist_b, lw=1, ls='-', marker='o', markersize=2, label='Свободные койки', color='g')  # построение графика
    plt.xlabel('Дни')
    plt.ylabel('Количество')
    plt.title('График занятых и свободных коек за период')
    plt.legend()  # легенда графика
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()
    return uri


def drawpie(values, names, title):
    all_values = 0

    for i in values:
        all_values += i

    per = []
    for i in values:
        per.append(i / all_values * 100)
        # try:
        #     per.append(i / all_values * 100)
        # except ZeroDivisionError:
        #     per.append(0)

    labels = []

    for i in range(len(values)):
        temp_per = "%.2f" % per[i]
        labels.append(f"{names[i]} - {str(values[i])} ({str(temp_per)}%)")

    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    plt.pie(values, labels=labels, colors=colors)
    plt.axis('equal')
    plt.title(title)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()
    return uri


def analytics(request):
    startdate_str = None
    enddate_str = None

    startdate_str = request.POST.get("start")  # первый datepicker
    enddate_str = request.POST.get("end")  # второй datepicker

    if startdate_str is None:
        startdate_str = datetime.date(2022, 1, 1)
        enddate_str = datetime.date(2022, 1, 31)

    startdate = datetime.datetime.strptime(str(startdate_str), "%Y-%m-%d")  # из string в datetime
    enddate = datetime.datetime.strptime(str(enddate_str), "%Y-%m-%d")

    days = (enddate - startdate).days + 1  # количество дней в рассматриваемом промежутке

    globalQueryset = Datatable.objects.filter(cell_46__range=(startdate, enddate - datetime.timedelta(days=1))).values()  # значения queryset по отрезку времени

    list_days_ill = []  # список для подсчёта занятых коек по датам
    list_days_free = []  # список для подсчёта свободных коек по датам

    for i in range(days):  # заполнение списков нулями, чтобы в пустые дни не было дропов
        list_days_ill.append(0)
        list_days_free.append(0)

    for i in globalQueryset:  # заполнение списков значениями из значений queryset
        list_days_ill[i['cell_46'].day - days] += i['cell_7']
        list_days_free[i['cell_46'].day - days] += i['cell_5']

    # print('list_days_ill')
    # for i in list_days_ill:
    #     print(i)
    #
    # print('list_days_free')
    # for i in list_days_free:
    #     print(i)

    ill_for_chart_value = []  # занятые койки из period
    free_doss_for_chart_value = []  # свободные койки из period
    covid_for_chart_value = []  # заболевшие covid-19 из period
    other_for_chart_value = []  # другие заболевания из period

    for i in globalQueryset:
        ill_for_chart_value.append(i['cell_7'])
        free_doss_for_chart_value.append(i['cell_5'] - i['cell_7'])
        covid_for_chart_value.append(i['cell_8'])
        other_for_chart_value.append(i['cell_7'] - i['cell_8'])

    covid_for_chart_value_sum = 0  # сумма заболевших covid-19 из period
    other_for_chart_value_sum = 0  # сумма других заболеваний из period
    free_doss_for_chart_value_sum = 0  # сумма свободных коек из period

    for i in covid_for_chart_value:
        covid_for_chart_value_sum += i

    for i in other_for_chart_value:
        other_for_chart_value_sum += i

    for i in other_for_chart_value:
        free_doss_for_chart_value_sum += i

    names_reasons = ["COVID-19", "Другие причины"]  # список для вывода лейблов диаграммы на экран
    names_mil_districts = ["ЦП", "ЗВО", "ЮВО", "ЦВО", "ВВО", "СФ"]
    values_reasons = [covid_for_chart_value_sum, other_for_chart_value_sum]  # данные для отрисовки диаграммы о причинах

    ill_table_values = {}  # словарь из queryset'ов
    ill_for_screen_districts = []  # список больных по округам солгасно списку names_reasons
    ill_for_screen_all = 0  # сумма всех больных за период для вывода сверху справа
    ill_for_districts_pies = {}  # словарь для подсчёта больных covid-19 по округам
    other_for_districts_pies = {}  # словарь для подсчёта больных не covid-19 по округам
    list_for_districts_pies = []

    for i in names_mil_districts:
        temp = globalQueryset.filter(cell_48__exact=i)
        ill_for_districts_pies[i] = 0
        other_for_districts_pies[i] = 0
        for j in temp:
            ill_for_districts_pies[i] += int(j['cell_8'])
            other_for_districts_pies[i] += int(j['cell_7']) - int(j['cell_8'])
        list_for_districts_pies.append([ill_for_districts_pies[i], other_for_districts_pies[i]])

    for i in names_mil_districts:
        ill_table_values[i] = globalQueryset.filter(cell_48__exact=i)
        # получение словаря (распарсенного queryset) из queryset всех записей по округам за период

        sum = 0

        for j in ill_table_values[i]:  # суммирование всех занятых коек (cell_7) по округам за период
            sum += int(j['cell_7'])

        ill_for_screen_districts.append(sum)
        ill_for_screen_all += sum  # суммирование данных данных за округа в данные за все округа

    try:
        chart = drawchart(list_days_ill, list_days_free, days)  # основной график
        pie_reasons = drawpie(values_reasons, names_reasons, 'Причины заболевания по всем округам')  # круговая диаграмма о причинах заболеваний
        pie_mil_districts = drawpie(ill_for_screen_districts, names_mil_districts, 'Количество заболевших по округам')  # круговая диаграмма о заболеваниях в округах
        pie_cp = drawpie(list_for_districts_pies[0], names_reasons, 'Причины болевания в госпиталях ЦП')
        pie_west = drawpie(list_for_districts_pies[1], names_reasons, 'Причины болевания в госпиталях ЗВО')
        pie_south = drawpie(list_for_districts_pies[2], names_reasons, 'Причины болевания в госпиталях ЮВО')
        pie_center = drawpie(list_for_districts_pies[3], names_reasons, 'Причины болевания в госпиталях ЦВО')
        pie_east = drawpie(list_for_districts_pies[4], names_reasons, 'Причины болевания в госпиталях ВВО')
        pie_north = drawpie(list_for_districts_pies[5], names_reasons, 'Причины болевания в госпиталях СФ')
    except ZeroDivisionError:
        return render(request, "crudapp/errorpage.html")
    except ValueError:
        return render(request, "crudapp/errorpage.html")

    context = {
        'chart': chart,
        'pie_reasons': pie_reasons,
        'pie_mil_districts': pie_mil_districts,
        'ill_for_screen_all': ill_for_screen_all,
        'free_doss_for_chart_value_sum': free_doss_for_chart_value_sum,
        'pie_west': pie_west,
        'pie_cp': pie_cp,
        'pie_south': pie_south,
        'pie_center': pie_center,
        'pie_east': pie_east,
        'pie_north': pie_north,
    }

    return render(request, "crudapp/analytics.html", context)
