#!/usr/bin/bash

TEST_SERVER=QA

GENERATOR_ALLURE=.\\Executer\\allure_generator.sh
PYTEST_LOG=.\\Results\\pytest.log

# Running PyTest
echo "EXECUTER: PyTest Execution Started..."
echo "EXECUTER: PyTest Execution Log -> $PYTEST_LOG"
TEST_SERVER=$TEST_SERVER pytest > $PYTEST_LOG
grep 'ERROR' $PYTEST_LOG
STATUS=$?

# Removing Junk Files after PyTest
echo "EXECUTER: Removing Junk Files after PyTest..."
rm -rf .pytest_cache
rm -rf .\\Resource\\__pycache__
rm -rf .\\Resource\\Pages\\__pycache__
rm -rf .\\Resource\\Common\\__pycache__
rm -rf .\\Tests\\__pycache__

if [ $STATUS == 1 ]; then
    echo "EXECUTER: Generating Allure report..."
    $GENERATOR_ALLURE
else
    echo "EXECUTER: ERROR Detected! Skipping Allure report generation..."
    echo "EXECUTER: Press any key to Exit..."
    read
fi
