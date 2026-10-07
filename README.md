<div align="center">

# SONU.KR | Personal Portfolio

**A modern, responsive portfolio website built with Flask, HTML, CSS and JavaScript.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-ff4d1f?style=for-the-badge&logo=render&logoColor=white)](https://sonu-portfolio-vefb.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

[View Live Site](https://sonu-portfolio-vefb.onrender.com/) · [LinkedIn](https://www.linkedin.com/in/sonu-kumar-ray-3b36b0380/) · [GitHub](https://github.com/sonu3012)

</div>

---

## About

This is the personal portfolio of **Sonu Kumar Ray**, a B.Tech graduate in Artificial Intelligence & Data Science. It presents my skills, projects, internships and certifications in one place, with a bold orange, dark and white design.

## Features

- Animated loader, typing role effect and smooth scroll animations
- Orange hero section with wavy section dividers
- Skills, featured projects (with GitHub and live demo links), experience timeline, education and certifications
- Download Resume button and a link to all certificates
- Contact section with a working message form
- Fully responsive on mobile, tablet and desktop
- All content stored in one file (`data.py`), so it is easy to update

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Templating | Jinja2 |
| Server | Gunicorn |
| Hosting | Render |

## Project Structure

```
sonu-portfolio/
├── app.py                  # Flask app and routes
├── data.py                 # All portfolio content (edit this)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Main page template
└── static/
    ├── css/style.css       # Styling
    ├── js/main.js          # Animations and form logic
    ├── img/profile.png     # Profile photo
    └── Sonu_Kumar_Ray_Resume.pdf
```

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/sonu3012/sonu-portfolio.git
cd sonu-portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Customise

| What | Where |
|---|---|
| Name, about, links, skills, projects, experience, certifications | `data.py` |
| Profile photo (transparent PNG works best) | `static/img/profile.png` |
| Resume PDF | `static/`, with the file name set in `data.py` |
| Colours, fonts, layout | `static/css/style.css` |

## Deployment

The site is deployed on **Render**.

| Setting | Value |
|---|---|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

Every `git push` to the `main` branch redeploys the site automatically.

## Contact

- **Email:** sonukroy897@gmail.com
- **LinkedIn:** [sonu-kumar-ray](https://www.linkedin.com/in/sonu-kumar-ray-3b36b0380/)
- **GitHub:** [sonu3012](https://github.com/sonu3012)

---

<div align="center">

If you like this project, please give it a star on GitHub.

Built by **Sonu Kumar Ray**

</div>

