from fastapi import FastAPI , HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {
        "title": "Welcome to the Platform!",
        "content": "This is our very first post. We're excited to see what you create and share.",
    },
    
     2: {
        "title": "FastAPI vs. Django: A Quick Comparison",
        "content": "While Django is 'batteries included,' FastAPI shines for performance and asynchronous endpoints. Choose the right tool for the job!",
    },
    
    3: {
        "title": "Thoughts on the Future of AI",
        "content": "The integration of large language models into everyday coding workflows is accelerating rapidly. What are your predictions for 2026?",
        },
    
    4: {
        "title": "Draft: My Next Great Idea",
        "content": "Need to flesh out the details on the new microservice architecture. Key points: use Kafka, separate read/write DBs...",
    }
}

@app.get('/posts')
def get_all_posts(limit: int = None):
    if limit:
        return text_posts[:limit]
    
    return text_posts

@app.get('/posts/{id}')
def get_posts(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)


@app.post('/posts')
def create_posts(post: PostCreate) -> PostResponse:
    new_post = {'title':post.title, 'content': post.content}
    text_posts[max(text_posts.keys() + 1)] = new_post
    return new_post

@app

