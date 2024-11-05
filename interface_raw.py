from abc import ABC, abstractmethod

class NotificationSender(ABC):
  @abstractmethod
  def send_notification(self, message: str) -> None: pass
  
  # Define a regra de construção das classes que herdam de NotificationSender
      
class EmailNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f"Sending email notification: {message}")

class SMSNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f"Sending SMS notification: {message}")
    
class Notificator:
  def __init__(self, notification_sender: NotificationSender) -> None:
    self.__notification_sender = notification_sender 
    
  def send(self, message: str) -> None:
    self.__notification_sender.send_notification(message)
      
obj = Notificator(EmailNotificationSender())
obj.send("Olá mundo!")
