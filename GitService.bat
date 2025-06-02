@echo off
title Git Auto-Commit Utility
color 0A
echo [Запуск] Git Auto-Commit приложения...
echo.
:: Автоматическое определение пути к BAT-файлу
set BAT_DIR=%~dp0
echo Расположение bat-файла: %BAT_DIR%

:: Поиск EXE в той же папке (имя должно совпадать с названием bat-файла)
set EXE_NAME=%~n0.exe
set APP_PATH=%BAT_DIR%%EXE_NAME%

:: Проверка существования EXE
if not exist "%APP_PATH%" (
    echo [ОШИБКА] Не найден файл: %EXE_NAME%
    echo Ищем в: %APP_PATH%
)
echo Найдено приложение: %APP_PATH%
echo.
:: Запуск приложения (без указания репозитория - будет автоопределение)
call "%APP_PATH%"