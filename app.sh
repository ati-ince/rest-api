cd rest-api
git fetch
git pull
if [ -d "__pycache__" ]
then
    rm -R /__pycache__ 
fi
python3 ./database.py
