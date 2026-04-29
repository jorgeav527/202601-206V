from fastapi import APIRouter, Request, HTTPException, Form, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import get_db_connection
from app.schemas import PostCreate, PostResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_post_or_404(post_id: int):
    with get_db_connection() as conn:
        post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return dict(post)


@router.get("/post/{id}")
def get_post_detail(id: int):
    return get_post_or_404(id)


@router.post("/post-create", status_code=201)
def create_one_post(post: PostCreate):
    with get_db_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (post.title, post.content),
        )
        conn.commit()
        last_id = cursor.lastrowid

    return {"id": last_id, "title": post.title, "content": post.content}


@router.get("/post-all", response_model=list[PostResponse])
def get_all_post():
    with get_db_connection() as conn:
        posts = conn.execute("SELECT * FROM posts").fetchall()

    return [dict(row) for row in posts]


@router.get("/post-table", response_class=HTMLResponse)
def get_post_table(request: Request):
    with get_db_connection() as conn:
        posts = conn.execute("SELECT * FROM posts").fetchall()

    return templates.TemplateResponse(
        request,
        "partials/table.html",
        context={"posts": posts},
    )


@router.post("/post-ui", response_class=HTMLResponse)
def create_from_ui(title: str = Form(...), content: str = Form(...)):
    with get_db_connection() as conn:
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content),
        )
        conn.commit()

    return HTMLResponse(
        content=f"""
        <div class="alert alert-success">
            Post creado correctamente: <strong>{title}</strong>
        </div>
        """
    )


@router.get("/posts/search", response_class=HTMLResponse)
def search_posts(request: Request, q: str = Query("")):
    search_term = f"%{q}%"

    with get_db_connection() as conn:
        posts = conn.execute(
            "SELECT * FROM posts WHERE title LIKE ? OR content LIKE ?",
            (search_term, search_term),
        ).fetchall()

    return templates.TemplateResponse(
        request,
        "partials/table.html",
        context={"posts": posts},
    )