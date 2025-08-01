import datetime

from app.common.http_response.error_response import ErrorCodes, ErrorResponse


class AppBaseException(Exception):
    def __init__(self, *, code: ErrorCodes, message: str, status_code: int = 400, data: dict | None = None):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.data = data or {}


    def to_response_model(self, path: str = "") -> ErrorResponse:
        return ErrorResponse(
            code=self.code,
            message=self.message,
            status=self.status_code,
            timestamp=datetime.datetime.now(datetime.timezone.utc),  # RFC 3339-compliant
            path=path,
            data=self.data,
        )
        
class DatabaseOperationException(AppBaseException):
    def __init__(self, operation: str | None = None, message: str | None = None, data: dict | None = None):
        message = f"Failed to perform {operation} operation. {message} "

        super().__init__(
            code=ErrorCodes.DATABASE_ERROR,
            message=message,
            status_code=500,
            data=data,
        )
        
class EntityNotFoundException(AppBaseException):
    def __init__(self, data: dict, message: str = "Entity not found"):
        super().__init__(
            code=ErrorCodes.ENTITY_NOT_FOUND,
            message=message,
            status_code=404,
            data=data,
        )
        
        
class InvalidRequestException(AppBaseException):
    def __init__(self, message: str = "Invalid Request", data: dict | None = None):
        super().__init__(
            code=ErrorCodes.INVALID_REQUEST,
            message=message,
            status_code=400,
            data=data,
        )