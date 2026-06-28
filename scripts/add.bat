@echo off
setlocal enabledelayedexpansion

set CONFIG_FILE=sources.txt

if not exist "%CONFIG_FILE%" (
    echo Configuration file not found: %CONFIG_FILE%
    exit /b 1
)

for /f "usebackq tokens=1-5 delims=|" %%a in ("%CONFIG_FILE%") do (

    if not "%%a"=="" (
        if not "%%a:~0,1%%"=="#" (
            set NAME=%%a
            set REPO=%%b
            set REF=%%c
            set SPARSE_PATH=%%d
            set MODE=%%e

            echo ----------------------------------------
            echo Repository : !NAME!
            echo Reference  : !REF!
            echo Path       : !SPARSE_PATH!
            echo Mode       : !MODE!
            echo ----------------------------------------

            if not exist "!NAME!" (
                echo Cloning repository...

                git clone ^
                    --depth=1 ^
                    --filter=blob:none ^
                    --sparse ^
                    --branch=!REF! ^
                    !REPO! ^
                    !NAME!

                pushd !NAME!

                echo Configuring sparse checkout...
                git sparse-checkout set !SPARSE_PATH!

                if /I "!MODE!"=="archive" (
                    echo Removing Git metadata...
                    rmdir /s /q .git
                )

                popd

                echo Completed.
            ) else (
                if /I "!MODE!"=="archive" (
                    echo Archive already exists.
                    echo Delete the directory manually if you want to re-sync.

                ) else (
                    if exist "!NAME!\.git" (
                        echo Updating repository...

                        pushd !NAME!

                        git fetch --depth=1 origin !REF!
                        git checkout !REF!
                        git sparse-checkout set !SPARSE_PATH!

                        git pull origin !REF!

                        popd

                        echo Completed.
                    ) else (
                        echo Directory exists but is not a Git repository.
                        echo Skipping.
                    )
                )
            )

            echo.
        )
    )
)

echo Synchronization completed.
