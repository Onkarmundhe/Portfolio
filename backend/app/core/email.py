from typing import Optional
import smtplib
import time
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

# Global SMTP connection pool with thread safety
_smtp_connection = None
_connection_time = 0
_connection_lock = threading.Lock()

def get_smtp_connection():
    """Get or create SMTP connection with reuse and better keep-alive"""
    global _smtp_connection, _connection_time
    
    with _connection_lock:
        # Check if we have a valid connection (less than 10 minutes old)
        if _smtp_connection and (time.time() - _connection_time) < 600:
            try:
                # Test if connection is still alive with a quick noop
                status = _smtp_connection.noop()
                if status[0] == 250:  # 250 means OK
                    print(f"🔄 Reusing existing SMTP connection (age: {time.time() - _connection_time:.1f}s)")
                    return _smtp_connection
            except Exception as e:
                print(f"⚠️  Existing connection failed: {e}")
                _smtp_connection = None
        
        # Create new connection with optimizations
        print("🔌 Creating new SMTP connection...")
        connection_start = time.time()
        try:
            # Use SMTP_SSL for faster connection (port 465) if available
            if settings.SMTP_PORT == 465:
                server = smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT)
            else:
                server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
                server.starttls()
            
            # Login
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            
            # Set timeout for faster failure detection
            server.sock.settimeout(30)
            
            _smtp_connection = server
            _connection_time = time.time()
            
            connection_duration = time.time() - connection_start
            print(f"✅ New SMTP connection established in {connection_duration:.2f}s")
            return server
            
        except Exception as e:
            print(f"❌ Failed to create SMTP connection: {e}")
            return None

def warm_smtp_connection():
    """Pre-warm SMTP connection on startup"""
    print("🔥 Pre-warming SMTP connection...")
    connection = get_smtp_connection()
    if connection:
        print("✅ SMTP connection pre-warmed successfully")
    else:
        print("❌ Failed to pre-warm SMTP connection")

async def send_email(
    to_email: str,
    subject: str,
    message: str,
    from_name: str,
    from_email: str
) -> bool:
    """
    Send email using SMTP with connection reuse
    """
    start_time = time.time()
    print(f"🚀 Starting email send process for {from_name}")
    
    try:
        # Create message (this is fast)
        msg_start = time.time()
        msg = MIMEMultipart()
        msg['From'] = f"{from_name} <{settings.SMTP_FROM_EMAIL}>"
        msg['To'] = settings.SMTP_TO_EMAIL
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        # Create email body
        body = f"""
New contact form submission from your portfolio:

Name: {from_name}
Email: {from_email}
Subject: {subject}

Message:
{message}

---
This email was sent from your portfolio contact form.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        msg_time = time.time() - msg_start
        
        # Get SMTP connection (reused if possible)
        smtp_start = time.time()
        server = get_smtp_connection()
        if not server:
            raise Exception("Could not establish SMTP connection")
        
        # Send email
        text = msg.as_string()
        server.sendmail(settings.SMTP_FROM_EMAIL, settings.SMTP_TO_EMAIL, text)
        # Don't quit the connection - keep it for reuse
        
        smtp_end = time.time()
        total_time = time.time() - start_time
        smtp_time = smtp_end - smtp_start
        
        print(f"✅ Email sent successfully from {from_name} ({from_email})")
        print(f"⏱️  Total: {total_time:.2f}s | SMTP: {smtp_time:.2f}s | Msg: {msg_time:.3f}s")
        return True
        
    except Exception as e:
        total_time = time.time() - start_time
        print(f"❌ Error sending email after {total_time:.2f}s: {e}")
        return False

def configure_smtp():
    """
    Configure SMTP settings (placeholder)
    
    In production, you would add these to your settings:
    - SMTP_HOST
    - SMTP_PORT
    - SMTP_USERNAME
    - SMTP_PASSWORD
    - SMTP_USE_TLS
    """
    pass