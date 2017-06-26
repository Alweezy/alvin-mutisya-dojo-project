# Dojo Room Allocation Software

---

[![Build Status](https://travis-ci.org/Alweezy/alvin-mutisya-dojo-project.svg?branch=develop)](https://travis-ci.org/Alweezy/alvin-mutisya-dojo-project)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/Alweezy/alvin-mutisya-dojo-project/badge.svg?branch=develop)](https://coveralls.io/github/Alweezy/alvin-mutisya-dojo-project?branch=develop)
---

![Andela Logo](https://3xyh3sqxv063a8xzo5uk2zn1-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Andela-logo-landscape-blue-400px.png)

---

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in.
When a new Staff joins they are assigned an office space only.
This program digitizes and randomizes a room allocation system for one of Andela Kenya’s
facilities called The Dojo.


## Installation

- Create a virtual environment
```
virtualenv venv
```

- Activate your virtual environment
```
source venv/bin/activate
```

- Clone the repo

> git clone https://github.com/Alweezy/alvin-mutisya-dojo-project.git

- Once in the app directory, install Requirements
```
pip install -r requirements.tx
```


---

## Usage

```python

Usage:
    dojo create_room (Living|Office) <room_name>...
    dojo add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    dojo print_room <room_name>
    dojo print_allocations [--o=filename.txt]
    dojo print_unallocated [--o=filename.txt]
    dojo reallocate_person <employee_id> <new_room_name>
    dojo load_people <filename>
    dojo save_state [--db=sqlite_database]
    dojo load_state <sqlite_database>
    dojo (-i | --interactive)

Options:
    -h,--help  :  Show this screen.
    -i,--interactive  :  Interactive Mode
    -v,--version  :  Version of the system
```
---
### Explanation:
___
The ```dojo create_room (Living|Office) <room_name>...```  command creates rooms in the Dojo
> Using this command, the user can create as many rooms as possible by specifying multiple room names
  after the create_room command.

```add_person <person_name> <FELLOW|STAFF> [wants_accommodation]``` adds a person to the system and allocates the person
 a random room
>wants_accommodation here is an optional argument which can be either Y or N.
The default value if it is not provided is N.

```print_room <room_name>``` prints  the names of all the people in room_name on the screen.

```print_allocations [-o=filename]```  prints a list of allocations onto the screen.
> Specifying the optional -o option here outputs the registered allocations to a txt file.

```print_unallocated [-o=filename]``` prints a list of unallocated people to the screen.
> Specifying the -o option here outputs the information to the txt file provided.

```reallocate_person <person_identifier> <new_room_name> - reallocates the person with
person_identifier to new_room_name.

```load_people``` adds people to rooms from a txt file.

```save_state [--db=sqlite_database]``` persists all the data stored in the app to a SQLite database.
> Specifying the --db parameter explicitly stores the data in the sqlite_database specified.

```load_state <sqlite_database>``` loads data from a database into the application.


### License

- This app is provided under the [MIT License](https://opensource.org/licenses/MIT)

### Asciinema
- Follow [This link](https://asciinema.org/a/2chdxdxi21fv3mycrzk1unyor)
