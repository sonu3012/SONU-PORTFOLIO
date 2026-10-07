"""
All portfolio content lives here. Edit this file only; the page updates itself.
Anything marked  # TODO  is a placeholder for you to confirm from your resume.
"""

PROFILE = {
    "brand": "SONU KUMAR RAY",
    "name": "Sonu Kumar Ray",
    "first_name": "Sonu",
    "roles": ["AI & Data Science Developer", "Python Developer", "AI Agent Builder", "ML Enthusiast"],
    "tagline": (
        "I build AI agents, data-driven apps and clean web experiences "
        "using Python, Flask and modern LLM APIs."
    ),
    "about": [
        "I'm Sonu Kumar Ray, a B.Tech graduate in Artificial Intelligence & Data Science "
        "who loves turning data and real-world problems into practical AI applications.",
        "I work with Python, SQL, Machine Learning, NLP, LLMs, Generative AI and Agentic AI, "
        "and I've built a Real Estate AI Calling Agent, AI Order Tracking & Customer Support Agent and a "
        "Movie Recommendation System.",
        "I'm looking for opportunities where I can solve meaningful problems with modern "
        "technology and grow as an AI & Data professional.",
        "I like projects where AI solves a real business problem, and I care about clean code, "
        "simple UX and shipping things that actually run.",
    ],
    "location": "Delhi NCR,India",
    "email": "sonukroy897@gmail.com",
    "github": "https://github.com/sonu3012",
    "linkedin": "https://www.linkedin.com/in/sonu-kumar-ray-3b36b0380/",
    "certificates_link": "https://drive.google.com/drive/folders/1ygF7BFqKR2Eit_HLNhM9MqmsfcysI5a4",
    "resume_file": "Sonu_Kumar_Ray_Resume oct.pdf",  # put your PDF in static/ with this exact name
    "open_to": "Open to AI & ML / Data Science & Analytics roles, including india & abroad. Willing to relocate.",
}

STATS = [
    {"value": "8.0", "label": "CGPA"},
    {"value": "3", "label": "Internships"},
    {"value": "5", "label": "Projects"},
]

SKILLS = [
    {
        "title": "Programming & Scripting",
        "icon": "💻",
        "items": ["Python", " C++", "SQL"],
    },
    {
        "title": "AI & ML",
        "icon": "🧠",
        "items": ["AI Automation", "GEN AI & AGENTIC AI", "AI Agents & Tool Calling", "LLMs integration", "Prompt Design" ""],
    },
    {
        "title": "Data Science & Analytics",
        "icon": "📊",
        "items": ["Exploratory Data Analysis (EDA)","Feature Engineering", "Machine Learning", "Recommendation Systems", "Data Analysis", "Business Intelligence"],
    },
    {
        "title": "Database & Backend",
        "icon": "⚙️",
        "items": [" MYSQL","SQLite", "Flask", "FastAPI", "REST APIs"],
    },
    {
        "title": "Data visualization & Frontend",
        "icon": "🎨",
        "items": ["HTML5", "CSS3", "Next.js", "Streamlit", "Tableau", "Power BI","excel"],
    },
    {
        "title": "Tools",
        "icon": "🛠️",
        "items": ["Git", "GitHub", "VS Code", "Jupyter Notebook","Google Colab","pyCharm"],
    },
    {
         "title": "Soft Skills",
                "icon": "🎨",
                "items": ["Problem Solving", "Critical Thinking", "Communication", "Teamwork", "Adaptability"],
    },
]

PROCESS = [
    {"step": "01", "title": "Understand", "text": "Start with the real problem, the user and the data before writing any code."},
    {"step": "02", "title": "Design", "text": "Sketch the flow, pick the simplest architecture that works, plan the APIs."},
    {"step": "03", "title": "Build", "text": "Write clean, tested code and wire up the AI, backend and UI together."},
    {"step": "04", "title": "Ship", "text": "Deploy, document with a clear README and iterate on feedback."},
]

