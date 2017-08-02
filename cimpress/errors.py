
class CimpressError(Exception):

    def __init__(self, message=None, context=None):
        super(CimpressError, self).__init__(message)
        self.message = message
        self.context = context


class ArgumentError(ValueError, CimpressError):
    pass


class HttpError(CimpressError):
    pass


class ResourceNotFound(CimpressError):
    pass


class AuthenticationError(CimpressError):
    pass


class ServerError(CimpressError):
    pass


class BadGatewayError(CimpressError):
    pass


class ServiceUnavailableError(CimpressError):
    pass


class BadRequestError(CimpressError):
    pass


class RateLimitExceeded(CimpressError):
    pass


class MultipleMatchingUsersError(CimpressError):
    pass


class UnexpectedError(CimpressError):
    pass


class TokenUnauthorizedError(CimpressError):
    pass


error_codes = {
    'unauthorized': AuthenticationError,
    'forbidden': AuthenticationError,
    'bad_request': BadRequestError,
    'action_forbidden': BadRequestError,
    'missing_parameter': BadRequestError,
    'parameter_invalid': BadRequestError,
    'parameter_not_found': BadRequestError,
    'not_found': ResourceNotFound,
    'service_unavailable': ServiceUnavailableError,
}
