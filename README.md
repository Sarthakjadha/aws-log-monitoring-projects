# Real-Time Application Log Monitoring & Alerting System on AWS


📌 Project Overview



This project implements a real-time application log monitoring and alerting system using AWS services.  

It continuously collects application logs from an EC2 instance, analyzes them using Amazon CloudWatch, and automatically sends email alerts when ERROR-level log events are detected.



The project simulates a real-world production monitoring scenario commonly used in DevOps and cloud environments.



---



 🛠 AWS Services Used



- Amazon EC2 :– Hosts the application and generates logs

- Amazon CloudWatch Agent : – Collects logs from EC2

- Amazon CloudWatch Logs : – Centralized log storage

- CloudWatch Metric Filters : – Converts ERROR logs into metrics

- CloudWatch Alarms : – Triggers alerts based on thresholds

- Amazon SNS : – Sends email notifications

- AWS IAM : – Secure role-based access management

---

🔄 Project Workflow

EC2 → CloudWatch Agent → CloudWatch Logs → Metric Filter → Alarm → SNS → Email

1. A Python application running on EC2 continuously writes logs to `/var/log/app.log`

2. CloudWatch Agent monitors the log file and pushes logs to CloudWatch Logs

3. A metric filter scans logs for the keyword `ERROR`

4. Each detected error increments a custom CloudWatch metric

5. A CloudWatch alarm monitors the metric value

6. When the threshold is breached, an SNS email alert is triggered instantly



---



🧩 Application Code



import logging

import random

import time



logging.basicConfig(

&nbsp;   filename="/var/log/app.log",

&nbsp;   level=logging.INFO,

&nbsp;   format="%(asctime)s %(levelname)s %(message)s"

)



while True:

&nbsp;   if random.choice(\[True, False]):

&nbsp;       logging.error("ERROR: Database connection failed")

&nbsp;   else:

&nbsp;       logging.info("INFO: Application running normally")



&nbsp;   time.sleep(10)


---

🚀 Future Enhancements

1 Slack or SMS notifications

2 Lambda-based auto-remediation

3 CloudWatch dashboards

4 Infrastructure as Code (Terraform / CloudFormation)

5 Auto Scaling integration

---


📁 Project Structure
aws-log-monitoring-project/
├── README.md
├── app.py
├── architecture/
│   └── architecture-diagram.png
└── screenshots/
    ├── Matric.png
    ├── app group error.png
    ├── app log group.png
    ├── cloudwatch.png
    ├── ec2.png
    ├── email.png
    ├── sns.png
    └── terminal.png