PROJECTS = [
    {
        "tag": "AI Voice/calling Agent",
        "title": "Real Estate AI Calling Agent",
        "text": (
            "A live AI voice-calling agent that talks in Hindi, Hinglish and basic English, "
            "qualifies property leads (budget, location, BHK, timeline) and generates a call summary."
        ),
        "stack": ["Python", "Gemini API", "Flask", "Streamlit", "SQLite", "Vapi"],
        "github": "https://github.com/sonu3012/real-estate-ai-calling-agent",   # TODO: replace with the repo link
        "live": "",
    },
    {
        "tag": "AI Chatbot Agents",
        "title": "AI Order Tracking & Customer Support Agent",
        "text": (
            "An agent that answers online-store customer questions by choosing and chaining tools "
            "(order lookup, product search) and handles invalid orders without making up data."
        ),
        "stack": ["Python", "OpenAI / Gemini API", "Tool Calling", "Flask"],
        "github": "https://github.com/sonu3012/AGENTIC_AI_STORE",   # TODO
        "live": "https://agenticaistore-nn6g8svpytyd5uajasmytf.streamlit.app/",
    },
    {
        "tag": "Machine Learning",
        "title": "Movie Recommendation System",
        "text": "A content-based movie recommender with search, posters and movie details in a clean Streamlit interface.",
        "stack": ["Python", "Machine Learning", "Streamlit"],
        "github": "https://github.com/sonu3012/movie-recommendation-system",   # TODO
        "live": "https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/",
    },
    {
        "tag": "Data Science",
        "title": "House Price Prediction",
        "text": "A regression-based model that predicts house prices from property features.",  # TODO: add dataset / accuracy
        "stack": ["Python", "Machine Learning", "Data Analysis"],
        "github": "https://github.com/sonu3012",   # TODO
        "live": "",
    },
    {
        "tag": "Client Website",
        "title": "KK Engineering Website",
        "text": (
            "A full website for an HVAC and AC ducting business in Pune with services, project gallery, "
            "admin dashboard and a WhatsApp enquiry form."
        ),
        "stack": ["Next.js", "Tailwind CSS", "FastAPI"],
        "github": "https://github.com/sonu3012/kk-engineering-website",   # TODO
        "live": "https://kk-engineering-website-1.onrender.com/",
    },
]

EXPERIENCE = [
        {
            "company": "Remarkable Skills",
            "role": "Data Analytics Intern",
            "period": "Jun 2025  Jul 2025",
            "location": "Remote",
            "points": [
                "Worked on data analysis, data cleaning, and visualization using Python, Pandas, and analytical tools.",
                "Gained hands-on experience transforming raw data into meaningful insights."
            ],
        },

        {
            "company": "Grass Solution",
            "role": "Data Science Trainee & Intern",
            "period": "Jan 2025 – May 2025",
            "location": "On-site",
            "points": [
                "Completed comprehensive Data Science training with hands-on experience in Python, data analysis, machine learning, and data visualization.",
                "Worked on practical projects including Movie Recommendation System and House Price Prediction System."
            ],
        },

        {
            "company": "Tech Force Academy",
            "role": "Salesforce Intern",
            "period": "Jul 2024 – Aug 2024",
            "location": "Remote",
            "points": [
                "Completed hands-on training and internship focused on Salesforce fundamentals and CRM concepts.",
                "Gained practical experience with Salesforce features and cloud-based CRM solutions."
            ],
        },
    ]

EDUCATION = [
    {
        "degree": "B.Tech in Artificial Intelligence & Data Science",
        "school": "Arya College of Engineering & IT, Jaipur (RTU)",
        "detail": "CGPA 8.0",
    },
]

CERTIFICATIONS = [
    {"title": "Forecasting Using Machine Learning Tools", "issuer": "NPTEL+ Workshop · Syracuse University faculty", "date": "Jan 2025"},
    {"title": "Data to Dashboard: Mastering Visual Storytelling with Tableau", "issuer": "NPTEL+ Workshop", "date": "Feb 2025"},
    # TODO: add more from your resume
]
