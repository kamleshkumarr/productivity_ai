from datetime import date, timedelta
from .models import DailyActivity

# 🔥 STREAK LOGIC
def get_streak(user):
    today = date.today()
    streak = 0

    while True:
        try:
            activity = DailyActivity.objects.get(user=user, date=today)
            if activity.tasks_completed > 0:
                streak += 1
                today -= timedelta(days=1)
            else:
                break
        except DailyActivity.DoesNotExist:
            break

    return streak


# 🤖 AI MOTIVATION LOGIC
def get_motivation(streak):
    if streak >= 7:
        return "🚀 Elite performer! You're unstoppable!"
    elif streak >= 3:
        return "🔥 Great consistency! Keep pushing!"
    elif streak >= 1:
        return "👍 Good start! Build your streak!"
    else:
        return "💡 Start today. One task is enough!"