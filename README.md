# wagtail-blog-simple
Simple  and customizable blog app for wagtail 

## Features

- Categories and tags with views
- RSS
- Basic starter templates with pagination
- Comments
- Related Blog
- Rich text editor with gist compatible

## Installation

You should start with a existing wagtail django project and have a basic understanding of Wagtail before starting.
See http://docs.wagtail.io

Tested with Wagtail 2.x and Django 3.1

Refer [here](https://docs.wagtail.io/en/stable/getting_started/index.html) for wagtail configuration 
1. `pip install wagtail-blog-simple`
2. Add `wagtail_blog` to INSTALLED_APPS in settings.py 
3. Update WAGTAILEMBEDS_FINDERS as follows
```
WAGTAILEMBEDS_FINDERS = [
    {
        'class': 'wagtail_blog.embed_finder.GistEmbedFinder'
    }
]
```
4. Add `url(r'^blog/', include('wagtail_blog.urls', namespace="blog")),` to urls.py
5. `python manage.py migrate`
6. Override [templates](/wagtail_blog/templates/blog/) as needed.
7. Create a 'Blog index' page in wagtail cms dashboard (under root page)

 ![image](https://user-images.githubusercontent.com/19246595/133918962-aae57142-71c5-4ff8-b573-46e9b31b4710.png)
8. Then add sub pages to Blog Index page which will your blogs

![image](https://user-images.githubusercontent.com/19246595/133919010-1de1d950-6b4b-46d1-940e-eb6958893418.png)


## Extending

Wagtail blog features abstract base models. If you want to change functionality you may extend this models from `blog.abstract` and use them how you'd like. Do not add `blog` to your INSTALLED_APPS if you do this. You'll need to create your own logic to gather context variables. See blog/models.py for an example of this. Wagtail blog doesn't support any way to "drop in" the blog app and just make minor changes to models.

## Settings

- `BLOG_PAGINATION_PER_PAGE` (Default 10) Set to change the number of blogs per page. Set to None to disable (useful if using your own pagination implementation).
- `BLOG_LIMIT_AUTHOR_CHOICES_GROUP` Optionally set this to limit the author field choices based on this Django Group. Otherwise it defaults to check if user is_staff. Set to a tuple to allow multiple groups.
- `BLOG_LIMIT_AUTHOR_CHOICES_ADMIN` Set to true if limiting authors to multiple groups and want to add is_staff users as well.

## Credits

This is extended version of [this repo](https://github.com/thelabnyc/wagtail_blog) with more features
