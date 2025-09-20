🚀 Serverless Attendance System Using Face Recognition

📝 Overview:
A modern, cloud-powered Face Recognition Attendance System built using AWS Lambda, Amazon Rekognition, DynamoDB, and S3.
This serverless web app allows seamless, accurate employee attendance marking and provides real-time analytics 📊 for admins.

✨ Key Features

👤 Face Recognition-based marking with >90% accuracy

📊 Instant dashboard analytics (daily & weekly summary)

🔐 Secure, scalable, and cost-effective AWS architecture

📑 Table of Contents

🏗️ Architecture

🌟 Features

⚙️ Setup & Deployment

🎯 Usage

🛠️ Tech Stack

📂 Project Structure

🏗️ Architecture

🎨 Frontend: Static website hosted in Amazon S3 (HTML/JS/CSS)

⚡ Backend: AWS Lambda functions (Python), integrated via API Gateway / Lambda Function URL

🖼️ Face Processing: Amazon Rekognition Collection

💾 Data Storage: DynamoDB for attendance records, S3 for image uploads

🌟 Features

⚡ Fast & Accurate Attendance: Automatically marks attendance for faces matching >90% similarity.

📊 Admin Dashboard: Real-time view of daily & weekly attendance, employee count, advanced analytics.

🔒 Robust Security: Base64-encoded images securely transmitted.

🔗 Easy Integration: RESTful APIs with CORS enabled, simple deployment & extensible for other scenarios.

⚙️ Setup & Deployment
🖥️ Frontend:

Place static files (index.html, index.js, style.css) inside /frontend

Host the frontend on Amazon S3 (static website hosting enabled)

⚡ Backend:

Write Lambda functions in lambda_function.py

Deploy Lambda & set up API Gateway or Lambda Function URL

Connect Lambda to DynamoDB & Rekognition

☁️ AWS Resources Needed:

📂 DynamoDB table (e.g., EmployeeAttendance)

🗂️ S3 bucket for image uploads

🖼️ Rekognition collection (e.g., employee_faces)

🔧 Configuration:

Update config variables in frontend (e.g., apiUrl)

🎯 Usage

👩‍💼 Employee: Scan face via browser → attendance marked automatically.
🧑‍💻 Admin: Login to dashboard → view daily/weekly summaries & export data.

🛠️ Tech Stack

⚡ AWS Lambda (Python)

🖼️ Amazon Rekognition

💾 DynamoDB

☁️ Amazon S3 (Static Hosting + Image Storage)

🎨 HTML, CSS, JavaScript (Frontend)
