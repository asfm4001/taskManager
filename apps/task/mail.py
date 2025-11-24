from django.core.mail import send_mail

def notify_by_mail(instance):
    subject = "[系統自動發送] TaskManger"
    body = f"Dear {instance.owner}, 特別通知您，任務'{instance.title}'狀態已更改。"
    return send_mail(
        subject,
        body,
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )