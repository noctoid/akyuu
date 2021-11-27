#!/bin/bash

VENV_DIR=venv/bin/activate

source $VENV_DIR
uvicorn akyuu.main:app --reload
