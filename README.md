# s3-to-local-hybrid-cloud-data-archiver


This project is a lightweight hybrid cloud solution for archiving data from AWS S3 to a local on-premises directory. It automates the secure transfer of files from an S3 bucket, stores them locally, and deletes them from the cloud — ensuring cost-effective storage and compliance.

---

## 🚀 Features

- ✅ Automatically scans S3 bucket for files
- ⬇ Downloads files from S3 to a local directory
- 🗑 Deletes files from S3 after successful download
- 📂 Supports structured archiving to on-premises storage
- 🛡️ Useful for hybrid cloud data retention and cost-saving

---

## 🏗️ Project Structure
s3-archive-script/
│
├── s3_data_archiver.py # Main Python script
├── testfile.txt # Test file (for demonstration)
└── README.md # Project documentation
---

## 🧠 How It Works

1. You upload files to your S3 bucket (`live-data-storing-place`)
2. Run the Python script `s3_data_archiver.py`
3. The script:
   - Downloads all objects in the bucket
   - Stores them in `~/archive-data/`
   - Deletes the original files from the S3 bucket

---

## ⚙️ Prerequisites

- AWS CLI configured with valid credentials
- Python 3.x installed
- IAM permissions for:
  - `s3:GetObject`
  - `s3:DeleteObject`
  - `s3:ListBucket`

---

## 🛠️ Setup & Execution

```bash
# Clone the repo (if uploaded to GitHub)
git clone https://github.com/TejPATHAK/s3-to-local-hybrid-cloud-data-archiver.git
cd s3-archive-script

# Make sure the archive directory exists
mkdir -p ~/archive-data
rm -f ~/archive-data/*

# Upload a file to S3 (for test)
aws s3 cp testfile.txt s3://live-data-storing-place/

# Run the archiver
python3 s3_data_archiver.py

```

##🧾 License
This project is open-source and available under the MIT License.

---
##🙋‍♀️ Author
Tejaswi Pathak
DevOps Enthusiast | Cloud & Automation Engineer
GitHub | LinkedIn
