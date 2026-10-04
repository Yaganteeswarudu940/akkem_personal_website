"""Structured resume content used across every page of the portfolio.

Edit the values below to update the site — no other file needs to change.
"""

PROFILE = {
    "name": "Dr. Akkem Yaganteeswarudu",
    "initials": "AY",
    "title": "Senior Data Scientist @ Deloitte",
    "subtitle": "Ph.D. (NIT Silchar) · Postdoctoral Fellow (SR University)",
    "tagline": (
        "Strategic AI leader turning Generative AI, Agentic Systems, and Explainable AI "
        "research into enterprise-scale impact."
    ),
    "email": "eswar.genai@gmail.com",
    "phone": "+91 8296655882",
    "scholar_url": "https://scholar.google.com/citations?hl=en&user=HvqNYOMAAAAJ",
    "location": "Hyderabad, India",
    "resume_file": "assets/resume.pdf",  # drop your PDF here to enable the download button
    "photo_file": "assets/profile.jpg",  # drop a square photo here to replace the initials avatar
}

CORE_COMPETENCIES = [
    {
        "category": "Leadership",
        "icon": "🧭",
        "skills": [
            "AI Strategy & Roadmap Development",
            "Multi-Disciplinary Team Management (15+ members)",
            "Cross-Functional Collaboration",
            "Budget & Resource Forecasting",
        ],
    },
    {
        "category": "Generative AI & Agentic Systems",
        "icon": "🤖",
        "skills": [
            "RAG Frameworks",
            "Multi-Agentic Orchestration (LangGraph)",
            "LLM Fine-tuning (GPT-4, Gemini)",
            "Prompt Engineering Governance",
        ],
    },
    {
        "category": "Advanced Analytics",
        "icon": "📊",
        "skills": [
            "Explainable AI (SHAP, LIME)",
            "Predictive Modeling",
            "Anomaly Detection",
        ],
    },
    {
        "category": "Operational Excellence",
        "icon": "⚙️",
        "skills": [
            "Azure AI Studio",
            "AWS",
            "Scalable Architecture (FastAPI, AKS)",
            "Agile / GitFlow",
            "Performance Metrics & KPI Design",
        ],
    },
    {
        "category": "Programming",
        "icon": "💻",
        "skills": ["Python", "Pandas", "NumPy", "Scikit-Learn"],
    },
]

EDUCATION = [
    {
        "course": "Postdoctoral Fellow",
        "institute": "SR University, Warangal",
        "branch": "CSE",
        "score": "-",
        "supervisor": "Dr. Muthu Kumar T, Dr. Saroj Kumar Biswas",
    },
    {
        "course": "Ph.D.",
        "institute": "NIT, Silchar",
        "branch": "CSE",
        "score": "9.25 CGPA",
        "supervisor": "Dr. Saroj Kumar Biswas, Dr. Aruna Varanasi",
    },
    {
        "course": "Master's Degree (M.Tech)",
        "institute": "J.N.T.U - SJCET",
        "branch": "CSE",
        "score": "78%",
        "supervisor": "Dr. Chandra Sekhar",
    },
    {
        "course": "Bachelor's Degree (B.Tech)",
        "institute": "J.N.T.U - SJCET",
        "branch": "CSE",
        "score": "74%",
        "supervisor": "Dr. Chandra Sekhar",
    },
    {
        "course": "Intermediate",
        "institute": "Srikrishna Jr College",
        "branch": "MPC",
        "score": "94%",
        "supervisor": "-",
    },
    {
        "course": "SSC",
        "institute": "Govt Boys High School",
        "branch": "All",
        "score": "84%",
        "supervisor": "-",
    },
]

CERTIFICATIONS = [
    "Certified AWS Machine Learning Specialty Professional",
    "Google Cloud Certified — Professional Machine Learning Engineer",
    "Google L400 Highest Badge for GenAI (RAG Frameworks & Generative AI Solution Deployment)",
    "Microsoft Certified Solution Developer / Associate",
]

