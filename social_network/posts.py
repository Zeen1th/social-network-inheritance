from datetime import datetime

class Post:
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None  # User is initially None
        self.timestamp = timestamp or datetime.now()

    def set_user(self, user):
        self.user = user

class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)

    def __str__(self):
        user_str = f"@{self.user.first_name} {self.user.last_name}" if self.user else "Unknown User"
        timestamp_str = self.timestamp.strftime('%A, %b %d, %Y')
        return f'{user_str}: "{self.text}"\n\t{timestamp_str}'

class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        user_str = f"@{self.user.first_name} {self.user.last_name}" if self.user else "Unknown User"
        timestamp_str = self.timestamp.strftime('%A, %b %d, %Y')
        return f'{user_str}: "{self.text}"\n\t{self.image_url}\n\t{timestamp_str}'

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        user_str = f"@{self.user.first_name} Checked In" if self.user else "Unknown User"
        timestamp_str = self.timestamp.strftime('%A, %b %d, %Y')
        return f'{user_str}: "{self.text}"\n\t{self.latitude}, {self.longitude}\n\t{timestamp_str}'

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.set_user(self)  # Set the post's user to this user
        self.posts.append(post)

    def follow(self, other):
        self.following.append(other)

    def get_timeline(self):
        # Get all posts from followed users
        timeline_posts = []
        for followed_user in self.following:
            timeline_posts.extend(followed_user.posts)
        # Sort by timestamp (newest first)
        return sorted(timeline_posts, key=lambda post: post.timestamp, reverse=True)

    def __str__(self):
        return f'<User: "{self.first_name} {self.last_name}">'
