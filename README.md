# classify_image_web
web app for classify_image.py(tensorflow)

# prerequesties

- python3
- Tensorflow
- git command
- patch command

# how to use

```shell
python build.py
```

```shell
python classify_image_web.py
```

## macOS

```shell
open http://localhost:8000/input
```

## Windows

```shell
start http://localhost:8000/input
```

Firefox,Chrome works well.

## You can use also from CLI

Something like this:

```
curl --data-binary '@/Users/kjunichi/Pictures/IMG_0132.jpg' http://localhost:8000
```
