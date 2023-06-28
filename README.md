# [Web-ML Assistant (T4)]

You can go to:
<a href='https://webmlassistantteam2-production.up.railway.app/' target="_blank">LIVE Web-ML Assistant App</a>

# Stack of technologies used
<a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="30" height="30"/> </a>
<a href="https://keras.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/512px-Keras_logo.svg.png?20200317115153" alt="Keras" width="30" height="30"/> </a>
<a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" width="30" height="30"/> </a>
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30" height="30"/> </a> 
<a href="https://www.djangoproject.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-icon.svg" alt="django" width="30" height="30"/> </a> 
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="30" height="30"/> </a> 
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="30" height="30"/> </a>
<a href="https://www.w3schools.com/js/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/javascript/javascript-icon.svg" alt="js" width="30" height="30"/> </a>
<a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="postgresql" width="30" height="30"/> </a>
<a href="http://nginx.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="30" height="30"/> </a>
<a href="https://gunicorn.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="30" height="30"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="30" height="30"/> </a>
<a href="https://www.w3schools.io/terminal/bash-tutorials/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="30" height="30"/> </a>
<a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/linux/linux-icon.svg" alt="linux" width="30" height="30"/> </a>
<a href="https://getbootstrap.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-icon.svg" alt="linux" width="30" height="30"/> </a>

# About the project

- Main idea of the project: creating a personal Web-ML Assistant with useful modules (Computer Vision, NLP, CRUD)
- Deadline: MVP - 10 days, Prod - 2 days, presentation - 1 day
- Supported modules: Computer Vision (Image Classification, Object Detection, Depth Estimation, Semantic Segmentation), NLP (Image Funny Annotations, Personal Info Remover), authentication (AUTH functionality), contacts (CRUD, filter functionality for address book, validation), noteapp (CRUD, filter functionality for notes), news (news scraping module via spyder), storage (upload and download files to / from server, sorting by categories)
- Dataset based on [CIFAR10](https://www.kaggle.com/c/cifar-10/)
- Technical Requirements for Computer Vision module: implement a Web-service and create CNN capable of classifying an image given to it in one of the 10 classes.
- Techniques were used: transfer learning, fine tuning using EfficientNetV2 neural network, data augmentation, ReduceLROnPlateau, EarlyStopping, model compression (Quantization, Pruning)

# About the Image Classification App features

- Used Django web framework with the MVT architecture.
- Realised data filtering (io, os) and pre-processing (PIL) for uploaded images.
- App deals with different types exceptions.
- The App has a status bar for uploading or recognition process with evaluation of estimated time.
- Filtering non-CIFAR10 classes.
- Informative output with visualized probability style.
- Work with zero-background, 4K images.
- Included examples on main page for testing purposes.
- Supported AVIF format.

## About the Team

- [@Yurii Skiter](https://github.com/yuragoit) Team Lead, DevOps, MLOps, ML Engineer
- [@Dmytro Levoshko](https://github.com/DmytroLievoshko) Scrum Master, ML Engineer, Dev, QA
- [@Valerii Sydorenko](https://github.com/ErizoUA) Dev, ML Engineer, QA
- [@Serhii Korobchenko](https://github.com/serhii-korobchenko) Dev, ML Engineer, QA

## Start the app in Docker

> **Step 01** - Download the code from the GH-repository (using GIT) 

```bash
$ # Get the code
$ git clone https://github.com/yuragoit/webMLAssistantTeam2.git
$ cd webMLAssistantTeam2
```

> **Step 02** - Edit `.env` at `DB_*` settings (`DB_ENGINE=...`).

```txt
# Use True for development (switch to SQLite), False for production (switch to Postgres + Gunicorn + Nginx)
DEBUG=False

# Deployment SERVER address
DB_ENGINE=postgres          # Database Driver
DB_NAME=db                  # Database Name
DB_USERNAME=postgres        # Database User
DB_PASS=****************    # Strong Password 
DB_HOST=db                  # Database HOST, default is localhost 
DB_PORT=5432                # PostgreSQL port, default = 5432 

```

> **Step 03** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

> **Step 04** - Access the App

Visit `http://localhost:5085` in your browser. The app should be up and running

## Manual Build / Access

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/yuragoit/webMLAssistantTeam2.git
$ cd webMLAssistantTeam2
```

### Set Up for Unix, MacOS

> Install modules via venv  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Start the T4 App

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`

### Set Up for Windows

> Install modules via venv (Windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Start the T4 App

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`

## Create Users

By default, the T4 App redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the T4 App (see above)
- Access the `registration` page `http://127.0.0.1:8000/register/` and create a new User
- Access the `sign in` page `http://127.0.0.1:8000/login/` and authenticate

## Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # App that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some routes
   |    |    |-- *.py                      # All other py-files    
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- **************/                # Other target modules (contacts, noteapp, news, storage)
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS-files, JS-files
   |    |
   |    |-- templates/                     # Templates used to render target pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                  # Master pages
   |         |    |-- base-fullscreen.html # Used by Authentication pages
   |         |    |-- base.html            # Used by common pages
   |         |
   |         |-- accounts/                 # Authentication pages
   |         |    |-- login.html           # Login page
   |         |    |-- register.html        # Register page
   |         |
   |         |-- home/                     # UI Pages
   |              |-- index.html           # Index page
   |              |-- 403-page.html        # 403 page
   |              |-- 404-page.html        # 404 page
   |              |-- *.html               # All other pages
   |
   |-- requirements.txt                     # Development modules
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the T4 app - Django default start script
   |
   |-- ************************************************************************
```

## Screenshots

![ML_Classifier_PC](https://github.com/yuragoit/webMLAssistantTeam2/assets/101989870/8dbb4663-881b-47c8-b706-d0c9464e6d5c)
![ML_Detection](https://github.com/yuragoit/webMLAssistantTeam2/assets/101989870/d1b42735-58fa-4432-9af8-8adcbe1815c3)
![ML_Depth](https://github.com/yuragoit/webMLAssistantTeam2/assets/101989870/1a927e54-cc1c-4b08-b930-064307fd7522)
![ML_Semantic](https://github.com/yuragoit/AirbusShipDetection/assets/101989870/0dce0a55-72ef-4d6d-adb7-42b7da2894fa)
## License

[MIT](https://choosealicense.com/licenses/mit/)

## Used By

This project is used by the following companies:

- LLC GoIT School
