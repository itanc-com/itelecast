# Messages API Specification

This document describes the API endpoint for scheduling or immediately delivering messages.

## Endpoint

`POST /api/v1/messages`

## Request Body

```json
{
  "message": "Hello, Telegram!",
  "schedule_time": "2025-07-31T15:00:00Z"
}
```

- `message` (string, required): The content to be delivered.
- `schedule_time` (string, optional, ISO8601): The time to deliver the message. If omitted, invalid, or in the past, the message will be delivered ASAP.

## Response

### Success (201 Created)

```json
{
  "message_id": "42",
  "status": "scheduled", // or "delivered" if sent immediately
  "message": "Hello, Telegram!",
  "schedule_time": "2025-07-31T15:00:00Z",
  "detail": "Message scheduled for delivery."
}
```

### Error Responses

- **400 Bad Request**
  - Missing or invalid fields

    ```json
    {
      "error": "Message content is required."
    }
    ```

- **422 Unprocessable Entity**
  - Invalid schedule time format

    ```json
    {
      "error": "Schedule time must be in ISO8601 format."
    }
    ```

## Scheduling & Delivery Logic

- If `schedule_time` is provided and is a valid future time, the message is saved and scheduled for delivery at that time.
- If `schedule_time` is missing, invalid, or in the past, the message is saved and delivered immediately.
- Messages are stored in the system database for auditing and status tracking.

## Security Considerations

- Input validation and sanitization for all fields.
- Rate limiting should be applied to prevent abuse.
- Authentication and authorization may be required to access the endpoint.

## Notes

- Future support for message editing and deletion may be added.
- GDPR compliance and data retention policies should be observed for stored messages.
- The endpoint is suitable for both bot and admin-triggered messages.
