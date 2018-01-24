# jenkins_bcrypt_pw_util

Simple Python script that generates Jenkins-compatible bcrypt encrypted passwords on the commandline.

## Usage

```
USAGE: jenkins_bcryptpw.py PASSWORD
```

## Example

```
$ jenkins_bcryptpw.py my_password
plaintext : my_password
hash      : $2a$10$0y4ypazwfO1EP1UAoimns.Ayp52rR1aEWHSqLIVCvy07ZKigXgSpu
check     : passed
```
