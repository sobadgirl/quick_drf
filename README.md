# Quick DRF

Start a DRF project quickly. Integrated many plugins.

It's self-use project, and **not suit with new Djangor**. You must familiar with django and drf.

## Usage:

0. please make sure that you hava `poetry` installed and `python >= 3.8`
1. clone this repository
2. rename the **two** dirs `quick_drf` as you like, mark it as `<project_name>`
3. change the value of `project_name` in `<project_name>.settings.py` and `manage.py`.
4. then, install dependencies by run `poetry install`
5. start your server: `poetry run python manage.py runserver 0:8000`

## Features

1. Add `page` `limit` pagination. at `<project_name>.pagination`
2. Add some `permissions` in `<project_name>.permissions`

## Installed Plugins

#### [drf-extensions](https://github.com/chibisov/drf-extensions)

**Notice:**
Actually used [this](https://github.com/sobadgirl/drf-extensions) version with some updates: [PR](https://github.com/sobadgirl/drf-extensions/pull/1), [PR](https://github.com/chibisov/drf-extensions/pull/328)

I add this to use Nested routes. With this plugin, you can visite url like:

```
/api/users/1/
/api/users/1/houses/
/api/users/1/houses/2/
/api/users/1/houses/2/tables
/api/users/1/houses/2/tables/1
...
```

just need:

1. add `NestedViewSetMixin` to your `ViewSet`
   ```
   class YourViewSet(NestedViewSetMixin, ...):
       pass
   ```
2. register router
   ```python
   from rest_framework_extensions.routers import ExtendedSimpleRouter
   router = ExtendedSimpleRouter()
   router.register(
       "users",
       UserViewSet,
       basename="user"
   ).register(
       "houses",
       HouseViewSet,
       basename="user-houses",
       parents_query_lookups=["user"]
   ).register(
       "tables",
       TableViewSet,
       basename="user-house-tables",
       parents_query_lookups=["user", "hose"]
   )
   ```

#### [django-url-filter)](https://github.com/miki725/django-url-filter)

Used this filter as default filter in `settings.REST_FRAMEWORK`

You can filter your models using request query params with this plugin, like:

```
/api/users?created_at__date=2022-22-22
/api/users?id__gte=30
...
```

#### [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

I added this to show SQLs to make majorizations.

#### [rest-framework-generic-relations](https://github.com/Ian-Foote/rest-framework-generic-relations)

This is use to serializer generic foreign keys.

#### [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)

This is use to generate and authenticate JWT token. Just visit `/api/token/` to get a JWT token.

url defined in `quick_drf.urls`

#### [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

This is use to allow for CORS headers. default allow all.

#### [django-environ](https://github.com/joke2k/django-environ)

This is used to read env from `.env` file and parse into django recognizable format. With this, you can define db just like:

```
# settings.py
DATABASES = {
    "default": env.db_url()
}

# .env
db_url=mysql://root:password@localhost:3306/test
```

#### [django-extensions](https://github.com/django-extensions/django-extensions)

The main use of me is `shell_plus`, it cal auto import all models

#### [ipython]

Add to dev dependencies.

#### [django-restql](https://github.com/yezyilomo/django-restql)

This plugin allows you to query you models and filter `fields`, with this plugin, you can only take some fields of your model:

```
/api/users?query={id,username}

// You will got response like
[
    {
        id: 1,
        username: "xxx1"
    },
    {
        id: 2,
        username: "xxx2"
    },
    ...
]
```

OR query with some params

```
/api/users?query=(id: 2){username,avatar}

// You will got response with models only `id=2`
[
    {
        username: "xxx2",
        aratar: "xxxx"
    }
]
```

**Notice**:
This query filter not realy executed by this plugin, it just convert the `GQL-like` query to request params, then the filter_backends executed the realy query.

The `id`, `username`, `avatar`, `...` are fields of your model `User`.

Just need:

1. add `QueryArgumentsMixin` to your `ViewSet`
   ```
   from django_restql.mixins import QueryArgumentsMixin
   class YourViewSet(QueryArgumentsMixin, ...):
       pass
   ```
2. add `DynamicFieldsMixin` to your `Serializer`
   ```
   from django_restql.mixins import DynamicFieldsMixin
   class YourSerializer(DynamicFieldsMixin, ...):
        pass
   ```

#### [drf-spectacular](https://github.com/tfranzel/drf-spectacular)

This plugin is API doc generator. and urls ware add to `quick_drf.urls`, just view `/schema/redoc` or `/schema/swagger`
