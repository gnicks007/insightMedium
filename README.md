# insightMedium

Then download web driver to `driver` folder from [Selenium](http://selenium-python.readthedocs.io/) or via the command-line with `curl` (update `{VERSION}` with the latest version code and `{OS}` with your server operating system.

```shell
$ mkdir driver | cd driver
$ curl -O https://chromedriver.storage.googleapis.com/{VERSION}/chromedriver_{OS}.zip
$ unzip chromedriver_{OS}.zip
```

## Documentation

### Users
* `GET /@{username}` - Get user profile

#### Response
```json
{
  "avatar": "1*Y7zH0UM975YmchIO86uIGA.jpeg",
  "bio": "Mixtape of developer, designer and startup. Cofounder and developer of DualCores Studio. Follow my technical blog: http://enginebai.logdown.com/",
  "display_name": "Engine Bai",
  "facebook": "789985027713671",
  "followedby_count": 445,
  "following_count": 238,
  "publications": [
    {
      "creator_user_id": "3301d32a6bba",
      "description": "Stories from the mix of designer and developer. 設計與工程的交織，混搭激盪出不同的想像。",
      "display_name": "DualCores Studio",
      "follower_count": 302,
      "image": {
        "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
        "original_height": 591,
        "original_width": 591
      },
      "logo": {
        "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
        "original_height": 591,
        "original_width": 591
      },
      "name": "dualcores-studio",
      "post_count": 0,
      "publication_id": "275e26e7c1b2",
      "url": "https://medium.com/dualcores-studio"
    },
    ...more
  ],
  "twitter": "enginebai",
  "user_id": "3301d32a6bba",
  "username": "enginebai"
}
```

### Publication
* `GET /{publication_name}` - Get publication profile

```json
{
  "creator_user_id": "3301d32a6bba",
  "description": "Stories from the mix of designer and developer. 設計與工程的交織，混搭激盪出不同的想像。",
  "display_name": "DualCores Studio",
  "follower_count": 302,
  "image": {
    "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
    "original_height": 591,
    "original_width": 591
  },
  "logo": {
    "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
    "original_height": 591,
    "original_width": 591
  },
  "name": "dualcores-studio",
  "post_count": 0,
  "publication_id": "275e26e7c1b2",
  "url": "https://medium.com/dualcores-studio"
}
```

### Post
* `GET /@{username}/posts` - Get user latest posts
* `GET /{publication_name}/posts` - Get publication latest posts
* `GET /top` - Get most popular today posts
* `GET /tags/{tag}` - Get tagged in popular posts
* `GET /tags/{tag}/latest` - Get tagged in latest posts

#### Parameters
|Name   |Type   |Description   |
|---|---|---|
|n   |integer   |The count of posts to return. Default is 10.   |

#### Response
```json
[
  {
    "image_count": 14,
    "post_date": 1478533474858,
    "post_id": "99a3d86df228",
    "preview_image": {
      "image_id": "1*zhnQJhNzp-Oal1-GU1EUKw.png",
      "original_height": 412,
      "original_width": 608
    },
    "read_time": 7.74811320754717,
    "recommend_count": 351,
    "response_count": 10,
    "title": "Make an android custom view, publish and open source.",
    "url": "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228",
    "word_count": 1669
  },
  ...more
]
```

### Post detail
* `GET /post` - Get the post content

#### Parameters
|Name   |Type   |Description   |
|---|---|---|
|u   |string   |The post url to parse content.   |
|format   |string   |(optional) The format of response, the value could be `text`, `html`, `md`, `json`, default is `text`.   |

#### Response

```
## Simple text, json, html, markdown format
```

