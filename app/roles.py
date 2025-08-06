from rolepermissions.roles import AbstractUserRole


class Receptionist(AbstractUserRole):
    available_permissions = {
        'can_manage_appointments': True,
        'can_view_clients': True,
    }


class Manager(AbstractUserRole):
    available_permissions = {
        'can_view_reports': True,
        'can_view_clients': True,
        'can_manage_professionals': True,
    }
