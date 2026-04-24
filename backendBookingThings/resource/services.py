from datetime import datetime
from .models import Reservation
from django.db import transaction
from django.core.mail import send_mail

def is_resource_available(resource, date, startAt, endsAt, waitList):
    day_name = datetime.strptime(str(date), "%Y-%m-%d").strftime("%A")

    schedule = resource.availableSchedule.get("avialableDays", [])

    day_schedule = next(
        (d for d in schedule if d["day"] == day_name),
        None
    )

    if not day_schedule:
        return False, "No disponible ese día"

    day_start = int(day_schedule["startAt"])
    day_end = int(day_schedule["endsAt"])

    if not (day_start <= startAt and endsAt <= day_end):
        return False, "Fuera del horario permitido"

    reservations = Reservation.objects.filter(
        resource=resource,
        date=date,
        status__in=['requested', 'confirmed'],
        waitList=False
    )

    for r in reservations:
        if not (endsAt <= r.startAt.hour or startAt >= r.endsAt.hour):
            if waitList == False:
                return False, "Horario ya reservado"

    return True, "Disponible"



def promote_waitlist(released_reservation):
    with transaction.atomic():

        # SEARCH SAME RESOURCE IN A SAME TIME SLOT
        next_reservation = (
            Reservation.objects
            .select_for_update()
            .filter(
                resource=released_reservation.resource, 
                waitList=True,
                status="requested"
            )
            .filter(
                startAt=released_reservation.startAt,
                endsAt=released_reservation.endsAt
            )
            .order_by("createdAt")
            .first()
        )

        if not next_reservation:
            return None

        next_reservation.waitList = False
        next_reservation.status = "confirmed"
        next_reservation.save()

        sendFakeEmail(next_reservation)

        return next_reservation
    

def sendFakeEmail(reservation):

    print(reservation.user.email)

    if not reservation.user.email:
        return "No email provided"

    send_mail(
        subject="Reserva confirmada",
        message=f"""
            Hola {reservation.user.username},
            Tu reserva para {reservation.resource.name} ha sido confirmada.
            Fecha: {reservation.date}
            Gracias por usar la plataforma.
        """,
        from_email="noreply@bookingthings.com",
        recipient_list=[reservation.user.email],
        fail_silently=False,
    )