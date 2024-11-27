import os
from time import sleep
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from posting import acronym  # Assuming this is a custom function you have
load_dotenv()

# Configuration
site_url = "https://" + os.getenv("Website") + "/wp-json/wp/v2"
username = os.getenv("WP_USER")
application_password = os.getenv("WP_password")

def get_posts(page=1, per_page=100):
    response = response = requests.get(
        f'{site_url}/posts?page={page}&per_page={per_page}&status=publish,future,draft',
        auth=HTTPBasicAuth(username, application_password)
        )
    response.raise_for_status()
    return response.json()

def get_all_posts():
  all_posts = []
  page = 1
  per_page = 100  # Number of posts per page

  while True:
      # Include 'status' parameter to fetch scheduled posts
      response = requests.get(
          f'{site_url}/posts?page={page}&per_page={per_page}&status=future',
          auth=HTTPBasicAuth(username, application_password)
      )
      
      # Check for errors
      try:
          response.raise_for_status()
      except requests.exceptions.HTTPError as e:
          print(f"Error fetching posts on page {page}: {e}")
          print(f"Response content: {response.content}")  # Print the response content for debugging
          break  # Exit the loop on error

      posts = response.json()
      if not posts:  # If no more posts, break the loop
          break
      
      all_posts.extend(posts)
      print(f"Fetched {len(posts)} scheduled posts from page {page}. Total posts fetched: {len(all_posts)}")
      
      # Check if we have reached the last page
      total_pages = int(response.headers.get('X-WP-TotalPages', 0))
      if page >= total_pages:  # If the current page is the last page, break
          break
      
      page += 1  # Increment the page number for the next request

  return all_posts

def get_categories():
  response = requests.get(f'{site_url}/categories', auth=HTTPBasicAuth(username, application_password))
  response.raise_for_status()
  return response.json()

def get_tags():
  response = requests.get(f'{site_url}/tags', auth=HTTPBasicAuth(username, application_password))
  response.raise_for_status()
  return response.json()

def get_or_create_tag(tag_name):
  tags = get_tags()
  # Check if the tag already exists
  for tag in tags:
      if tag['name'] == tag_name:
          return tag['id']  # Return the existing tag ID

  # If the tag does not exist, create it
  response = requests.post(
      f'{site_url}/tags',
      json={'name': tag_name},
      auth=HTTPBasicAuth(username, application_password)
  )
  
  # Check for errors and print the response for debugging
  try:
      response.raise_for_status()
  except requests.exceptions.HTTPError as e:
      # Handle the specific case where the tag already exists
      if response.status_code == 400 and 'term_exists' in response.json().get('code', ''):
          existing_tag_id = response.json()['data']['term_id']
          print(f"Tag '{tag_name}' already exists with ID: {existing_tag_id}")
          return existing_tag_id  # Return the existing tag ID
      else:
          print(f"Error creating tag '{tag_name}': {e}")
          print(f"Response content: {response.content}")  # Print the response content for debugging
          raise  # Re-raise the exception after logging

  return response.json()['id']  # Return the new tag ID

def add_tag_to_post(post_id, tag_id):
  # Get the current post
  post_response = requests.get(f'{site_url}/posts/{post_id}', auth=HTTPBasicAuth(username, application_password))
  post_response.raise_for_status()
  post = post_response.json()

  # Get existing tags
  existing_tags = post.get('tags', [])

  # Add new tag if it doesn't already exist
  if tag_id not in existing_tags:
      # Update the post with the new tag
      updated_tags = existing_tags + [tag_id]
      update_response = requests.post(
          f'{site_url}/posts/{post_id}',
          json={'tags': updated_tags},
          auth=HTTPBasicAuth(username, application_password)
      )
      update_response.raise_for_status()
      print(f"Updated post {post_id} with new tag ID: {tag_id}")
  else:
      print(f"Post {post_id} already has the tag ID: {tag_id}")

# Main execution
posts = get_all_posts()  # Use the new function to get all posts
categories = get_categories()

for post in posts:
    try:
        post_id = post['id']
        post_slug = post['slug']
        print(f"Processing post slug: {post_slug}")
        if "_" in post_slug:
            chapter_num = int(post_slug.split("_")[-1])
        elif "chapter-" in post_slug:
            if "chapter-2" in post_slug:
                chapter_num = 2
            elif "chapter-" in post_slug:
                if len(post_slug.split("-")) == 3:
                    chapter_num = int(post_slug.split("-")[-2])
                else:
                    chapter_num = int(post_slug.split("-")[-1])
        else:
            chapter_num = 0
    
        # Assuming the first category is the one you want to use as a tag
        if post['categories']:
            category_id = post['categories'][0]
            category_name = next((cat['name'] for cat in categories if cat['id'] == category_id), None)
            if category_name:
                tagname = f"{acronym(category_name)} c{chapter_num}"
                print(f"Tag name to be added: {tagname}")
                tag_id = get_or_create_tag(tagname)  # Get or create the tag and get its ID
                add_tag_to_post(post_id, tag_id)
    except Exception as e:
        print(e)
        sleep(10)

# Removed the break statement to process all posts
