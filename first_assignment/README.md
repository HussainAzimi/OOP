# First Assignment
This project is for the first assignment of the Object Oriented Programming class 

## Setup Environment
1. Create and active a virtual environment
2. Install dependencies


## Implement basic Object Oriented Programming Sample Tracking Objects application

- **Encapsulation:** I protected tube's internal state by using private-ish attributes (_volume_uL) and exposing them only via read-only properties.
  This prevent users from manually setting negative volumes.

- **EAFP:** in add_volume and consume_volume, I prioritized creating the SampleEvent first. This ensures that validation happends naturally before the tube's state is ever modified.

- **Future Improvement:** In a future version, I would add a "rollback" mechanism if a transfer_to fails halfway trough (e.g., the second tube is full), the first tube should undo its consumption to maintain data integrity.
