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

### License

- This app is provided under the [MIT License](https://opensource.org/licenses/MIT)

### Asciinema
- Follow [This link](https://asciinema.org/a/2chdxdxi21fv3mycrzk1unyor)
