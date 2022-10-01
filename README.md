wallabag2GoodLinks converter
============================

Converts a [wallabag](https://www.wallabag.org/) JSON export to [GoodLinks](https://goodlinks.app/) format.


Wallabag format
---------------

* `is_archived` (0/1)
* `is_starred` (0/1)
* `tags` (List)
* `is_public` (true/false)
* `id`
* `title`
* `url`
* `given_url`
* `content` (HTML)
* `created_at` (yyyy-mm-ddThh:mm:ss+hh:mm)
* `updated_at`
* `published_at`
* `published_by` (List)
* `annotations` (List)
* `mimetype` (text/html)
* `language` (en)
* `reading_time` (Int)
* `domain_name`
* `preview_picture` (URL)
* `http_status` ("200")
* `headers` (Object)


GoodLinks format
----------------

* `readAt` (Unixtime)
* `addedAt`
* `summary`
* `starred` (true/false)
* `title`
* `tags` (List)
* `url`