# ---------------------------------------------------------------------------
# Work experience (most recent first). Each role can carry multiple projects.
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "company": "Deloitte",
        "role": "Data Science Team Manager & Senior Specialist Data Scientist",
        "duration": "Oct 2021 - Present",
        "location": "Hyderabad, India",
        "highlights": [
            "Spearheaded a Multi-Agentic Business Process Analyzer (MAS-BPA) using LangGraph and "
            "Azure Kubernetes Service, automating complex documentation and process reimagination.",
            "Led a 20–30 member team deploying 3 RAG-based solutions that automated 40% of routine "
            "Business Case Modelling, saving an estimated 1,200 man-hours annually.",
            "Enforced code review and content-quality policies across 1,00,000+ LLM training prompts, "
            "accelerating fine-tuning schedules by 2 months while holding a 95% quality standard.",
            "Trained 1,000+ professionals on Python and ML, achieving a 4.8/5.0 satisfaction score "
            "and a 70% skill-adoption rate.",
        ],
        "projects": [
            {
                "name": "Healthcare UMR Classification & Alert Generation",
                "client": "Major Healthcare Provider",
                "tech": ["GPT-4.1", "Dataiku", "Snowflake", "Python", "Agentic AI"],
                "points": [
                    "Designed LLM pipelines (GPT-4.1) to classify Unsolicited Medical Requests into "
                    "General, Sub, Strategic, and Emerging themes.",
                    "Used LLM summarization to surface concise insights on UMR trends across themes.",
                    "Generated actionable alerts tracking volume and distribution change in requests.",
                    "Leveraged Snowflake + Dataiku for scalable pipeline orchestration.",
                ],
            },
            {
                "name": "Multi-Agentic Business Process Analyzer (MAS-BPA)",
                "client": "Internal Deloitte Platform",
                "tech": ["Python", "FastAPI", "LangGraph", "React", "AKS", "Azure PostgreSQL", "GPT-4/Gemini"],
                "points": [
                    "Built a multi-agentic AI solution automating business process analysis and documentation.",
                    "Engineered LangGraph agents — Process Configuration, BPMN Generator, Documentation — "
                    "orchestrated with a human-in-the-loop controller.",
                    "Auto-generated BPMN 2.0 diagrams, process documentation, and BRDs.",
                    "Added a Process Health Check module mapping KPIs to activities for root-cause analysis.",
                    "Proposed future-state 'To-Be' packages (YAML, BPMN, documentation) via AI.",
                    "Built a scalable backend on AKS with FastAPI and Azure PostgreSQL supporting multiple LLM providers.",
                    "Implemented Guardrails and AgentOps for evaluation metrics, PII protection, and content safety.",
                ],
            },
            {
                "name": "GenAI BMR Use Cases",
                "client": "Deloitte Business Case Modelling",
                "tech": ["Python", "GPT-3/4", "LangChain", "Azure AI Studio"],
                "points": [
                    "Led a 10-member team building 3 RAG-based GenAI solutions for Business Case Modelling "
                    "and quantitative data synthesis.",
                    "Automated 40% of routine BMR use cases, saving ~1,200 man-hours annually.",
                    "Enforced code review achieving a 95% quality standard and GitFlow compliance.",
                ],
            },
            {
                "name": "Bedrock - Foundational LLM Training Data",
                "client": "AWS",
                "tech": ["Python", "LLM Evaluation", "Leaderboards"],
                "points": [
                    "Managed multiple 10-person teams reviewing 1,00,000+ prompts for foundational LLM training.",
                    "Enforced a plagiarism-free, grammatically rigorous content policy, accelerating fine-tuning by 2 months.",
                    "Built a Python-based internal leaderboard and KPI system for prompt-ranking teams.",
                ],
            },
        ],
    },
    {
        "company": "Deloitte (Client Engagements)",
        "role": "Data Scientist - Cross-Client Delivery",
        "duration": "2021 - Present",
        "location": "Remote / Hyderabad",
        "highlights": [],
        "projects": [
            {
                "name": "Experience Monitoring",
                "client": "Dell",
                "tech": ["Python", "Pandas", "Flask API"],
                "points": [
                    "Engineered a regression model predicting manufacturing cycle duration across 7 stages.",
                    "Achieved a 15% reduction in MAE vs. baseline, contributing to a 5% cycle-time reduction.",
                    "Consolidated a year of production data from Teradata and Oracle for feature engineering.",
                ],
            },
            {
                "name": "Falcon Project",
                "client": "Johnson & Johnson",
                "tech": ["Python", "Pandas", "Machine Learning"],
                "points": [
                    "Built a supervised ML model achieving 97% accuracy predicting job failures/anomalies.",
                    "Developed ETL completion-time prediction models, improving scheduling reliability by 12%.",
                ],
            },
        ],
    },
    {
        "company": "Sure IT Solutions",
        "role": "Data Scientist",
        "duration": "Prior engagement",
        "location": "India",
        "highlights": [],
        "projects": [
            {
                "name": "Central Clearing House (CCH)",
                "client": "US Transportation Department",
                "tech": ["Python", "NLP", "OpenCV", "Airflow", "Flask API"],
                "points": [
                    "Built an OpenCV + NLP pipeline to identify vehicle number plates across US agencies "
                    "and hubs with 95% recognition accuracy.",
                    "Designed the system architecture, integrating Airflow for file scheduling and a "
                    "high-availability Flask API for model serving.",
                ],
            },
        ],
    },
    {
        "company": "Pyramid IT Solutions",
        "role": "Data Scientist",
        "duration": "Prior engagement",
        "location": "India",
        "highlights": [],
        "projects": [
            {
                "name": "Virtual Nursing Assessment",
                "client": "Healthcare Client",
                "tech": ["Python", "ML/DL", "NLP", "Flask API"],
                "points": [
                    "Built a Rothman Index model over 26 physiological parameters achieving 94% accuracy "
                    "in 24-hour mortality-risk early warnings.",
                    "Applied ML for diabetes classification and heart-disease risk analysis (90% accuracy).",
                    "Used NLP sentiment analysis on patient feedback, driving a 15% UI improvement.",
                    "Mentored 3 junior data scientists on model selection and large-scale patient data analysis.",
                ],
            },
        ],
    },
    {
        "company": "Unisys",
        "role": "Senior Software Engineer, Data Science",
        "duration": "Dec 2017 - Nov 2019",
        "location": "Hyderabad, Telangana",
        "highlights": [],
        "projects": [
            {
                "name": "Civil Registry System",
                "client": "Philippines Government",
                "tech": ["Python", "ML/DL", "NLP", "Chatbot", "Tableau"],
                "points": [
                    "Built an imputation model predicting missing ages in vital-events data with 96% accuracy.",
                    "Predicted certificate demand across cities, cutting document processing time by 10%.",
                    "Designed a Deep Learning chatbot that handled 80% of routine customer inquiries.",
                    "Led Tableau dashboards visualizing 100,000+ annual certificate issuances.",
                ],
            },
        ],
    },
    {
        "company": "Honeywell",
        "role": "Data Scientist",
        "duration": "Feb 2017 - Dec 2017",
        "location": "Bangalore, Karnataka",
        "highlights": [],
        "projects": [
            {
                "name": "Aerospace Estimation Tool (AET)",
                "client": "Honeywell",
                "tech": ["Python", "Machine Learning", "NLTK"],
                "points": [
                    "Built a regression model for budget-plan estimation, reducing forecasting variance by 8%.",
                    "Ran NLTK sentiment analysis on 500+ performance reviews for risk categorization.",
                ],
            },
        ],
    },
    {
        "company": "ITC InfoTech (Contractor)",
        "role": "Data Scientist",
        "duration": "Sept 2016 - Feb 2017",
        "location": "Bangalore, Karnataka",
        "highlights": [],
        "projects": [
            {
                "name": "Escalator Calculation Tool",
                "client": "KONE",
                "tech": ["Python", "Machine Learning"],
                "points": [
                    "Built a supervised ML model optimizing escalator energy consumption (7% efficiency gain).",
                    "Predicted hand-rail requirements, accelerating proposal generation by 1 week.",
                ],
            },
        ],
    },
    {
        "company": "Magus IT Solutions",
        "role": "Software Engineer",
        "duration": "July 2012 - July 2016",
        "location": "India",
        "highlights": [],
        "projects": [
            {
                "name": "Healthipass",
                "client": "Healthipass Product",
                "tech": ["Time Series Analysis", "Data Analysis"],
                "points": [
                    "Optimized appointment-scheduling logic, cutting patient wait times by ~15 minutes.",
                    "Analyzed insurance claim patterns to give patients upfront coverage details.",
                ],
            },
        ],
    },
]

