"""
Main application entry point for the Novel Translation and Publishing System.
Orchestrates the workflow between translation and publishing components.
"""

import json

import pandas as pd
from get_the_novel import get_the_novel_pages, get_novel_page
from page_translator import page_translate
import os
from posting import posting_the_chapter
from datetime import date, datetime, timedelta
from time import sleep
from novel_update import save_to_csv

df = pd.DataFrame(columns=["name","url","posted","breakoff page","last page","series_id","post url","chapter","post date"])

# Function to handle the main logic
def novel_translate_and_post(data):
    global sections, df
    # Get the number of pages of the novel
    novel_page_url = data["url"].replace("https://www.52shuku.vip/", "").replace(".html","")
    data["last page"] = get_the_novel_pages(novel_page_url)

    # Get all the pages
    for i in range(data["breakoff page"], data["last page"] + 1):
        try:
            text = get_novel_page(novel_page_url, i)[0]
            # Send the page to the translator
            if i == 2:
                # Load the tags from the JSON file
                with open('nu_all_tags.json', 'r') as file:
                    seo_tags = json.load(file)

                # More comprehensive validation
                if not data.get("series_id") or not isinstance(data.get("series_id"), str):
                    data["series_id"] = "Insert Novel Name Here"

                prompt = f'''
                Translate the following text to English and correct the grammar. After translating, format the text with the following structure:

                1. **Novel Name**: {data["series_id"]}
                2. **Chapter Name / Title**: Format as "Chapter {i-1}): <Chapter Name>" (if not found, make up according to content)
                3. **Meta Title**: Insert a suitable meta title for the chapter here.
                4. **Meta Description**: Insert a suitable meta description for the chapter here.
                5. **Synopsis**: Insert the summary / introduction / novel summary here (Only if available on the page otherwise mark it as N/A)
                    - Keep it as paragraphs. Start with a newline.
                6. **Content**: Insert the chapter content Here (keep it as paragraphs. Start with a newline.)
                    - Translate the text and correct grammar.
                    - Remove chapter name if it is in the content (only from the content)
                    - Add a new line after the text.
                7. **SEO Tags**: Add relevant SEO tags for the novel and chapter using this {seo_tags} list. Add it as a list []. Do not add any quotes.
                8. Anything else: (Name this bullet properly)

                Text to translate and correct:
                    {text}
                '''
            else:
                prompt = f'''
                Translate the following text to English and correct the grammar. After translating, format the text with the following structure:

                1. **Novel Name**: {data["series_id"]}
                2. **Chapter Name / Title**: Format as "Chapter {i-1}: <Chapter Name>" (if not found, make up according to content)
                3. **Meta Title**: Insert a suitable meta title for the chapter here.
                4. **Meta Description**: Insert a suitable meta description for the chapter here.
                5. **Content**: Insert the chapter content Here (keep it as paragraphs. Start with a newline.)
                    - Translate the text and correct grammar.
                    - Remove chapter name if it is in the content (only from the content)
                    - Add a new line after the text.
                6. **SEO Tags**: Add relevant SEO tags for the novel and chapter. Add it as a list []. Do not add any quotes.
                7. Anything else: (Name this bullet properly)

                Text to translate and correct:
                    {text}
                '''
            
            text = page_translate(prompt)

            # Import here to avoid circular import
            from posting import dividing_text
            sections = dividing_text(text)
            sections["Last Page"] =  data["last page"] - 1
            
            if i == 2:
                data["series_id"] = sections['Novel Name']
                sections['post date'] = datetime.now()
            else:
                sections['Novel Name'] = data["series_id"]
                sections['post date'] = datetime.strptime(data['post date'], "%m/%d/%y")
            print("Posting...")
            sections['Page Number'] = i - 1
            post_url = posting_the_chapter(sections)

            if i == 2:
                sections['Content'] = sections['Synopsis']
                sections['chapter Name / Title'] = data["series_id"]
                sections['Page Number'] = 0
                post_url = posting_the_chapter(sections)
                print(post_url)
            print(post_url)

            try:
                file_name = f"novels/{data['series_id'].replace(' ', '-').lower()}"
                if not os.path.exists(file_name):
                    os.makedirs(file_name)
                    os.chmod(file_name, 0o0777)
                file_name = file_name + f'/chapter-{i-2}.txt'
                with open(file_name, 'x',  encoding='utf-8') as output:
                    output.write(text)
            except Exception as e:
                print(f"Error creating file: {e}")

            # add data back
            data["breakoff page"] = i + 1
            data["post url"] = post_url
            data["chapter"] = "c"+ str(sections['Page Number'])
            post_date = date.today() + timedelta(days=sections['Page Number'])
            post_date = str(post_date.strftime('%m/%d/%y'))
            data["post date"] = post_date

            df = save_to_csv(data, df)
            post_data(all_novels, data)

            if sections['Page Number'] >= 51:
                data["posted"] = "yes"
                break

        except Exception as e:
            print(e)
            sleep(1000)

    if data["breakoff page"] > data["last page"]:
        data["posted"] = "yes"
    return data

def get_current_novel_path():
  current_date = datetime.now()
  file_name = f"{current_date.year}_{current_date.strftime('%m')}_novels.json"

  # Create directory if it doesn't exist
  os.makedirs('all_novels', exist_ok=True)

  return os.path.join('all_novels', file_name)

def initialize_json_if_not_exists(file_path):
  if not os.path.exists(file_path):
      with open(file_path, 'w') as f:
          json.dump([], f)

# Get novel
def get_novel():
  # Get path to current novels.json
  novel_path = get_current_novel_path()
  initialize_json_if_not_exists(novel_path)

  # Get new novels
  posting_novel = {}
  with open(novel_path, 'r') as f:
      all_novels = json.load(f)

  return all_novels

# Send data back to json
def post_data(all_novels, data):
  novel_path = get_current_novel_path()

  for key, i in enumerate(all_novels):
      if i["url"] == data["url"]:
          all_novels[key] = data
          break

  with open(novel_path, "w") as out_file:
      json.dump(all_novels, out_file)
  return "posted"

# Main execution
all_novels = get_novel()

for i in all_novels:
    if i["posted"] == "no":

        if i != {}:
            try:
                data = novel_translate_and_post(i)
            except Exception as e:
                print(e)
                i["breakoff page"] = 2
                data = novel_translate_and_post(i)
            print(post_data(all_novels, data))
