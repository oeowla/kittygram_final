from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cats.views import AchievementViewSet, CatViewSet
EOF

python -m isort --check-only --diff test_urls.py