TEACHING = {
    "role": "Assistant Professor, St. John's College of Engineering & Technology",
    "duration": "June 2009 - Nov 2010",
    "subjects": [
        "Machine Learning",
        "Python",
        "Data Structures",
        "C Programming",
        "Compiler Design",
        "Theory of Computation",
        "Formal Languages & Automata Theory",
    ],
    "note": "Guided 15+ student mini- and major-projects.",
}

CORPORATE_TRAINING = [
    "Trained 1,000+ Deloitte professionals on Python and Machine Learning - 4.8/5.0 average satisfaction, "
    "70% 90-day skill-adoption rate.",
    "Associate Editor, IEEE Transactions on Artificial Intelligence (2023-2024).",
    "Reviewer for 20+ SCI/Scopus journals including Neurocomputing, Pattern Recognition, Scientific Reports, "
    "Engineering Applications of Artificial Intelligence, and Computers and Electronics in Agriculture.",
]

INVITED_TALKS = [
    {
        "date": "Jan 2024",
        "host": "Nitte Meenakshi Institute of Technology (3rd Yr CSE)",
        "topic": "Workshop: AI and Machine Learning",
        "impact": "Equipped 80+ participants to prototype basic ML models.",
    },
    {
        "date": "Mar 2024",
        "host": "Sreenidhi Institute of Science and Technology (3rd Yr CSE)",
        "topic": "Guest Lecture: Core Machine Learning & XAI",
        "impact": "Gave students insight into ML maturity models and industry XAI practice.",
    },
    {
        "date": "Jun 2024",
        "host": "Sreenidhi Institute of Science and Technology (2nd Yr CSE)",
        "topic": "Guest Lecture: Python Programming for Data Science",
        "impact": "Built a strong prerequisite foundation for advanced data science coursework.",
    },
    {
        "date": "Feb 2025",
        "host": "St. John's College of Engineering & Technology (3-day Workshop)",
        "topic": "Workshop: Python Programming",
        "impact": "Elevated programming fluency for 100+ students.",
    },
    {
        "date": "Feb 2026",
        "host": "CBIT, Hyderabad",
        "topic": "Workshop: Opening the Blackbox (XAI)",
        "impact": "Practical introduction to Explainable AI use cases.",
    },
    {
        "date": "Mar 2026",
        "host": "NBKR, Nellore",
        "topic": "Workshop on GenAI",
        "impact": "Practical introduction to GenAI use cases.",
    },
    {
        "date": "Oct 2026",
        "host": "TECH, Tadipatri",
        "topic": "Workshop on GenAI and agentic AI",
        "impact": "Practical introduction to GenAI use cases.",
    },
]

