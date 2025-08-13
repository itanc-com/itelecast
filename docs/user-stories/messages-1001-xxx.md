# User Story: Schedule or Send a Message

## Title
As a user, I want to submit a message to the system with an optional scheduled delivery time, so that my message can be sent immediately or at my preferred future time.

## Narrative
As a system user,  
I want to send a message to the service,  
and optionally specify a time for it to be published,  
So that my message can be delivered instantly if no schedule is set,  
Or scheduled for delivery at the exact time I choose.

## Acceptance Criteria

- I can submit a message with or without a scheduled time.
- If I provide a valid future schedule time, the message is delivered at that time.
- If I do not specify a schedule, or if the time is invalid or in the past, my message is delivered immediately.
- I receive confirmation about the message status (scheduled or delivered).

## Reference

For technical details about this functionality, see the API specification in [./api-spec-messages-1001.md](./api-spec-messages-1001.md).