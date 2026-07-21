# پروژه WOOX 🚀

این یک پروژه تحت وب است که با فریم‌ورک **Django** ساخته شده است.

## 🛠️ تکنولوژی‌های استفاده شده
- **Backend:** پایتون (Python) و جنگو (Django)
- **پایگاه داده:** SQLite3 (پیش‌فرض)
- **کنترل نسخه:** گیت (Git)

## ⚙️ راهنمای نصب و راه‌اندازی

برای اجرای پروژه روی سیستم خودتان، مراحل زیر را دنبال کنید:

### ۱. دریافت پروژه
اگر پروژه را از گیت کلون کرده‌اید، وارد پوشه اصلی شوید:
```bash
cd WOOX/woox
```
### ۲. ساخت محیط مجازی (Virtual Environment)
برای ایجاد یک محیط ایزوله جهت نصب پکیج‌ها:
```bash
python -m venv venv
```
### ۳. فعال‌سازی محیط مجازی
برای ورود به محیط مجازی ساخته شده:
```bash
source venv/Scripts/activate
```
### ۴. نصب پیش‌نیازها
نصب فریم‌ورک جنگو و وابستگی‌های آن:
```bash
pip install django
```
### ۵. اجرای سرور
راه‌اندازی سرور توسعه‌ی جنگو:

```bash
python manage.py runserver
```

# ادامه کار در محیط ادیتور
Log in to VS Code and continue working there.
```bash
code .
```
### اجرای سرور

فعال‌سازی محیط مجازی
```bash
source ../venv/Scripts/activate

راه‌اندازی سرور توسعه‌ی جنگو:
python manage.py runserver

ساخت اولین اپ در پروژه
ls
python manage.py startapp main
settings.py
add new app in settings.py
add new sqlite in settings.py
add urls.py in new app main
```
---
### urls.py project
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
]
```
### urls.py app project(main)
```
from django.urls import path
from .views import index

urlpatterns = [
    path('',index,name="home"),
]
```
### views.py project
```from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hallo World Woox</h1>")
```