PHD_THESIS = {
    "title": "Design of Explainable Crop Recommendation System for Smart Farming using Machine Learning",
    "status": "Ph.D. Awarded",
    "supervisors": "Dr. Saroj Kumar Biswas (NIT Silchar), Dr. Aruna Varanasi (SNIST, Hyderabad)",
    "summary": (
        "Developed a novel, high-performance, interpretable AI system for real-time crop recommendation, "
        "addressing data scarcity, model opacity, and computational efficiency in predictive agriculture."
    ),
    "contributions": [
        "Novel Ensemble-Based Stacking + Attention-based Cascaded Deep Learning Network (AACNet), improving "
        "accuracy while reducing time complexity for real-time deployment.",
        "Hybrid SHAP + LIME feature selection and interpretation methodology for transparent, variable-level "
        "model decisions.",
        "GAN-based synthetic data generation to mitigate labelled-data scarcity in agriculture.",
        "End-to-end architecture: IoT sensor integration, FPGA-accelerated inference, and a production-ready "
        "Streamlit deployment.",
    ],
    "tech": ["GANs", "SHAP", "LIME", "Ensemble Learning", "IoT Integration", "Streamlit"],
}

PUBLICATIONS = [
    {
        "title": "Deciphering the black box: interactive crop recommendation system using Explainable AI with "
        "visualization dashboards",
        "venue": "Journal of Experimental & Theoretical Artificial Intelligence (2025)",
        "url": "https://doi.org/10.1080/0952813X.2025.2595024",
        "type": "journal",
    },
    {
        "title": "AI-Driven Smart Farming Portal: Overcoming Language Barriers and Enhancing Agricultural "
        "Productivity through Machine Learning",
        "venue": "Engineering Research Express (2025, in press)",
        "url": "https://doi.org/10.1088/2631-8695/ade19d",
        "type": "journal",
    },
    {
        "title": "Enhancing Transparency in Smart Farming: Local Explanations for Crop Recommendations Using LIME",
        "venue": "Procedia Computer Science, Vol. 258 (2025), pp. 1993-2005",
        "url": "https://doi.org/10.1016/j.procs.2025.04.450",
        "type": "conference",
    },
    {
        "title": "Analysis of An Intellectual Mechanism of a Novel Crop Recommendation System using Improved "
        "Heuristic Algorithm-based Attention and Cascaded Deep Learning Network",
        "venue": "IEEE Transactions on Artificial Intelligence",
        "url": "https://doi.org/10.1109/TAI.2024.3508654",
        "type": "journal",
    },
    {
        "title": "Streamlit-based enhancing crop recommendation systems with advanced explainable artificial "
        "intelligence for smart farming",
        "venue": "Neural Computing & Applications 36, 20011–20025 (2024)",
        "url": "https://doi.org/10.1007/s00521-024-10208-z",
        "type": "journal",
        "citations": 134,
    },
    {
        "title": "A comprehensive review of synthetic data generation in smart farming by using variational "
        "autoencoder and generative adversarial network",
        "venue": "Engineering Applications of Artificial Intelligence, Vol. 131 (2024), 107881",
        "url": "https://doi.org/10.1016/j.engappai.2024.107881",
        "type": "journal",
        "citations": 341,
    },
    {
        "title": "Smart farming using artificial intelligence: A review",
        "venue": "Engineering Applications of Artificial Intelligence, Vol. 120 (2023), 105899",
        "url": "https://doi.org/10.1016/j.engappai.2023.105899",
        "type": "journal",
        "citations": 512,
    },
    {
        "title": "Role of Explainable AI in Crop Recommendation Technique of Smart Farming",
        "venue": "International Journal of Intelligent Systems and Applications (IJISA), 17(1), 31-52 (2025)",
        "url": "https://doi.org/10.5815/ijisa.2025.01.03",
        "type": "journal",
    },
    {
        "title": "Streamlit Application for Advanced Ensemble Learning Methods in Crop Recommendation Systems "
        "- A Review and Implementation",
        "venue": "Indian Journal of Science and Technology, 16(48), 4688-4702 (2023)",
        "url": "https://doi.org/10.17485/IJST/v16i48.2850",
        "type": "journal",
    },
    {
        "title": "Smart Farming Monitoring Using ML and MLOps",
        "venue": "ICICC 2023, Lecture Notes in Networks and Systems, vol 703, Springer",
        "url": "https://doi.org/10.1007/978-981-99-3315-0_51",
        "type": "conference",
    },
    {
        "title": "Multi Disease Prediction Model by using Machine Learning and Flask API",
        "venue": "5th International Conference on Communication and Electronics Systems (ICCES 2020)",
        "url": "https://doi.org/10.1109/ICCES48766.2020.9137896",
        "type": "conference",
    },
    {
        "title": "Diabetes Analysis and Risk Calculation — Auto Rebuild Model by Using Flask API",
        "venue": "ICIPCN 2020, Advances in Intelligent Systems and Computing, vol 1200, Springer",
        "url": "https://doi.org/10.1007/978-3-030-51859-2_27",
        "type": "conference",
    },
    {
        "title": "Security in Software Applications by Using Data Science Approaches",
        "venue": "Proceedings of International Conference on Sustainable Expert Systems, LNNS vol 176, Springer",
        "url": "https://doi.org/10.1007/978-981-33-4355-9_27",
        "type": "conference",
    },
]

