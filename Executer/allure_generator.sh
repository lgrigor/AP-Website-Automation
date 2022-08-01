#!/usr/bin/bash

ALLURE_RESULT=.\\Results\\allure_results
ALLURE_REPORT_DIR=.\\Results\\allure-report
ALLURE_REPORT_HISTORY=$ALLURE_REPORT_DIR\\history
ALLURE_RESULT_HISTORY=$ALLURE_RESULT\\history

if [ -d "$ALLURE_REPORT_HISTORY" ]; then
    if [ -d "$ALLURE_RESULT_HISTORY" ]; then
        echo "ALLURE GEN: rm-ing old result history!"
        rm -rf $ALLURE_RESULT_HISTORY
    fi
    echo "ALLURE GEN: mv-ing new result history before generation!"
    mv -f $ALLURE_REPORT_HISTORY $ALLURE_RESULT
fi

allure generate $ALLURE_RESULT --clean -o $ALLURE_REPORT_DIR
allure open $ALLURE_REPORT_DIR