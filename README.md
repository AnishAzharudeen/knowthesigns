
# Project Name - Know the signs


here we neeed to add a description 
* [Link to Deployed Project](https://knowthe-signs-e02e6c0640d7.herokuapp.com/)

## CONTENTS
- [Project Name - Know the signs](#project-name---know-the-signs)
  - [CONTENTS](#contents)
  - [PROJECT DESIGN](#project-design)
    - [Wireframes](#wireframes)
    - [Logic](#logic)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Typography](#typography)
  - [Tech. stack](#tech-stack)
    - [Languages and frameworks](#languages-and-frameworks)
  - [Hosting platforms](#hosting-platforms)
  - [Packages](#packages)
    - [Tools and Libraries](#tools-and-libraries)
  - [DEPLOYMENT](#deployment)
    - [Deployment to Heroku involved the following steps and changes:](#deployment-to-heroku-involved-the-following-steps-and-changes)
  - [FORKING AND CLONING INSTRUCTIONS](#forking-and-cloning-instructions)
    - [Here's a step-by-step guide to forking:](#heres-a-step-by-step-guide-to-forking)
    - [Here's a step-by-step guide to cloning:](#heres-a-step-by-step-guide-to-cloning)
    - [Resources](#resources)
    - [Media](#media)
    - [Credits](#credits)
    - [Content References](#content-references)
      - [Copilot](#copilot)
      - [Educational sites](#educational-sites)
  - [Future features](#future-features)
  - [Acknowledgement](#acknowledgement)
  - [Credit](#credit)
    - [Images](#images)
  

## PROJECT DESIGN

  ### Wireframes

   The initial wireframes were created in [Miro](https://miro.com/es/) to understand how the site would work, and this layout would drive User Stories, the logic required and overall design artwork decisions.


<span style="justify-content:space-between; align-items:top;">
  <p>Desktop</p>
  <img src="./static/doc_images/wire_frame_desktop.png"/>

  </br>
    <p>Mobile</p>
  <img src="./static/doc_images/wire_frame_mobile.png"/>


</span>
    

  ### Logic
  The database schema and website logic was conceived and created using [Lucid](https://lucid.app/) as follows:

  Database Structure:


* [Back to Contents](#contents)

  ### Color Scheme
  The main colours of orange, dark blue and white were chosen for maximum contrast. I used [Coolors](https://coolors.co) to generate a colour palette.


  I used [Canva](https://www.canva.com/) to generate a logo and a style guide.


<span style="display:flex; gap:50px; text-align:center;">


    ![complete logo ](./static/images/logo2.png)



</span>

  * [Back to Contents](#contents)

  ### Imagery
  - I used FontAwesome https://fontawesome.com/ for various icons in the navbar, shopping bag, and other places for visual effects.

   <br>

  - I used [Pexels](https://www.pexels.com/es-es/) for free images .

  * [Back to Contents](#contents)

  ### Typography
   * I used a default Google font of Roboto and sans serif throughout the website for visual clarity and consistency.
   * And  Alfa+Slab+One&display font for the title of the home page 
   


## Tech. stack
The site has been built with the following tech, tools and libraries

### Languages and frameworks

* HTML5
* CSS3
* JavaScript
* JQuery
* Python
* Django
* Pillow - python image processing library
* Bootstrap 5 - frontend responsive styling framework

## Hosting platforms
* AWS - Host SQL database
* Cloudinary - Host images/videos
* Heroku - Host Django website
* Git - Host repository and project booard

## Packages
* Psycopg2 - postgreSQL adapter for python
* Gunicorn - WSGI HTTP server for UNIX
* Django AllAuth - user authentication
* Django crispy forms - Bootstrap form styling 


### Tools and Libraries
* GitHub Projects - agile management, kanban, roadmap and milestones
* GitHub Repo - code storage
* Git - version control
* GitPod & VS Code - IDE
* [Miro](https://balsamiq.com/) - creating wireframes
* [Coolors](https://coolors.co) - color pallette generator
* [Image resizer](https://www.reduceimages.com/) - resizing images for optimal storage
* [Canva](https://www.canva.com/) - creating artwork
* Google Fonts - consistent typography
* [Lucid Chart](https://lucid.app/) - creating a database schema
* [FontAwesome](https://fontawesome.com/) - icons
* [W3C HTML Validator](https://validator.w3.org/) - html code validation
* [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) - css code validation
* LightHouse - measures performance, accessibility, best practices and SEO
* Chrome Dev Tools - for development debugging
* [CI Python Linter](https://pep8ci.herokuapp.com/) - code analysis tool conforming to pep8
* Prettier - code formatter for html, css and javascript
* ESLint - code analysis tool for javascript


## DEPLOYMENT
  for a deployment, keep in mind that depending on the functionalities, some extra configuration may be missing. Very important is the configuration of variables in Heroku and the add-ons since without these activated you will not be able to see the project correctly

  Initially, Django was installed following this Code Institute [DRF Cheatsheet](https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn)

   1. Create a Cloudinary account and gather API key
   2. Create ElephantSQL database and gather API key
   3. Install Django
   4. Create project
   5. Install Cloudinary Storage
   6. Install Pillow (image processing)
   7. Update INSTALLED_APPs
       * all apps in the django project must be make migrations
       * python manage.py makemigrations
       * python manage.py migrate
       * to pass external data to the models if you need it.
          - create the fixture folder
          - add your file.json to the folder
          - python manage.py loaddata 'name.json' 
   8. Create env.py file
       * Add CLOUDINARY_KEY (from Cloudinary API key)
       * Add SECRET_KEY - (a unique password)
       * ADD DATABASE_URL - (postgres ElephantSQL API key)
       * STRIPE_SECRET_KEY 
       * STRIPE_PUBLIC_KEY 
       * DEBUG = True (if you have to push to heroku set False)
   9. Update settings.py
       * CLOUDINARY_STORAGE
       * Define Media Storage URL
       * Set DEFAULT_FILE_STORAGE
       * Set DATABASES
       * set STRIPE settings
    

  ### Deployment to Heroku involved the following steps and changes:
   1. Install gunicorn and psycopg2 then freeze requirements to requirements.txt.
   2. Create a Procfile (web: gunicorn core.wsgi:application).
   3. Log into your Heroku account, create a new app, and access the dashboard for your application.
   4. Go to Settings and open the Config Vars add all the Api keys in your env.py
       * Add CLOUDINARY_KEY (the Cloudinary API key)
       * Add SECRET_KEY - (the unique password)
       * Add STRIPE_SECRET_KEY - (stripe payments Api key)
       * AWS_DB_NAME - AWS database name
       * AWS_HOST - AWS url
       * AWS_PASSWORD
       * AWS_USER
       * DEVELOPMENT - Set to "False", to use AWS instead of local database
       * SECRET_KEY - Contains your Django secret key for encryption
   5. Ensure your application has an ALLOWED_HOST your '.herokuapp.com'
   6.  Ensure in Resources in heroku dasboard change your dinos active.
   7.  Go to the Deploy tab, connect the project to GitHub, and choose main branch to deploy
       * Click Deploy Branch (manually)
       * (Optional) Select Enable Automatic Deploys


* [Back to Contents](#contents)


## FORKING AND CLONING INSTRUCTIONS
You can create a copy of a GitHub Repository without affecting the original by forking or cloning it.

### Here's a step-by-step guide to forking:
Forking is often used for proposing changes or using the project as a starting point for your own idea. Forking will apear on your GitHub profile.
1. Log into GitHub or sign up for an account.
2. Go to the [Iron Haven Fitness Repository](https://github.com/richard9106/Project-5)
3. Click "Fork" on the right side of the repository's page to create a copy in your own repository.

### Here's a step-by-step guide to cloning:
Cloning is often used for experimenting locally.  It will not show up on your GitHub profile.
1. Go to the [Iron Haven Fitness Repository](https://github.com/richard9106/Project-5)
2. Click the green code button, then the arrow, and select the "clone by https" option to copy the URL.
3. Open your preferred code editor and navigate to the directory where you want to clone the repository.
4. Type 'git clone', paste the copied URL, and press enter. The repository will then be cloned to your machine.

* [Back to Contents](#contents)


 ### Resources
  I used the following resources to help develop features and functionality:
 
  * ChatGPT was used to help troubleshoot and explain code functions
  * Google and StackOverflow were also used for more context and understanding
  * I reached out to Code Institute team members and tutor support from time to time


  * [Back to Contents](#contents)



  ### Media
  * The Iron Haven Fitness logo was custom-designed for this project.
  * Logo icon created in Canva Pro.
  * images from pexel
  * Icons - font awesome.

  * [Back to Contents](#contents)

  ### Credits

### Content References

#### Copilot

- We have utilized GitHub Copilot to assist in generating content for the website.

#### Educational sites
 


## Future features

We have several exciting features planned for future development to enhance this website

- **Feedback to improve**: Implement a system where reporters receive regular feedback on their issue's progress. This will help reports  stay informed.



These future features aim to create a more comprehensive and interactive learning environment, supporting the educational growth of children while keeping parents and teachers actively involved.

## Acknowledgement
 
- We would like to extend our heartfelt thanks to **Code Institute** for providing this incredible platform and the opportunity to develop "Know the signs."

- Special thanks to the instructors and mentors - ****, ****, and **** for their invaluable guidance and support throughout the process.

## Credit

### Images

* [Right story carousel arrow](https://www.svgrepo.com/svg/334215/right-arrow)
* [Left story carousel arrow](https://www.svgrepo.com/svg/334036/left-arrow)
=======
- We would also like to express our gratitude to our amazing team for their hard work, dedication, and collaboration in bringing "Know the signs" to life.

