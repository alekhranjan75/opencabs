# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-23 14:38
from __future__ import unicode_literals

from django.db import migrations


def copy_booking_vehicle_data_to_booking_vehicle_table(apps, schema_editor):
    pass
    Booking = apps.get_model('opencabs', 'Booking')
    BookingVehicle = apps.get_model('opencabs', 'BookingVehicle')

    for booking in Booking.objects.all():
        vehicle = BookingVehicle(
            booking=booking,
            driver_paid=booking.driver_paid,
            driver_pay=booking.driver_pay,
            driver_invoice_id=booking.driver_invoice_id,
            vehicle=booking.vehicle,
            driver=booking.driver,
            extra_info=booking.extra_info)
        vehicle.save()


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0019_bookingvehicle'),
    ]

    operations = [
        migrations.RunPython(copy_booking_vehicle_data_to_booking_vehicle_table),
    ]
