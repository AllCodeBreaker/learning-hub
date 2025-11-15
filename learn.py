"""Module for learning paths and job roles."""

# from flask import Blueprint, render_template
# learn_bp = Blueprint("learn", __name__, template_folder="templates")


__all__ = ["ALLOWED_DEPARTMENTS", "get_jobs", "get_job", "get_placements", "get_placement"]

ALLOWED_DEPARTMENTS = {
    "cse": {
        "name": "CSE",
        "expansion": "Computer Science and Engineering",
        "desc": "The Computer Science and Engineering (CSE) department focuses on the study of computer systems, software development, algorithms, and data structures. It prepares students for careers in software engineering, data science, artificial intelligence, and more."
    },
    "it": {
        "name": "IT",
        "expansion": "Information Technology",
        "desc": "The Information Technology (IT) department emphasizes the application of technology in business and organizational contexts. It covers topics such as network administration, cybersecurity, database management, and IT project management, preparing students for roles in IT support, systems analysis, and network engineering."
    },
    "ads": {
        "name": "ADS",
        "expansion": "Artificial Intelligence and Data Science",
        "desc": "AI & Data Science focuses on machine learning, data analysis, and building intelligent systems. Students learn statistics, ML algorithms, and practical data pipelines."
    },
    "mech": {
        "name": "MECH",
        "expansion": "Mechanical Engineering",
        "desc": "Mechanical Engineering covers design, thermodynamics, materials, and manufacturing — useful for careers in product development and system design."
    },
    "ece": {
        "name": "ECE",
        "expansion": "Electronics and Communication Engineering",
        "desc": "ECE teaches electronics, signal processing, embedded systems, and communications engineering — leading to roles in hardware, IoT, and telecom."
    }
}

