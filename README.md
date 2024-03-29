# Education YouTuber GPT

[![Main](https://github.com/sa64r/education-youtuber-gpt/actions/workflows/main.yml/badge.svg)](https://github.com/sa64r/education-youtuber-gpt/actions/workflows/main.yml)

This project is to create a better way to find the answers you're looking for from specific youtubers. You select a channel from the dropdown and then ask the question you want. You will be presented with a plain text answer and a selection of related videos you can watch if you would like further information

Demo:

https://github.com/sa64r/education-youtuber-gpt/assets/64925510/8cb9711e-e32b-4b0c-910a-a61aba27f559

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
1. Assign the constants in `populate_db.py` to the appropriate values to `channel_id` and `channel_name` in `main()`
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

3. Enter your OpenAI API key where indicated
