#!/bin/bash

# Запуск приложения
uvicorn --factory application.api.main:create_app --reload --host 0.0.0.0 --port 8000
