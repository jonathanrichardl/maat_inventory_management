## Drive Image Uploader

### How to get started:
1. [Open Google Cloud Console.](https://console.cloud.google.com/apis/)
2. Create your first Google Cloud Project and download Client File. You can follow [this tutorial.](https://youtu.be/6bzzpda63H0)
3. Put the secret_client.json from step 2 to the root folder.
4. Change the **.env.example** to the **.env** and change the CLIENT_SECRET_FILE=*your_secret_client.json*
5. Enable your Google Drive API. You can follow [this tutorial.](https://www.youtube.com/watch?v=9K2P2bWEd90&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz&index=1&ab_channel=JieJenn)
6. Open [Google Drive](https://drive.google.com/). Create a new folder. Open the folder and copy the URL part after the last **/**. For example = https://drive.google.com/drive/u/0/folders/copy_only_this_string_id
7. Paste the string from step 6 to the **.env** to FOLDER_ID=your_folder_id_from_the_last_drive_folder_url.
8. Install the requirements.txt. You can use **pip install -r requirements.txt** or creating the virtualenv before install the requirements (optional).
9. Run the gui.py and try to upload a JPG/JPEG file.
10. Refresh your Google Drive Folder page from step 6.
11. Your file is uploaded!

### Potential Problem and Solution
1. Error: *The developer hasn’t given you access to this app. It’s currently being tested and it hasn’t been verified by Google. If you think you should have access, contact the developer* <br>
Solution: Open Google Cloud Console > Select OAuth consent screen > Scroll down to the *Test users* section > Add your email (the same email as your Google Cloud Console account)


### References:
1. Youtube Playlist to create and upload files to Drive: https://youtube.com/playlist?list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz


