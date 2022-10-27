#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plotter python ../../plotter.py
assert_in_stdout "Script is finished running"
assert_exit_code 0
