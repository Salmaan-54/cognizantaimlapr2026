"""Display appointments."""

from stores.appointmentstore import AppointmentStore


def display_appointments(appointment_store: AppointmentStore):
    """
    Display all appointments in the store along with doctor details and patient details (like ailment) in a readable format
    """
    appointments = appointment_store.get_all_appointments()
    if not appointments:
        print("No appointments found.")
        return
    
    for appointment in appointments:
        doctor = appointment.doctor
        patient = appointment.patient
        print(f"Appointment ID: {appointment.id}")
        print(f"Doctor: {doctor.name} (Specialization: {doctor.specialization})")
        print(f"Patient: {patient.name} (Ailment: {patient.ailment})")
        print(f"Date: {appointment.date}, Time: {appointment.time}")
        print("-" * 40)