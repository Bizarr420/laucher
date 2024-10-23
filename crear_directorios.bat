@echo off
setlocal

:: Define la ruta base donde se crearán los directorios
set "BASE_DIR=%USERPROFILE%\AppData\Roaming\.minecraftLauncher"

:: Crea el directorio .minecraftLauncher si no existe
if not exist "%BASE_DIR%" (
    mkdir "%BASE_DIR%"
    echo Directorio base creado: %BASE_DIR%
)

:: Crea subdirectorios solo si no existen
if not exist "%BASE_DIR%\mods" (
    mkdir "%BASE_DIR%\mods"
    echo Directorio mods creado: %BASE_DIR%\mods
)

if not exist "%BASE_DIR%\config" (
    mkdir "%BASE_DIR%\config"
    echo Directorio config creado: %BASE_DIR%\config
)

if not exist "%BASE_DIR%\saves" (
    mkdir "%BASE_DIR%\saves"
    echo Directorio saves creado: %BASE_DIR%\saves
)

if not exist "%BASE_DIR%\resourcepacks" (
    mkdir "%BASE_DIR%\resourcepacks"
    echo Directorio resourcepacks creado: %BASE_DIR%\resourcepacks
)

if not exist "%BASE_DIR%\versions" (
    mkdir "%BASE_DIR%\versions"
    echo Directorio versions creado: %BASE_DIR%\versions
)

if not exist "%BASE_DIR%\shaderpacks" (
    mkdir "%BASE_DIR%\shaderpacks"
    echo Directorio shaderpacks creado: %BASE_DIR%\shaderpacks
)

if not exist "%BASE_DIR%\logs" (
    mkdir "%BASE_DIR%\logs"
    echo Directorio logs creado: %BASE_DIR%\logs
)

if not exist "%BASE_DIR%\libraries" (
    mkdir "%BASE_DIR%\libraries"
    echo Directorio libraries creado: %BASE_DIR%\libraries
)

:: Fin del script
endlocal
pause
