import random
from datetime import time, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from emrsystem.models import Doctor, Patient, Visit

GUEST_USERNAME = "guest"
GUEST_PASSWORD = "guest1234"

APPOINTMENT_START_HOUR = 9
APPOINTMENT_END_HOUR = 17
APPOINTMENT_DURATION_MINUTES = (15, 20, 30, 45)
WEEKS_AHEAD = 52 * 3


class Command(BaseCommand):
    help = (
        "Seeds a plain 'guest' demo doctor account and generates randomized "
        "weekly appointments for existing patients over the next 3 years, so "
        "the app always has upcoming appointments to show a demo visitor."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-appointments",
            action="store_true",
            help="Only create/update the guest account, skip appointment generation.",
        )

    def handle(self, *args, **options):
        guest = self._create_guest_doctor()
        self.stdout.write(self.style.SUCCESS(f"Guest doctor ready: {guest.username} / {GUEST_PASSWORD}"))

        if options["skip_appointments"]:
            return

        created = self._generate_weekly_appointments()
        self.stdout.write(self.style.SUCCESS(f"Created {created} appointments across {WEEKS_AHEAD} weeks."))

    def _create_guest_doctor(self):
        guest, _ = Doctor.objects.get_or_create(
            username=GUEST_USERNAME,
            defaults={
                "first_name": "Guest",
                "last_name": "User",
                "email": "guest@demo.com",
                "isDoctor": True,
                "isPatient": False,
                "is_active": True,
                "Phone_Number": "000-000-0000",
                "address": "Demo Account — no address on file",
                "date_of_birth": "1990-01-01",
                "sex": "O",
                "Unit": "01",
                "Department": "gl",
                "Role": "pf",
            },
        )
        guest.set_password(GUEST_PASSWORD)
        guest.is_active = True
        guest.isDoctor = True
        guest.save()
        return guest

    def _generate_weekly_appointments(self):
        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        if not patients or not doctors:
            self.stdout.write(self.style.WARNING("No patients/doctors found, skipping appointment generation."))
            return 0

        doctor_units = {d.pk: d.Unit or "01" for d in doctors}
        today = timezone.now().date()
        # Start of the current ISO week (Monday) so "every week" reads cleanly on a calendar.
        week_start = today - timedelta(days=today.weekday())

        created = 0
        with transaction.atomic():
            for week in range(WEEKS_AHEAD):
                monday = week_start + timedelta(weeks=week)
                num_appointments = random.randint(1, 3)
                for _ in range(num_appointments):
                    patient = random.choice(patients)
                    doctor = random.choice(doctors)
                    appt_date = monday + timedelta(days=random.randint(0, 4))  # weekday appointment
                    if appt_date < today:
                        continue

                    start_hour = random.randint(APPOINTMENT_START_HOUR, APPOINTMENT_END_HOUR - 1)
                    start_minute = random.choice((0, 15, 30, 45))
                    time_from = time(start_hour, start_minute)
                    duration = random.choice(APPOINTMENT_DURATION_MINUTES)
                    till_minutes = start_hour * 60 + start_minute + duration
                    time_till = time(min(till_minutes // 60, 23), till_minutes % 60)

                    Visit.objects.create(
                        patient=patient,
                        date=appt_date,
                        time_from=time_from,
                        time_till=time_till,
                        payment=round(random.uniform(100, 400), 2),
                        assigned_doctor=doctor,
                        Unit=doctor_units.get(doctor.pk, "01"),
                        visit_completed=False,
                    )
                    created += 1
        return created
