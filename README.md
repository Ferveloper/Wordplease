# Wordplease

Wordplease is a Python/Django blogging platform to provide valuable content to everyone. Sign up and share your knowledge with the world!

## Web URLs

| URL | Action |
| ------- | --- |
| `/` | Home |
| `/admin/` | Admin site  |
| `/login/` | User login |
| `/logout/` | User logout |
| `/signup/` | User signup  |
| `/blogs/` | Blogs list |
| `/blogs/<str:username>` | User blog |
| `/blogs/<str:username>/<int:pk>` | User blogpost |
| `/new/` | Create new post |

## API Endpoints

| URL | Method | Action | Permission |
| ----| ------ | ------ | ------ |
| `/api/users/` | POST | Create user | Any |
| `/api/users/<pk>` | GET | User detail | Admin and Owner |
| `/api/users/<pk>` | PUT | Update user | Admin and Owner |
| `/api/users/<pk>` | DELETE | Delete user | Admin and Owner |
| `/api/blogs/` | GET | Blogs list | Any |
| `/api/blogs/<username>` | GET | User blog posts | Any |
| `/api/posts/` | POST | Create post | Owner |
| `/api/posts/<pk>` | GET | Post detail | Any |
| `/api/posts/<pk>` | PUT | Update post | Admin and Owner |
| `/api/posts/<pk>` | DELETE | Delete post | Admin and Owner |

Additionaly, published posts will be seen in GET methods by anyone, but not published posts only will  be seen by the owner and admin.
