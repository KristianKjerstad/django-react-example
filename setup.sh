#!/bin/bash
echo "installing python dependencies"
pip install -r backend/requirements.txt

echo "install frontend dependencies"
cd frontend && npm install
cd ..
