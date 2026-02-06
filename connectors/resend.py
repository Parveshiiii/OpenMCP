import os
import resend
import asyncio
from dotenv import load_dotenv; load_dotenv()

if "RESEND_API_KEY" in os.environ:
    resend.api_key = os.getenv("RESEND_API_KEY")
else:
    raise KeyError("NO Resend API key please set it in the .env file")

class EmailSender:

    def __init__(self, to: list[str], subject: str, html: str, from_: str = "OpenMCP <onboarding@resend.dev>"):
        self.from_ = from_
        self.to = to
        self.subject = subject
        self.html = html
    
    async def send_mail(self):
        params: resend.Emails.SendParams = {
            "from": self.from_,
            "to": self.to,
            "subject": self.subject,
            "html": self.html
        }
        return await asyncio.to_thread(resend.Emails.send, params)

async def send_email(to: list[str], subject: str, html: str) -> str:
    """
    Send an email using the Resend API.
    
    Args:
        to: List of email addresses to send to.
        subject: The subject of the email.
        html: The HTML content of the email body.
    """
    sender = EmailSender(to=to, subject=subject, html=html)
    result = await sender.send_mail()
    return str(result)
