# Seal Final Project

- **Name**: Erick Valencia
- **App**: Memorial Moments
- **Description**: Somewhat like Facebook and your own personal diary. A place for you to store events, pictures of said events, who attended, and much more

- **Deployed**:

## Dependencies
- TBD
- TBD
- TBD
- TBD


### Frontend: Svelte

###
- As a user, I would like to be able to create an account
- As a user, I would like to be able to sign into my account
- As a user, I wanted to be informed of what this site does
- As a user, once I learn about the site, I want to go to the homepage
- As a user, I want to be able to store memorable days
- As a user, I want to be able to add pictures
- As a user, I want to be able to see both of those things on the home page
- As a user, I want to be able to delete both of those things
- As a user, I want to be able to update both of those things
- TBD

| Route Name | Endpoint | Method | Description |
|------------|----------|--------|-------------|
| Signup | /signup | GET | Create user |
| Login | /login | GET | sign in |
| Education page | /education | GET | Learn about site |
| Index | /home | GET | Home page |
| GoodMemory ID show | /home/goodmemory/id | GET | bring to specific memory by id |
| BadMemory ID show | /home/badmemory/id | GET | bring to specific memory by id |
| Picture ID show | /home/picture/id | GET | bring to specific photo by id |
| Create Goodmemory | /home/goodmemory/new | POST | create a new memory |
| Create Badmemory | /home/badmemory/new | POST | create a new memory |
| Create new picture | /home/picture/new | POST | create new picture |
| Update a Badmemory | /home/badmemory/id | PUT | update memory |
| Update a picture | /home/picture/id | PUT | update picture |
| Delete Goodmemory | /home/goodmemory/id | DELETE | delete memory |
| Delete badmemory | /home/badmemory/id | DELETE | delete memory |
| Delete picture | /home/picture/id | DELETE | delete picture |

## ERD

![ERD](https://i.imgur.com/ePHMz42.jpg)