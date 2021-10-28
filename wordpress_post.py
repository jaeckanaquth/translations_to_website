import github_config as config
import requests
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc import WordPressTerm
from bs4 import BeautifulSoup as bs
from wordpress_xmlrpc.methods import taxonomies

client = Client(config.my_site, config.user, config.password)
# print(posting.split(","))

def posting_test(heading, df):
    posting = client.call(posts.GetPosts())
    posting = [str(i) for i in posting]
    for j, p in enumerate(posting):
        [p.replace(i, '') for i in config.special]
        posting[j] = p
    print(posting, heading)
    if heading == "Works related":
        return "Summary post seprately"
    elif heading in posting or heading in df['name'].to_list():
        return "Already posted"
    else:
        return "Need to be posted"
        
def posting(heading, content):
    print(heading)
    # heading = 'test'
    post = WordPressPost()
    post.title = heading
    post.terms_names = {
        'post_tag': config.tags,
        'category': [config.novel_name],
    }
    post.content = content
    post.id = client.call(posts.NewPost(post))
    post.post_status = 'publish'
    client.call(posts.EditPost(post.id, post))
    print(post)
    return post.id
        

def uploadImage(novel_img, img_data):
    data = {
        'name': novel_img,
        'type': 'image/jpeg',
    }
    data['bits'] = xmlrpc_client.Binary(img_data)
    response = client.call(media.UploadFile(data))
    attachment_id = response['id']
    return attachment_id
