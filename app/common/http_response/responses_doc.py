from typing import Any

from pydantic import BaseModel


class ErrorMessage(BaseModel):
    detail: str


class ResponseDoc:
    @staticmethod
    def HTTP_200_OK(description: str) -> dict:
        return {200: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_201_CREATED(description: str) -> dict:
        return {201: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_202_ACCEPTED(description: str) -> dict:
        return {202: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_203_NON_AUTHORITATIVE_INFORMATION(description: str) -> dict:
        return {203: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_204_NO_CONTENT(description: str, headers: dict[str, Any]) -> dict:
        return {204: {"description": description, "headers": headers}}

    @staticmethod
    def HTTP_400_BAD_REQUEST(description: str) -> dict:
        return {400: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_401_UNAUTHORIZED(description: str) -> dict:
        return {401: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_403_FORBIDDEN(description: str) -> dict:
        return {403: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_404_NOT_FOUND(description: str) -> dict:
        return {404: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_405_METHOD_NOT_ALLOWED(description: str) -> dict:
        return {405: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_409_CONFLICT(description: str) -> dict:
        return {409: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_429_TOO_MANY_REQUESTS(description: str) -> dict:
        return {429: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_422_UNPROCESSABLE_ENTITY(description: str) -> dict:
        return {422: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_498_INVALID_TOKEN(description: str) -> dict:
        return {498: {"model": ErrorMessage, "description": description}}

    @staticmethod
    def HTTP_500_INTERNAL_SERVER_ERROR(description: str) -> dict:
        return {500: {"model": ErrorMessage, "description": description}}