__jobs = {
    "cse": [
        {
            "id": "full-stack",
            "name": "Full Stack Web Developer",
            "desc": "Build both frontend and backend of web applications using modern stacks (React, Node, Django, Flask).",
            "steps": [
                "Learn HTML, CSS, and modern JavaScript (ES6+)",
                "Learn a front-end framework (React / Vue / Angular)",
                "Learn a backend framework (Node/Express, Flask, or Django)",
                "Understand databases (SQL and NoSQL)",
                "Build CRUD projects and deploy them (Heroku, Vercel, Docker)"
            ],
            "resources": [
                {"title": "freeCodeCamp Full Stack Course", "url": "https://www.freecodecamp.org/"},
                {"title": "The Odin Project", "url": "https://www.theodinproject.com/"},
                {"title": "MDN Web Docs", "url": "https://developer.mozilla.org/"}
            ]
        },
        {
            "id": "mobile-dev",
            "name": "Mobile Application Developer",
            "desc": "Create mobile apps for Android/iOS using native or cross-platform frameworks (Kotlin, Swift, Flutter, React Native).",
            "steps": [
                "Learn core programming (Kotlin/Swift/JavaScript)",
                "Pick native or cross-platform (Flutter or React Native)",
                "Build sample apps and learn state management",
                "Integrate APIs, local storage and testing",
                "Publish to app stores and maintain releases"
            ],
            "resources": [
                {"title": "Flutter docs", "url": "https://flutter.dev/docs"},
                {"title": "React Native docs", "url": "https://reactnative.dev/docs/getting-started"}
            ]
        },
        {
            "id": "data-scientist",
            "name": "Data Scientist",
            "desc": "Work with data, build models, and extract insights using statistics, ML, and data pipelines.",
            "steps": [
                "Learn Python and data libraries (pandas, numpy)",
                "Study statistics and machine learning fundamentals",
                "Practice with real datasets and competitions (Kaggle)",
                "Learn model evaluation and deployment (MLops basics)",
                "Build a portfolio of projects and visualizations"
            ],
            "resources": [
                {"title": "Kaggle Learn", "url": "https://www.kaggle.com/learn"},
                {"title": "Hands-On ML textbook", "url": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/"}
            ]
        }
    ],
    "it": [
        {
            "id": "sys-admin",
            "name": "System Administrator",
            "desc": "Manage servers, deploy applications, and ensure uptime and reliability of infrastructure.",
            "steps": [
                "Learn Linux fundamentals and shell scripting",
                "Understand server provisioning and configuration (Ansible, Terraform)",
                "Familiarize with cloud platforms (AWS, GCP, Azure)",
                "Monitor systems and learn backup/restore strategies",
                "Practice troubleshooting and incident response"
            ],
            "resources": [
                {"title": "Linux Journey", "url": "https://linuxjourney.com/"},
                {"title": "DigitalOcean tutorials", "url": "https://www.digitalocean.com/community/tutorials"}
            ]
        },
        {
            "id": "network-engineer",
            "name": "Network Engineer",
            "desc": "Design, maintain, and troubleshoot network infrastructure including routers, switches, and VPNs.",
            "steps": [
                "Learn networking fundamentals (OSI model, TCP/IP)",
                "Study routing and switching concepts",
                "Practice with network labs and simulators",
                "Learn network security and monitoring tools",
                "Gain certifications (optional: CCNA)"
            ],
            "resources": [
                {"title": "Cisco Networking Basics", "url": "https://www.cisco.com/"}
            ]
        },
        {
            "id": "cybersecurity-analyst",
            "name": "Cybersecurity Analyst",
            "desc": "Protect systems and data by monitoring threats, performing vulnerability assessments, and responding to incidents.",
            "steps": [
                "Learn security fundamentals and threat models",
                "Study common vulnerabilities and mitigation techniques",
                "Practice with CTFs and labs (TryHackMe, HackTheBox)",
                "Understand monitoring and SIEM tools",
                "Learn incident response and forensics basics"
            ],
            "resources": [
                {"title": "TryHackMe", "url": "https://tryhackme.com/"},
                {"title": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"}
            ]
        }
    ],
    "ads": [
        {
            "id": "data-scientist",
            "name": "Data Scientist",
            "desc": "Build predictive models, analyze datasets, and communicate insights to stakeholders.",
            "steps": [
                "Learn Python and data libraries (pandas, numpy)",
                "Study statistics and ML fundamentals",
                "Work on real datasets and case studies",
                "Learn model deployment basics and visualization",
                "Build a portfolio and present results clearly"
            ],
            "resources": [
                {"title": "Kaggle", "url": "https://www.kaggle.com/"}
            ]
        },
        {
            "id": "ml-engineer",
            "name": "Machine Learning Engineer",
            "desc": "Productionize ML models, design training pipelines, and optimize performance for real-world use.",
            "steps": [
                "Understand ML lifecycle and engineering principles",
                "Learn model serving and containerization (Docker, Kubernetes)",
                "Build scalable data pipelines",
                "Work on model monitoring and retraining strategies"
            ],
            "resources": [
                {"title": "ML Engineering Guide", "url": "https://ml-ops.org/"}
            ]
        },
        {
            "id": "data-engineer",
            "name": "Data Engineer",
            "desc": "Build and maintain data pipelines, ETL processes, and data warehouses for analytics and ML.",
            "steps": [
                "Learn SQL and data modelling",
                "Learn ETL tools and orchestration (Airflow)",
                "Work with cloud data warehouses (BigQuery, Redshift)",
                "Practice building robust pipelines and testing"
            ],
            "resources": [
                {"title": "Airflow docs", "url": "https://airflow.apache.org/docs/"}
            ]
        }
    ],
    "mech": [
        {
            "id": "mech-design",
            "name": "Mechanical Design Engineer",
            "desc": "Design mechanical systems and components using CAD tools and engineering principles.",
            "steps": [
                "Learn CAD tools (SolidWorks, Fusion360)",
                "Study mechanics, materials, and tolerances",
                "Create prototypes and iterate designs",
                "Understand manufacturing constraints and testing"
            ],
            "resources": [
                {"title": "Autodesk Fusion tutorials", "url": "https://www.autodesk.com/"}
            ]
        },
        {
            "id": "manufacturing-engineer",
            "name": "Manufacturing Engineer",
            "desc": "Optimize manufacturing processes, tooling, and production workflows for efficient fabrication.",
            "steps": [
                "Learn manufacturing processes and quality controls",
                "Understand lean manufacturing and process optimization",
                "Work with CNC, tooling, and shop practices"
            ],
            "resources": [
                {"title": "SME resources", "url": "https://www.sme.org/"}
            ]
        },
        {
            "id": "robotics-engineer",
            "name": "Robotics Engineer",
            "desc": "Work on automation, control systems, and integrating mechanical systems with electronics and software.",
            "steps": [
                "Learn control systems and basic electronics",
                "Practice with microcontrollers and actuators",
                "Integrate sensing and motion planning algorithms",
                "Build small robotic projects and iterate"
            ],
            "resources": [
                {"title": "ROS tutorials", "url": "https://docs.ros.org/"}
            ]
        }
    ],
    "ece": [
        {
            "id": "embedded-engineer",
            "name": "Embedded Systems Engineer",
            "desc": "Develop firmware and embedded software for microcontrollers and real-time systems.",
            "steps": [
                "Learn C/C++ and embedded programming fundamentals",
                "Understand microcontrollers, interrupts, and RTOS basics",
                "Practice with hardware (Arduino, STM32, Raspberry Pi)",
                "Learn debugging tools and flashing workflows"
            ],
            "resources": [
                {"title": "Embedded Systems - Coursera", "url": "https://www.coursera.org/"}
            ]
        },
        {
            "id": "electronics-design",
            "name": "Electronics Design Engineer",
            "desc": "Design PCBs, analog/digital circuits, and prototype electronic systems.",
            "steps": [
                "Study circuit theory and PCB design basics",
                "Learn PCB tools (KiCad, Eagle)",
                "Prototype circuits and test measurement techniques"
            ],
            "resources": [
                {"title": "KiCad tutorials", "url": "https://kicad.org/"}
            ]
        },
        {
            "id": "signal-processing",
            "name": "Signal Processing Engineer",
            "desc": "Work on processing, filtering, and analysing signals for communications and sensor systems.",
            "steps": [
                "Learn signals & systems and filtering theory",
                "Practice using MATLAB or Python (scipy)",
                "Apply techniques to communications or sensor data"
            ],
            "resources": [
                {"title": "Signal Processing - Coursera", "url": "https://www.coursera.org/"}
            ]
        }
    ]
}


def get_job(dept, job_id):
    """Return job dict for given department and job id (slug), or None."""
    jobs = __jobs.get(dept)
    if not jobs:
        return None
    for j in jobs:
        if j.get("id") == job_id:
            return j
    return None


# Sample placements data (companies / roles) with preparation tips
__placements = {
    "cse": [
        {
            "id": "google-frontend-intern",
            "company": "Google",
            "role": "Frontend Intern",
            "tips": [
                "Master JavaScript fundamentals and DOM manipulation",
                "Understand React internals and component design",
                "Practice algorithmic problems (arrays, strings, trees)",
                "Build small projects showcasing frontend skills"
            ],
            "resources": [
                {"title": "Cracking the Coding Interview", "url": "https://www.crackingthecodinginterview.com/"},
                {"title": "Frontend Handbook", "url": "https://frontendmasters.com/books/front-end-handbook/2019/"}
            ]
        },
        {
            "id": "microsoft-sde",
            "company": "Microsoft",
            "role": "Software Development Engineer",
            "tips": [
                "Practice data structures & algorithms regularly",
                "Write clean, testable code and understand OOP concepts",
                "Learn system design basics for backend roles",
                "Work on projects that demonstrate scale and reliability"
            ],
            "resources": [
                {"title": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer"}
            ]
        }
    ],
    "it": [
        {
            "id": "deloitte-it-analyst",
            "company": "Deloitte",
            "role": "IT Analyst",
            "tips": [
                "Understand enterprise IT systems and business processes",
                "Learn SQL and data reporting tools",
                "Practice communication and case-study problem solving"
            ],
            "resources": [
                {"title": "SQLBolt", "url": "https://sqlbolt.com/"}
            ]
        }
    ],
    "ads": [
        {
            "id": "uber-data-scientist",
            "company": "Uber",
            "role": "Data Scientist",
            "tips": [
                "Work on real datasets and feature engineering",
                "Know model evaluation metrics and A/B testing",
                "Prepare clear project case studies for interviews"
            ],
            "resources": [
                {"title": "Kaggle", "url": "https://www.kaggle.com/"}
            ]
        }
    ],
    "mech": [
        {
            "id": "bosch-mech-engineer",
            "company": "Bosch",
            "role": "Design Engineer",
            "tips": [
                "Build strong CAD and drafting skills",
                "Understand manufacturing processes and material selection",
                "Prepare a portfolio of mechanical projects"
            ],
            "resources": [
                {"title": "SolidWorks Tutorials", "url": "https://www.solidworks.com/"}
            ]
        }
    ],
    "ece": [
        {
            "id": "intel-embedded",
            "company": "Intel",
            "role": "Embedded Systems Engineer",
            "tips": [
                "Practice embedded C and low-level programming",
                "Work with microcontrollers and hardware interfaces",
                "Showcase projects with sensors and communication protocols"
            ],
            "resources": [
                {"title": "ARM Developer", "url": "https://developer.arm.com/"}
            ]
        }
    ]
}


def get_placements(dept=None):
    """Return placements for a department or all placements if dept is None."""
    if dept is None:
        return __placements
    return __placements.get(dept, [])


def get_placement(dept, placement_id):
    items = __placements.get(dept, [])
    for p in items:
        if p.get("id") == placement_id:
            return p
    return None





def get_jobs(dept=None):
    if dept is None:
        return __jobs
    elif dept in __jobs.keys():
        return __jobs.get(dept)
    else :
        return dict()

