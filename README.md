# SONU.KR Portfolio (Flask)

## Run
    pip install -r requirements.txt
    python app.py          # open http://127.0.0.1:5000

## Customise
- All text lives in `data.py` (skills, projects, experience, certifications). Lines marked `TODO` need your real details.
- Photo: save a transparent PNG cutout as `static/img/profile.png` (the hero and ID card pick it up automatically).
- Resume: put your PDF in `static/` named `Sonu_Kumar_Ray_Resume.pdf`.
- Contact form messages are saved to `messages.jsonl`.

## Deploy (Render / Railway)
Start command: `gunicorn app:app`
