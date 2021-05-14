from rest_framework import permissions


class IsAgentOrStaff(permissions.BasePermission):
    """
    View-level permission to only allow Admin,
    Agents and Supervisors view USER object list.
    Assumes {{request.user.is_admin}}
    """

    message = {"message": "Restricted Zone. Only Agents and Staffs allowed."}

    def has_permission(self, request, view):
        # Read permissions are restricted to Anonymous users.
        if request.user.is_anonymous:
            return False

        # Allow all requests from ADMIN, SUPERVISORS or AGENT.
        if request.user.is_admin or request.user.is_staff:
            return True
        return False
