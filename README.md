# Hospital Violence Detection System
## 📌 Overview
Workplace violence in healthcare is a serious but often overlooked issue, with studies showing that **1 in 5 healthcare workers** experience physical violence or verbal abuse. Our **AI-powered Hospital Violence Detection System** aims to detect and prevent violent incidents in real time using video and audio analysis, ensuring a safer work environment for medical staff and patients.
## 🎯 Features
- **Real-time Detection**: Identifies signs of verbal aggression and physical violence.
- **AI-Powered Analysis**: Uses computer vision and deep learning to distinguish between normal and aggressive behavior.
- **Automated Alerts**: Notifies security personnel instantly when violence is detected.
- **Privacy-Focused**: No personal identification—analyzes actions, not individuals.
- **User-Friendly Dashboard**: Displays alerts and logs for monitoring and review.
## 🏥 Beneficiaries
- **Healthcare Workers**: Provides a safer work environment by reducing incidents of violence.
- **Hospitals & Clinics**: Enhances security without additional manpower.
- **Patients**: Ensures a calm and safe healthcare experience.
## 🔍 Ethical Considerations
- **Bias Mitigation**: Trained on diverse datasets to avoid discrimination.
- **Privacy & Security**: All data is encrypted, and no personal identifiers are stored.
- **Transparency**: AI decisions are explainable and auditable.
## 🛠️ Tech Stack
- **Programming Language**: Python
- **Frameworks & Libraries**: OpenCV, TensorFlo

# 🚀 How to Use HackHive (MedSafe AI)

HackHive (MedSafe AI) is an AI-powered **hospital security system** that detects **aggressive behavior** and **alerts security personnel** in real time. Follow the steps below to install, configure, and run the system.

---

## 1️⃣ Prerequisites
Before installing, ensure your system has the following dependencies installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker & Docker Compose** (For containerized deployment)
- **Git** (To clone the repository)
- **FFmpeg** (For audio processing)
- **CUDA Toolkit** (If using GPU acceleration)

---

## 2️⃣ Installation
### 🔹 Clone the Repository
```sh
git clone https://github.com/AbdulMustaf/HackHive.git
cd HackHive
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

> **Note:** If using GPU, install `torch` and `torchvision` with CUDA support.

### 🔹 Set Up Environment Variables
Create a `.env` file in the root directory and add the following:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/medsafe
SECRET_KEY=your_secret_key
CUDA_ENABLED=True
```

---

## 3️⃣ Running the System
### 🔹 Start the Application
```sh
python main.py
```
- This will launch the **MedSafe AI detection pipeline**.
- The system will start **monitoring video, audio, and speech** for signs of violence.

### 🔹 Running with Docker (Recommended)
```sh
docker-compose up --build
```
- This will set up the entire **application + database** inside containers.

---

## 4️⃣ Using the Dashboard
- Open your browser and navigate to **`http://localhost:8000`**.
- View **real-time alerts** and **detection logs** on the dashboard.

---

## 5️⃣ Deployment
For production deployment:
- Use **Kubernetes** or **AWS Lambda** for scalable hosting.
- Store logs in **PostgreSQL** or **Cloud Storage** for compliance.

---

## 6️⃣ Contributing
We welcome contributions! 🚀 If you’d like to improve MedSafe AI:
1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request.

---

## 7️⃣ Support
For issues or suggestions, open an **[Issue](https://github.com/AbdulMustaf/HackHive/issues)** or contact the maintainer.

Happy coding! 🔥👨‍💻
