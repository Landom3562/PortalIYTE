from functools import wraps
import mysql.connector
from flask import Blueprint
from flask import request, jsonify
import pdb
from datetime import datetime
from config import sql_address, sql_user, sql_password, sql_database
from controller.commentController import get_comments
import jellyfish

search_bp = Blueprint('search', __name__, url_prefix="/api")
prefix = "/search"

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=sql_address,
    user=sql_user,
    password=sql_password,
    database=sql_database,
    autocommit=True,
    ssl_disabled=True  # Disable SSL
)

similarity_threshold = 0.7

def ensure_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn.ping(reconnect=True)
        except mysql.connector.Error:
            conn.reconnect()
        return func(conn, *args, **kwargs)
    return wrapper

@search_bp.route(prefix + '/post/<query>', methods=['GET'])
@ensure_connection
def search_post(conn, query):
    with conn.cursor(dictionary=True) as cur:
        cur.execute("SELECT * FROM post_details")
        rows = cur.fetchall()
        response = []
        for row in rows:
            if(jellyfish.jaro_similarity(row["post_title"], query) > similarity_threshold):
                post = {
                    "postId": row["post_id"],
                    "title": row["post_title"],
                    "content": row["post_content"],
                    "image": row["post_image"],
                    "likeCount": row["post_like_count"],
                    "commentCount": row["post_comment_count"],
                    "createDate": row["post_create_date"],
                    "user": {
                        "userId": row["user_id"],
                        "username": row["user_username"],
                        "profilePicture": row["user_profile_picture"]
                    },
                    "topic": {
                        "topicId": row["topic_id"],
                        "name": row["topic_name"],
                        "logo": row["topic_logo"]
                    },
                    "comments": []
                }
                post["comments"] = get_comments(row["post_id"])
                response.append(post)
        return jsonify(response)

@search_bp.route(prefix + '/topic/<query>', methods=['GET'])
@ensure_connection
def search_topic(conn, query):
    with conn.cursor(dictionary=True) as cur:
        cur.execute("SELECT * FROM topic")
        rows = cur.fetchall()
        response = []
        for row in rows:
            if(jellyfish.jaro_similarity(row["name"], query) > similarity_threshold):
                response.append({"id": row["id"], "name": row["name"], "description": row["description"], "logo": row["logo"]})
            return jsonify(response)

@search_bp.route(prefix + '/user/<query>', methods=['GET'])
@ensure_connection
def search_user(conn, query):
    with conn.cursor(dictionary=True) as cur:
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
        response = []
        for row in rows:
            if(jellyfish.jaro_similarity(row["username"], query) > similarity_threshold):
                response.append({"id": row["id"], "email": row["email"], "phoneNumber": row["phone_number"], "username": row["username"], "bio": row["bio"], "profilePicture": row["profile_picture"], "createTime": row["create_date"], "postCount": row["post_count"], "followerCount": row["follower_count"], "followingCount": row["following_count"]})
            return jsonify(response)