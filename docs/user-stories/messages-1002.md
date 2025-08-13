# User Story #1002: Store Messages for Later Processing

## Title
Store Messages for Later Processing by Job Scheduler

## Narrative
As a system user,  
I want the service to store each message in the database,  
So that the message can be processed and sent later by a job scheduler.

## Acceptance Criteria
- I can submit a message through the API.
- The system stores the message in the database along with its metadata (e.g., creation time, status).
- Messages remain in the database until processed by the job scheduler.
- I receive confirmation when the message has been successfully stored.
