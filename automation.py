import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
import datetime

# 1. LOAD THE DATA
# Make sure 'data.csv' is in the same folder as this script
df = pd.read_csv('data.csv')

# 2. GENERATE THE SUMMARY
summary = df.groupby('Category')['Sales'].sum()
print("Report Summary:")
print(summary)

# 3. CREATE A BAR CHART
summary.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales ($)')

# 4. SAVE THE CHART IMAGE
plt.tight_layout()
plt.savefig('report_chart.png')
print("Chart saved as report_chart.png")

# Note: plt.show() is removed so the script sends the email automatically 
# without waiting for you to close a window.

# --- EMAIL CONFIGURATION ---
sender_email = "vaishnavithanda49@gmail.com" 
app_password = "pszt gafx ybct zdqh" 
recipient_email = "vaishnavithanda49@gmail.com" # Fixed the spelling typo here

# Create the email container
msg = EmailMessage()
msg['Subject'] = 'Daily Sales Automation Report'
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content("Hello,\n\nPlease find the automated sales report chart attached.\n\nBest regards,\nPython Automation Bot")

# --- ATTACH THE CHART ---
with open('report_chart.png', 'rb') as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype='image', subtype='png', filename='Sales_Report.png')

# --- SEND THE EMAIL & LOG THE RESULT ---
try:
    print("Connecting to server...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
    
    print("✅ Email sent successfully!")

    # LOG THE SUCCESS
    with open("automation_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] SUCCESS: Report sent to {recipient_email}\n")

except Exception as e:
    # LOG THE ERROR
    with open("automation_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] ERROR: {str(e)}\n")
    print(f"❌ Error: {e}")