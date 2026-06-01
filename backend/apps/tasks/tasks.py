from celery import shared_task


@shared_task
def send_task_notification(task_id, username):
    """
    Simulate sending a notification when a task is created.
    In production this would send an email or push notification.
    """

    print(f'Sending notification to {username} for task {task_id}')
    return f'Notification sent for task{task_id}'