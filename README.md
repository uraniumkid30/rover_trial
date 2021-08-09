# Mars Rover Problem Solution with python

    This project supports python 2.x annd 3.x

# How to run ?

```bash
$ python run.py
```

# Docker

```bash
$ docker-compose up

If you run daemon mode

$ docker-compose up -d
```

# Run in docker

```bash
$ docker-compose exec app python main.py @test.txt
```

# Unittest

```bash
$ python -m unittest -v tests/test_mars_rover.py
```

# Run Unittest in docker

```bash
$ docker-compose exec app python -m unittest -v tests/test_mars_rover.py
```
