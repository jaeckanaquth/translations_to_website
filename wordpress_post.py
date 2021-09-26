import config, requests
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts, media
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc import WordPressPost

url = config.my_site
client = Client(url, config.user, config.password)
posting = client.call(posts.GetPosts())
posting = str(posting).replace("<","")
posting = str(posting).replace(">","")
posting = str(posting).replace(" WordPressPost: ","")
posting = str(posting).replace("b","")
posting = str(posting).replace("'","")
posting = str(posting).replace("[","")
posting = str(posting).replace("]","")
print(posting.split(","))

def posting_draft(heading, content):
    if heading not in posting:
        post = WordPressPost()
        post.title = heading
        post.content = content
        post.id = client.call(posts.NewPost(post))
        # whoops, I forgot to publish it!
        post.post_status = 'draft'
        client.call(posts.EditPost(post.id, post))
        return post.id
    else:
        return "Already posted"

def uploadImage(img_path):
    data = {
            'name': img_path,
            'type': 'image/jpeg',  # mimetype
    }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(img_path, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

    response = client.call(media.UploadFile(data))
    attachment_id = response['id']
    return attachment_id
