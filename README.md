# drone-cone-proto

## Milestone 0

### [Requirements Documentation](https://github.com/pharrison31415/drone-cone-proto/blob/main/doc/requirements.md)

## Milestone 1

### [High Level Design Documentation](https://github.com/pharrison31415/drone-cone-proto/blob/main/doc/HighLevelDesign.md)

### [Low Level Design Documentation](https://github.com/pharrison31415/drone-cone-proto/blob/main/doc/LowLevelDesign.md)

### [Wireframe Prototypes Links](https://github.com/pharrison31415/drone-cone-proto/blob/main/doc/WireframeMockup.md)

# Running

When running for the first time, run the following.

```sh
$ python apps/api/manage.py migrate
$ cd apps/web/frontend/
$ npm install
```

To start the api, run `$ python apps/api/manage.py runserver`

To start the frontend server, under `apps/web/frontend/`, run `$ npm run dev`
