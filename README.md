# Twitter API Like Script 🐦

## Overview

This script uses the Twitter API and Python (`tweepy`) to authenticate a user and like a specific tweet by its Tweet ID.

---

## 🔧 Requirements

- Python 3.x
- Twitter Developer Account + App Credentials
- Tweepy (`pip install tweepy`)
- dotenv (`pip install python-dotenv`)

---

## 🔑 Setup

⚠️ **Important Note on Access Levels**  
This script uses the Twitter API endpoint to like tweets, which requires **Elevated Access**.  
By default, new Twitter Developer accounts have only **Essential Access**, which does **NOT** allow liking tweets via the API.  
To use this script, apply for Elevated Access here:  
👉 [https://developer.twitter.com/en/portal/products](https://developer.twitter.com/en/portal/products)

1. Go to [https://developer.twitter.com/en/portal/dashboard](https://developer.twitter.com/en/portal/dashboard) and create a project/app.
2. Generate your keys:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret
3. Fill them in the `.env` file.

---

## 📁 File Structure

- `twitter_liker.py`: Main Python script
- `.env`: Environment variables file (never share real credentials)
- `README.md`: You're reading it!

---

## 🚀 Usage

1. Replace `REPLACE_WITH_TWEET_ID` in `twitter_liker.py` with an actual tweet ID.
   - To get a Tweet ID, copy the URL of any tweet and use the number at the end.
   - Example: `https://twitter.com/username/status/1234567890123456789` → `1234567890123456789`

2. Run the script:

```bash
python twitter_liker.py