JOURNAL_COUNT = sum(1 for p in PUBLICATIONS if p["type"] == "journal")
CONFERENCE_COUNT = sum(1 for p in PUBLICATIONS if p["type"] == "conference")

PATENTS = [
    {
        "id": "South Africa - 2026/01258",
        "title": "System and Method for Parameter-Efficient and Dynamically Weighted Ensemble-Based Gene "
        "Mutation Classification",
        "inventors": "Akkem Yaganteeswarudu, Muthu Kumar T, Saroj Kumar Biswas",
        "status": "Filed",
    },
    {
        "id": "South Africa - 2024/01704",
        "title": "An Artificial Intelligence Based Explainable Crop Recommendation System",
        "inventors": "Yaganteeswarudu Akkem, Saroj Kumar Biswas, Aruna Varanasi",
        "status": "Granted",
        "note": "Uses Explainable AI (XAI) to enable interpretable decision-making in precision agriculture.",
    },
    {
        "id": "India - Application 445181-001",
        "title": "Artificial Intelligence-Based Processing Device for Providing Smart Farming Crop "
        "Recommendations",
        "inventors": "Yaganteeswarudu Akkem, Saroj Kumar Biswas, Aruna Varanasi",
        "status": "Granted (Design Patent)",
        "note": "Specialized hardware device for accurate, real-time agricultural insights.",
    },
]

