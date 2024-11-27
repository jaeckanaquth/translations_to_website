"""
posting.py
Description: Manages WordPress post creation and updates
"""

"""
WordPress integration for automated post creation and management.
Handles authentication, post formatting and publishing.
"""

API_VERSION = 'wp/v2'  # WordPress REST API version
BATCH_SIZE = 10        # Number of posts to process in batch

class WordPressHandler:
    """Manages WordPress post operations and authentication."""
    
    def __init__(self):
        """Initialize WordPress connection and credentials."""
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
from datetime import datetime, timedelta
load_dotenv()

def acronym(title):
    """
    Generates acronym from novel title.
    
    Args:
        title (str): Full novel title
        
    Returns:
        str: Generated acronym
    """

def calculate_post_date(date_str):
    """
    Calculates posting date based on input string.
    
    Args:
        date_str (str): Date string to process
        
    Returns:
        datetime: Processed post date
    """

def posting_the_chapter(title, content, tags):
    """
    Posts chapter content to WordPress.
    
    Args:
        title (str): Chapter title
        content (str): Chapter content
        tags (list): Associated tags
        
    Returns:
        bool: Success status
    """
    
    tags = sections["SEO Tags"].split(',')
    tags = [i.replace('[','').replace(']','').replace("\'","").replace('\"','').lstrip() for i in tags]
    chapter_tag = f"{acronym(sections['Novel Name'])} c{sections['Page Number']}"
    tags.append(chapter_tag)
    category_slug = sections['Novel Name'].replace(" ", "-").lower()
    next_post_slug = f"chapter-{acronym(sections['Novel Name'])}_{int(sections['Page Number'])+1}"
    back_post_slug = f"chapter-{acronym(sections['Novel Name'])}_{int(sections['Page Number'])-1}"
    next_chapter_url = f"https://{os.getenv('Website')}/{category_slug}/{next_post_slug}"
    back_chapter_url = f"https://{os.getenv('Website')}/{category_slug}/{back_post_slug}"
    site_url = "https://" + os.getenv("Website") + "/xmlrpc.php"
    username = os.getenv("WP_USER")
    application_password = os.getenv("WP_PASSWORD")

    client = Client(site_url, username, application_password)
    response = requests.get(
        f"{site_url}/wp-json/wp/v2/posts",
        auth=HTTPBasicAuth(username, application_password)
    )
    post = WordPressPost()
    
    if sections['Page Number'] == 0:
       post.title = sections['Novel Name']
       post.terms_names = {
        'post_tag': tags,
        'category': ["Novel Title Pages"],
    }
    else: 
        post.title = sections['Chapter Name / Title']
        post.terms_names = {
            'post_tag': tags,
            'category': [sections['Novel Name']],
        }
    if sections['Page Number'] == 1:
        next_button = f'<a href={next_chapter_url}>Next >></a>'      # Replace with actual URL
        post.content = f'{sections["Content"]}<br><div style="text-align: right;">{next_button}</div>'
    elif sections['Page Number'] == 0:
        post.content = f"{sections['Content']}"
    elif sections["Page Number"] == sections["Last Page"]:
        back_button = f'<a href={back_chapter_url}><< Back</a>'  # Replace with actual URL
        post.content = f'{sections["Content"]}<br><div style="text-align: right;">{back_button}</div>'
    else:
        back_button = f'<a href={back_chapter_url}><< Back</a>'  # Replace with actual URL
        next_button = f'<a href={next_chapter_url}>Next >></a>'      # Replace with actual URL
        post.content = f'{sections["Content"]}<br><div style="text-align: right;">{back_button} | {next_button}</div>'
      # Set the slug
    if sections['Page Number'] == 0:
        post.slug = category_slug
        post_slug = category_slug
    else:
        post.slug = f"chapter-{acronym(sections['Novel Name'])}_{sections['Page Number']}"
        post_slug = f"chapter-{acronym(sections['Novel Name'])}_{sections['Page Number']}"
        
    post.id = client.call(posts.NewPost(post))

    post.date = calculate_post_date(sections)

    # Set custom fields for meta title and meta description
    post.custom_fields = [
        {'key': 'meta_title', 'value': sections['Meta Title']},
        {'key': 'meta_description', 'value': sections['Meta Description']}
    ]
    post.comment_status = 'open'
    post.post_status = 'publish'
    client.call(posts.EditPost(post.id, post))
    if sections['Page Number'] == 0:
        post_url = f"https://{os.getenv('Website')}/novel-title-pages/{category_slug}"
    else:
        post_url = f"https://{os.getenv('Website')}/{category_slug}/{post_slug}"
    return post_url


def dividing_text(formatted_text):
  sections = {
      "Novel Name": "",
      "Chapter Name / Title": "",
      "Synopsis": "",
      "Content": "",
      "SEO Tags": "",
      "Meta Title": "",  # New field for meta title
      "Meta Description": "",  # New field for meta description
      "Page Number": 0,
      "Last Page": 0
  }
  
  # Regular expression patterns
  novel_name_pattern = r"\*\*Novel Name\*\*:\s*(.+)"
  chapter_title_pattern = r"\*\*Chapter Name / Title\*\*:\s*(.+)"
  synopsis_pattern = r"\*\*Synopsis\*\*:\s*(.+?)(?=[5]\. \*\*Content\*\*|$)"
  content_pattern = r"\*\*Content\*\*:\s*(.+?)(?=[67]\. \*\*SEO Tags\*\*|$)"
  seo_tags_pattern = r"\*\*SEO Tags\*\*:\s*(.+)"
  meta_title_pattern = r"\*\*Meta Title\*\*:\s*(.+)"  # New pattern for meta title
  meta_description_pattern = r"\*\*Meta Description\*\*:\s*(.+)"  # New pattern for meta description

  # Search for matches
  novel_name_match = re.search(novel_name_pattern, formatted_text)
  chapter_title_match = re.search(chapter_title_pattern, formatted_text)
  synopsis_match = re.search(synopsis_pattern, formatted_text, re.DOTALL)
  content_match = re.search(content_pattern, formatted_text, re.DOTALL)
  seo_tags_match = re.search(seo_tags_pattern, formatted_text)
  meta_title_match = re.search(meta_title_pattern, formatted_text)
  meta_description_match = re.search(meta_description_pattern, formatted_text)

  # Extract and assign matches to dictionary
  if novel_name_match:
      sections["Novel Name"] = novel_name_match.group(1).strip()
  if chapter_title_match:
      sections["Chapter Name / Title"] = chapter_title_match.group(1).strip()
  if synopsis_match:
      sections["Synopsis"] = synopsis_match.group(1).strip()
  if content_match:
      sections["Content"] = content_match.group(1).strip()
  if seo_tags_match:
      sections["SEO Tags"] = seo_tags_match.group(1).strip()
  if meta_title_match:
      sections["Meta Title"] = meta_title_match.group(1).strip()  # Capture meta title
  if meta_description_match:
      sections["Meta Description"] = meta_description_match.group(1).strip()  # Capture meta description

  return sections
