# Education YouTuber GPT

This project is to create a better way to find the answers you're looking for from specific youtubers. You select a channel from the dropdown and then ask the question you want. You will be presented with a plain text answer and a selection of related videos you can watch if you would like further information

Demo:
https://github.com/sa64r/education-youtuber-gpt/assets/64925510/f2b3d783-1c4e-48a8-946b-204fa3d15c14

### Setting up the environment:
1. Install `python 3.8.5`
2. Install `pip`
3. Install `virtualenv` by running:
```
pip install virtualenv
```

4. Create a virtual environment by running:
```
python3 -m venv env
```
5. Activate the virtual environment by running: 
```
source env/bin/activate
```
6. Install the dependencies by running: 
```
pip install -r requirements.txt
```
7. Copy the `.env.example` file to `.env` and fill in the appropriate values

8. To deactivate the virtual environment run:
```
deactivate
```

 
### To add a new youtube channel to the db do the following:
1. Assign the constants in `populate_db.py` to the appropriate values to `CHANNEL_ID` and `CHANNEL_NAME`
2. Navigate to the `backend` directory by running:
```
cd backend
```
3. Run: 
```
python populate_db.py
```

### To run the app:
1. Ensure all dependencies are installed by running:
```
pip install -r requirements.txt
```

2. In the root of the repository run:
```
streamlit run app.py
```
