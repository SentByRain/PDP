import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

from src.config import CONFIG
from src.database_control.db import get_db
from src.models import Verification

template_env = Environment(loader=FileSystemLoader("src/routers/Mail/templates"))

def render_confirmation_template(template_name: str, **context) -> str:
    """
    Функция для рендеринга HTML-шаблона с переменными.
    """
    template = template_env.get_template(template_name)
    return template.render(**context)

def generate_confirmation_code():
    return str(random.randint(1000, 9999))

def save_code(email : str, code : str):
    db = next(get_db())
    check_user = db.query(Verification).filter(Verification.email == email).first()
    if check_user:
        check_user.code = code

    else:
        new_user = Verification(email=email, code=code)
        db.add(new_user)

    db.commit()

    return f"Code for {email} was succesesfully save to database"

def get_code(email : str):
    db = next(get_db())
    check_user = db.query(Verification).filter(Verification.email == email).first()
    if check_user:
        return check_user.code
    else: 
        raise KeyError(f"Verification code for user {email} wasn't found in database")

def send_confirmation_email(to_email: str):

    try:
        """
        Отправляет email с использованием HTML контента.
        """
        from_email = CONFIG.SMTP_USER
        password = CONFIG.SMTP_PASSWORD

        # Создаём MIME сообщение
        message = MIMEMultipart()
        message["Subject"] = 'Код подтверждения акаунта PDP'
        message["From"] = CONFIG.SMTP_USER
        message["To"] = to_email

        code = generate_confirmation_code()
        save_code(email=to_email, code=code)
        html_content = render_confirmation_template(template_name='confirmation_template.html', confirmation_code=code)

        # Добавляем HTML-контент
        part_html = MIMEText(html_content, "html")
        message.attach(part_html)

        server = smtplib.SMTP_SSL(CONFIG.SMTP_SERVER, CONFIG.SMTP_PORT)
        server.ehlo(from_email)
        server.login(from_email, password)
        server.auth_plain()
        server.send_message(message)
        
        server.quit()

        return to_email

    except Exception as e:
        raise e
    

    

