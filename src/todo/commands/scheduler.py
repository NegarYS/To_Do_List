"""Scheduler for periodic tasks using the schedule library."""

import schedule
import time
import threading
from datetime import datetime

from .autoclose_overdue import autoclose_overdue_tasks


class TaskScheduler:
    """Manages scheduled tasks for the Todo application."""

    def __init__(self):
        self.is_running = False
        self.thread = None

    def setup_schedules(self):
        """Setup all scheduled tasks."""

        schedule.every(15).minutes.do(autoclose_overdue_tasks)


        print("✅ Schedules setup completed:")
        print("   - Auto-close overdue tasks: every 15 minutes")

    def run_scheduler(self):
        """Run the scheduler in a loop."""
        self.is_running = True
        self.setup_schedules()

        print(f" Task scheduler started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("   Press Ctrl+C in the terminal to stop the scheduler.")

        while self.is_running:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                print("\n Scheduler stopped by user.")
                break
            except Exception as e:
                print(f" Scheduler error: {e}")
                time.sleep(1)

    def start(self):
        """Start the scheduler in a background thread."""
        if self.is_running:
            print(" Scheduler is already running.")
            return

        self.thread = threading.Thread(target=self.run_scheduler, daemon=True)
        self.thread.start()
        print("✅ Background scheduler started.")

    def stop(self):
        """Stop the scheduler."""
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=5)
        print(" Scheduler stopped.")


# Global scheduler instance
scheduler = TaskScheduler()


def start_scheduler():
    """Start the global scheduler."""
    scheduler.start()


def stop_scheduler():
    """Stop the global scheduler."""
    scheduler.stop()


def run_once():
    """Run all scheduled tasks once (for testing)."""
    print("🔨 Running scheduled tasks once...")
    schedule.run_all()
    print("✅ All scheduled tasks completed.")


if __name__ == "__main__":
    start_scheduler()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_scheduler()