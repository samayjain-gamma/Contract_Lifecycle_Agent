import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from src.core.exception import CustomException
from src.core.logger import logger

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(to_email: str, subject: str, body: str):
    logger.info("Entered in to send mail")
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        logger.info("Enter into try block")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            logger.info("enter in with block")
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            logger.info("goinf to call sendmail")
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

        print("Email sent successfully")

    except Exception as e:
        logger.error("Error occured while  sneding mail")
        raise CustomException(e)


if __name__ == "__main__":
    send_email(
        to_email="jainsamay2105@gmail.com",
        subject="Tesing email",
        body="THis is just a sending email",
    )
    # print(f"Username : {EMAIL_ADDRESS}")
    # print(f"Passsword : {EMAIL_PASSWORD}")
