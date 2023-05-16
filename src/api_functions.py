#works! 
## 1) find email for the certain query i.e. 'report*csv' in attachment name
## 2) get message ids
## 3) get attachments ids
## 4) downloads attachments for every found email

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
import base64
import os
import time


def search_email(service, query_string,label_ids=[]):
    try:
        message_list_response = service.users().messages().list(
            userId='me',
            labelIds=label_ids,
            q=query_string
        ).execute()

        message_items=message_list_response.get('messages')
        nextPageToken=message_list_response.get('nextPageToken')

        while nextPageToken:
            message_list_response = service.users().messages().list(
                    userId='me',
                    labelIds=label_ids,
                    q=query_string,
                    pageToken=nextPageToken
            ).execute()    

            message_items.extend(message_list_response.get('messages'))
            nextPageToken=message_items.get('nextPageToken')
        return message_items
    except Exception as e:
        return 'No emails found'

def get_message_detail(service, msg_id,msg_format='metadata',metadata_headers: list=None):
    # SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    # creds = Credentials.from_authorized_user_file('../token.json', SCOPES)
    #service = build('gmail', 'v1', credentials=creds)
    message_detail=service.users().messages().get(
        userId='me',
        id=msg_id,
        format=msg_format,
        metadataHeaders=metadata_headers
    ).execute()
    return message_detail

def get_file_data(service,message_id,attachment_id,file_name,save_location):
    response=service.users().messages().attachments().get(
        userId='me',
        messageId=message_id,
        id=attachment_id
    ).execute()

    file_data=base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
    return file_data