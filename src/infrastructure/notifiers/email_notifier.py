from application.dtos.notification_dto import NotificationDTO
from application.interfaces.notifier import Notifier


class EmailNotifier(Notifier):
    def notify(self, recipient, message):
        notification = NotificationDTO(recipient, message)
        print(f"Sending email to {notification.recipient}: {notification.message}")