# ---------------------------------------------------------------------------
# Faculty-style biosketch (Home page) — modeled on an academic profile layout:
# name banner, stat tiles, Information/Key Notes side panels, biosketch
# paragraph, areas of interest, and a Google Scholar citation summary.
# ---------------------------------------------------------------------------
BIOSKETCH_QUOTE = '"The goal is to turn data into information, and information into insight." — Carly Fiorina'

BIOSKETCH_TEXT = (
    "Akkem Yaganteeswarudu received his B.Tech in Computer Science and Engineering from J.N.T.U - SJCET "
    ", M.Tech in Computer Science and Engineering from J.N.T.U - SJCET, and Ph.D. in Computer Science "
    "and Engineering from NIT Silchar (9.25 CGPA). He is currently working as a Senior Data Scientist and "
    "Data Science Team Manager at Deloitte, and as a Postdoctoral Fellow at SR University, Warangal. His "
    "research interests include Generative AI, Agentic AI, Explainable AI (XAI), Machine Learning, Deep "
    "Learning, and NLP. "
    "He has guided 15+ student mini- and major-projects as a former Assistant Professor, and has mentored "
    "3+ junior data scientists and trained 1,000+ professionals on Python and Machine Learning at Deloitte "
    "with a 4.8/5.0 satisfaction score. He has published 13 peer-reviewed papers (8 journals, 5 conference "
    "papers) with 1,450+ Google Scholar citations, and holds 3 patents (2 granted, 1 filed) spanning "
    "explainable crop recommendation systems and gene mutation classification. He currently serves as "
    "Associate Editor for IEEE Transactions on Artificial Intelligence and reviews for 20+ SCI/Scopus "
    "journals."
)

AREAS_OF_INTEREST = [
    "Generative AI",
    "Agentic AI & Multi-Agent Systems",
    "Explainable AI (XAI)",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "Retrieval-Augmented Generation (RAG)",
    "LLM Fine-tuning & Prompt Engineering",
    "MLOps & Scalable AI Architecture",
    "Smart Farming / Precision Agriculture",
]

KEY_NOTES = [
    {"label": "Journal Publications", "value": JOURNAL_COUNT, "color": "green"},
    {"label": "Conference Publications", "value": CONFERENCE_COUNT, "color": "navy"},
    {"label": "Granted Patents", "value": 2, "color": "orange"},
    {"label": "Patent Applications", "value": 1, "color": "teal"},
    {"label": "Professionals Trained", "value": "1,000+", "color": "green"},
    {"label": "Workshops & Talks Delivered", "value": len(INVITED_TALKS), "color": "navy"},
    {"label": "Student Projects Guided", "value": "15+", "color": "orange"},
]

# Google Scholar summary (from the live profile) — update periodically to stay current.
SCHOLAR_STATS = {
    "citations_all": 1466,
    "citations_since2021": 1454,
    "h_index_all": 12,
    "h_index_since2021": 12,
    "i10_all": 13,
    "i10_since2021": 12,
    "profile_url": PROFILE["scholar_url"],
}

# Approximate citations-by-year — replace with your exact per-year figures from
# Google Scholar (Citations > "Cited by" graph) for a fully accurate chart.
CITATION_TIMELINE = {
    "2021": 7,
    "2022": 12,
    "2023": 82,
    "2024": 256,
    "2025": 661,
    "2026": 427,
}

# ---------------------------------------------------------------------------
# Career Guide content - mentoring philosophy distilled from teaching,
# corporate training, and 15+ years of industry experience.
# ---------------------------------------------------------------------------
CAREER_MILESTONES = [
    {"year": "2016", "event": "Moved into pure Data Science roles (ITC InfoTech, Honeywell), applying ML to "
     "industrial optimization problems."},
    {"year": "2017", "event": "Joined Unisys as Senior Software Engineer, Data Science, delivering NLP and "
     "Deep Learning to a government client."},
    {"year": "2019 - 2021", "event": "Began Ph.D. research at NIT Silchar on Explainable AI for smart farming."},
    {"year": "2021", "event": "Joined Deloitte as a Data Scientist, scaling into GenAI and Agentic AI delivery."},
    {"year": "2024", "event": "Started Postdoctoral Fellowship at SR University; became Associate Editor, "
     "IEEE Transactions on AI."},
    {"year": "Today", "event": "Leading multi-agentic GenAI platforms at Deloitte while mentoring students and "
     "professionals in AI/ML."},
]

CAREER_ADVICE = [
    {
        "title": "Build the fundamentals before chasing the hype",
        "icon": "🧱",
        "body": (
            "Every GenAI system I've shipped still rests on classic ML and statistics fundamentals. Learn "
            "Python, linear algebra, probability, and model evaluation deeply before jumping to the newest "
            "framework — the frameworks change every year, the fundamentals don't."
        ),
    },
    {
        "title": "Make your work explainable, not just accurate",
        "icon": "🔍",
        "body": (
            "A model nobody trusts never gets deployed. My Ph.D. and patents center on Explainable AI (SHAP, "
            "LIME) because stakeholders adopt what they can interpret. Whatever you build, be ready to explain "
            "why it made a decision."
        ),
    },
    {
        "title": "Ship, measure, and quantify your impact",
        "icon": "📈",
        "body": (
            "Don't just say you 'built a model' — quantify the man-hours saved, the accuracy gained, the "
            "process automated. Every project on this site carries a number because that's what turns a resume "
            "line into a promotion case."
        ),
    },
    {
        "title": "Learn to lead teams, not just models",
        "icon": "🤝",
        "body": (
            "Technical depth gets you in the room; leading multi-disciplinary teams keeps you there. Invest "
            "early in mentoring, code review discipline, and clear communication — it compounds faster than "
            "any single algorithm."
        ),
    },
    {
        "title": "Stay close to research, even in industry",
        "icon": "🎓",
        "body": (
            "Publishing, reviewing for journals, and teaching keep my industry work sharp. You don't need a "
            "Ph.D. to do this — reading papers, writing a blog post, or giving a guest lecture builds the same "
            "muscle."
        ),
    },
]

CAREER_FAQ = [
    {
        "q": "How do I move from a software engineering role into Data Science?",
        "a": (
            "Start inside your current job: find one workflow that produces data and prototype a small model "
            "or automation for it — exactly how I moved from Software Engineer to Data Scientist at ITC "
            "InfoTech/Honeywell. A working internal prototype is worth more than a certificate alone."
        ),
    },
    {
        "q": "Is a Ph.D. necessary for a career in AI?",
        "a": (
            "No — but it helps if you want to specialize deeply (e.g., Explainable AI, novel architectures) or "
            "move into research-adjacent leadership. Most of the GenAI delivery work I do today draws more on "
            "industry experience than the Ph.D. itself; the Ph.D. sharpened how I evaluate and communicate "
            "model behavior."
        ),
    },
    {
        "q": "How do I break into Generative AI / Agentic AI specifically?",
        "a": (
            "Pick one real business process, and build an end-to-end RAG or agentic prototype for it — "
            "including evaluation and guardrails, not just a demo notebook. That end-to-end discipline (data → "
            "orchestration → guardrails → measurable KPI) is what separates a toy project from a hire-me "
            "portfolio piece."
        ),
    },
    {
        "q": "What do you look for when mentoring students or junior data scientists?",
        "a": (
            "Curiosity about *why* a model fails, not just that it did. The mentees who ask 'what would change "
            "if I removed this feature' grow the fastest — that instinct is the seed of Explainable AI thinking."
        ),
    },
]

SOCIAL_LINKS = {
    "Email": f"mailto:{PROFILE['email']}",
    "Google Scholar": PROFILE["scholar_url"],
}
